import requests
import time
import copy
from concurrent.futures import ThreadPoolExecutor, as_completed

# -------------------------
# HEADERS (keep browser-like UA)
# -------------------------
headers = {
    "accept": "*/*",
    "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/json",
    "origin": "https://www.jiomart.com",
    "referer": "https://www.jiomart.com/search?q=milk",
    "user-agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
}

# -------------------------
# BASE REQUEST BODY
# -------------------------
json_data = {
    "query": "milk",
    "pageSize": 500,
    "facetSpecs": [
        {"facetKey": {"key": "brands"}, "limit": 500, "excludedFilterKeys": ["brands"]},
        {"facetKey": {"key": "categories"}, "limit": 500, "excludedFilterKeys": ["categories"]},
        {"facetKey": {"key": "attributes.category_level_4"}, "limit": 500, "excludedFilterKeys": ["attributes.category_level_4"]},
        {"facetKey": {"key": "attributes.category_level_1"}, "excludedFilterKeys": ["attributes.category_level_4"]},
        {
            "facetKey": {
                "key": "attributes.avg_selling_price",
                "return_min_max": True,
                "intervals": [{"minimum": 0.1, "maximum": 100000000}],
            }
        },
        {
            "facetKey": {
                "key": "attributes.avg_discount_pct",
                "return_min_max": True,
                "intervals": [{"minimum": 0, "maximum": 99}],
            }
        },
    ],
    "variantRollupKeys": ["variantId"],
    "branch": "projects/sr-project-jiomart-jfront-prod/locations/global/catalogs/default_catalog/branches/0",
    "queryExpansionSpec": {"condition": "AUTO", "pinUnexpandedResults": True},
    "userInfo": {"userId": None},
    "spellCorrectionSpec": {"mode": "AUTO"},
    "filter": (
        'attributes.status:ANY("active") AND '
        '(attributes.mart_availability:ANY("JIO","JIO_WA")) AND '
        '(attributes.available_regions:ANY("PANINDIAGROCERIES")) AND '
        '(NOT attributes.vertical_code:ANY("ALCOHOL"))'
    ),
    "visitorId": "anonymous",
}

SEARCH_URL = "https://www.jiomart.com/trex/search"


# -------------------------
# WORKER FUNCTION (ONE PINCODE)
# -------------------------
def fetch_by_pincode(pincode):
    session = requests.Session()
    session.headers.update(headers)

    # Set only pincode cookie (city auto-resolved)
    session.cookies.set("nms_mgo_pincode", pincode)

    all_products = []
    next_page_token = None
    page = 1

    while True:
        payload = copy.deepcopy(json_data)

        if next_page_token:
            payload["pageToken"] = next_page_token

        resp = session.post(SEARCH_URL, json=payload, timeout=30)

        if resp.status_code != 200:
            print(f"❌ {pincode} | page {page} | HTTP {resp.status_code}")
            break

        data = resp.json()

        products = data.get("results") or data.get("products") or []
        all_products.extend(products)

        print(f"✅ {pincode} | page {page} | {len(products)} items")

        next_page_token = data.get("nextPageToken")
        if not next_page_token:
            break

        page += 1
        time.sleep(0.3)  # anti-block delay

    return pincode, all_products


# -------------------------
# MAIN (PARALLEL EXECUTION)
# -------------------------
if __name__ == "__main__":
    pincodes = ["110001", "400001", "560001", "380000"]

    final_data = {}

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(fetch_by_pincode, p) for p in pincodes]

        for future in as_completed(futures):
            pincode, products = future.result()
            final_data[pincode] = products
            print(f"🎉 DONE {pincode} → TOTAL {len(products)} products")

    print("\nAll pincodes completed.")
