import requests
import json
import time

url = "https://www.zomato.com/webroutes/search/home"

headers = {
    "accept": "*/*",
    "content-type": "application/json",
    "origin": "https://www.zomato.com",
    "referer": "https://www.zomato.com/ahmedabad/delivery/dish-dosa",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "x-zomato-csrft": "d9a1e2939e03d2c425adfec5206a45f9",
}

cookies = {
    "csrf": "d9a1e2939e03d2c425adfec5206a45f9",
    "fbcity": "11",
}

processed_chain_ids = []
shown = 0
search_id = "0c86c715-1486-41a7-b022-2b8ee29b7333"

all_names = set()

while True:
    filters = {
        "searchMetadata": {
            "previousSearchParams": json.dumps({
                "PreviousSearchId": search_id,
                "PreviousSearchFilter": [
                    {"category_context": "delivery_home"},
                    "",
                    {"universal_dish_ids": ["10296"]}
                ]
            })
        },
        "postbackParams": json.dumps({
            "processed_chain_ids": processed_chain_ids,
            "shown_res_count": shown,
            "search_id": search_id
        }),
        "totalResults": 35,
        "hasMore": True,
        "getInactive": False
    }

    payload = {
        "context": "delivery",
        "filters": json.dumps(filters),
        "addressId": 0,
        "entityId": 11,
        "entityType": "city",
        "cityId": 11,
        "latitude": "23.042662",
        "longitude": "72.566729",
        "placeId": "3720",
        "isO2City": True
    }

    r = requests.post(url, headers=headers, cookies=cookies, json=payload)
    print("Status:", r.status_code)

    if r.status_code != 200:
        break

    data = r.json()

    results = data["sections"]["SECTION_SEARCH_RESULT"]
    meta = data["sections"]["SECTION_SEARCH_META_INFO"]["searchMetaData"]

    if not results:
        break

    for item in results:
        info = item["info"]
        name = info["name"]
        all_names.add(name)
        print(name)

        chain_id = info.get("chain_id")
        if chain_id and chain_id not in processed_chain_ids:
            processed_chain_ids.append(chain_id)

    shown += len(results)

    if not meta["hasMore"]:
        break

    time.sleep(1.5)  # IMPORTANT: slow down

print("\nTOTAL UNIQUE RESTAURANTS:", len(all_names))
