import requests

cookies = {
    '_fbp': 'fb.1.1767364027652.1536523600',
    'WZRK_G': '80e6129121bb49e5bf5f938120ab3dc0',
    '_gcl_au': '1.1.1211049607.1767364029',
    '_ga': 'GA1.1.1353623878.1767364029',
    'nms_mgo_state_code': 'GJ',
    '_gcl_gs': '2.1.k1$i1767411998$u220930947',
    '_gcl_aw': 'GCL.1767412033.Cj0KCQiA9t3KBhCQARIsAJOcR7wqa53wxLvXn9z2W_xLxur6lzKQkb061UxURoPYFS1Y3Zcp5tw7ONoaAtsEEALw_wcB',
    'AKA_A2': 'A',
    '__tr_jr': 'W3sidXRtcyI6Im9yZ2FuaWMiLCJ0cyI6IjIwMjYtMDEtMDRUMDQ6NTc6MDQuMDUyWiIsImVuYyI6InllcyJ9XQ==',
    'nms_mgo_pincode': '380000',
    'nms_mgo_city': 'AHMEDABAD',
    '__tr_luptv': '1767502665502',
    'RT': '"z=1&dm=www.jiomart.com&si=3c60f3dc-fc74-4e39-8698-eb31c3eb19cf&ss=mjz9fbc0&sl=3&tt=2b1&obo=1&rl=1"',
    '_ga_XHR9Q2M3VV': 'GS2.1.s1767502624$o3$g1$t1767502685$j59$l0$h335475436',
    'WZRK_S_88R-W4Z-495Z': '%7B%22p%22%3A4%2C%22s%22%3A1767502608%2C%22t%22%3A1767502685%7D',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.jiomart.com',
    'priority': 'u=1, i',
    'referer': 'https://www.jiomart.com/search?q=milk',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    # 'cookie': '_fbp=fb.1.1767364027652.1536523600; WZRK_G=80e6129121bb49e5bf5f938120ab3dc0; _gcl_au=1.1.1211049607.1767364029; _ga=GA1.1.1353623878.1767364029; nms_mgo_state_code=GJ; _gcl_gs=2.1.k1$i1767411998$u220930947; _gcl_aw=GCL.1767412033.Cj0KCQiA9t3KBhCQARIsAJOcR7wqa53wxLvXn9z2W_xLxur6lzKQkb061UxURoPYFS1Y3Zcp5tw7ONoaAtsEEALw_wcB; AKA_A2=A; __tr_jr=W3sidXRtcyI6Im9yZ2FuaWMiLCJ0cyI6IjIwMjYtMDEtMDRUMDQ6NTc6MDQuMDUyWiIsImVuYyI6InllcyJ9XQ==; nms_mgo_pincode=380000; nms_mgo_city=AHMEDABAD; __tr_luptv=1767502665502; RT="z=1&dm=www.jiomart.com&si=3c60f3dc-fc74-4e39-8698-eb31c3eb19cf&ss=mjz9fbc0&sl=3&tt=2b1&obo=1&rl=1"; _ga_XHR9Q2M3VV=GS2.1.s1767502624$o3$g1$t1767502685$j59$l0$h335475436; WZRK_S_88R-W4Z-495Z=%7B%22p%22%3A4%2C%22s%22%3A1767502608%2C%22t%22%3A1767502685%7D',
}

json_data = {
    'query': 'milk',
    'pageSize': 100,
    'facetSpecs': [
        {
            'facetKey': {
                'key': 'brands',
            },
            'limit': 500,
            'excludedFilterKeys': [
                'brands',
            ],
        },
        {
            'facetKey': {
                'key': 'categories',
            },
            'limit': 500,
            'excludedFilterKeys': [
                'categories',
            ],
        },
        {
            'facetKey': {
                'key': 'attributes.category_level_4',
            },
            'limit': 500,
            'excludedFilterKeys': [
                'attributes.category_level_4',
            ],
        },
        {
            'facetKey': {
                'key': 'attributes.category_level_1',
            },
            'excludedFilterKeys': [
                'attributes.category_level_4',
            ],
        },
        {
            'facetKey': {
                'key': 'attributes.avg_selling_price',
                'return_min_max': True,
                'intervals': [
                    {
                        'minimum': 0.1,
                        'maximum': 100000000,
                    },
                ],
            },
        },
        {
            'facetKey': {
                'key': 'attributes.avg_discount_pct',
                'return_min_max': True,
                'intervals': [
                    {
                        'minimum': 0,
                        'maximum': 99,
                    },
                ],
            },
        },
    ],
    'variantRollupKeys': [
        'variantId',
    ],
    'branch': 'projects/sr-project-jiomart-jfront-prod/locations/global/catalogs/default_catalog/branches/0',
    'queryExpansionSpec': {
        'condition': 'AUTO',
        'pinUnexpandedResults': True,
    },
    'userInfo': {
        'userId': None,
    },
    'spellCorrectionSpec': {
        'mode': 'AUTO',
    },
    'filter': 'attributes.status:ANY("active") AND (attributes.mart_availability:ANY("JIO", "JIO_WA")) AND (attributes.available_regions:ANY("PANINDIABOOKS", "PANINDIACRAFT", "PANINDIADIGITAL", "PANINDIAFASHION", "PANINDIAFURNITURE", "PANINDIAGROCERIES", "PANINDIAHOMEANDKITCHEN", "PANINDIAHOMEIMPROVEMENT", "PANINDIASTL")) AND (attributes.inv_stores_1p:ANY("ALL", "SANR", "SANS", "SURR", "SANQ", "S4LI", "S535", "SXJJ", "R741", "R300", "SAFY", "SLI1", "S0XN", "SZBL", "Y524", "SJ14", "V012", "SL9F", "R975", "S402", "V017", "SL7L", "SB41", "SLTP", "SL7Q", "SG84", "SL7O", "SH09", "V027", "S352") OR attributes.inv_stores_3p:ANY("ALL", "groceries_zone_non-essential_services", "general_zone", "groceries_zone_essential_services", "fashion_zone", "electronics_zone")) AND ( NOT attributes.vertical_code:ANY("ALCOHOL"))',
    'canonicalFilter': 'attributes.status:ANY("active") AND (attributes.mart_availability:ANY("JIO", "JIO_WA")) AND (attributes.available_regions:ANY("PANINDIABOOKS", "PANINDIACRAFT", "PANINDIADIGITAL", "PANINDIAFASHION", "PANINDIAFURNITURE", "PANINDIAGROCERIES", "PANINDIAHOMEANDKITCHEN", "PANINDIAHOMEIMPROVEMENT", "PANINDIASTL")) AND (attributes.inv_stores_1p:ANY("ALL", "SANR", "SANS", "SURR", "SANQ", "S4LI", "S535", "SXJJ", "R741", "R300", "SAFY", "SLI1", "S0XN", "SZBL", "Y524", "SJ14", "V012", "SL9F", "R975", "S402", "V017", "SL7L", "SB41", "SLTP", "SL7Q", "SG84", "SL7O", "SH09", "V027", "S352") OR attributes.inv_stores_3p:ANY("ALL", "groceries_zone_non-essential_services", "general_zone", "groceries_zone_essential_services", "fashion_zone", "electronics_zone")) AND ( NOT attributes.vertical_code:ANY("ALCOHOL"))',
    'visitorId': 'anonymous-7a1cce40-4a28-493a-bf64-e770d9650310',
}

# response = requests.post('https://www.jiomart.com/trex/search', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"query":"milk","pageSize":50,"facetSpecs":[{"facetKey":{"key":"brands"},"limit":500,"excludedFilterKeys":["brands"]},{"facetKey":{"key":"categories"},"limit":500,"excludedFilterKeys":["categories"]},{"facetKey":{"key":"attributes.category_level_4"},"limit":500,"excludedFilterKeys":["attributes.category_level_4"]},{"facetKey":{"key":"attributes.category_level_1"},"excludedFilterKeys":["attributes.category_level_4"]},{"facetKey":{"key":"attributes.avg_selling_price","return_min_max":true,"intervals":[{"minimum":0.1,"maximum":100000000}]}},{"facetKey":{"key":"attributes.avg_discount_pct","return_min_max":true,"intervals":[{"minimum":0,"maximum":99}]}}],"variantRollupKeys":["variantId"],"branch":"projects/sr-project-jiomart-jfront-prod/locations/global/catalogs/default_catalog/branches/0","queryExpansionSpec":{"condition":"AUTO","pinUnexpandedResults":true},"userInfo":{"userId":null},"spellCorrectionSpec":{"mode":"AUTO"},"filter":"attributes.status:ANY(\\"active\\") AND (attributes.mart_availability:ANY(\\"JIO\\", \\"JIO_WA\\")) AND (attributes.available_regions:ANY(\\"PANINDIABOOKS\\", \\"PANINDIACRAFT\\", \\"PANINDIADIGITAL\\", \\"PANINDIAFASHION\\", \\"PANINDIAFURNITURE\\", \\"PANINDIAGROCERIES\\", \\"PANINDIAHOMEANDKITCHEN\\", \\"PANINDIAHOMEIMPROVEMENT\\", \\"PANINDIASTL\\")) AND (attributes.inv_stores_1p:ANY(\\"ALL\\", \\"SANR\\", \\"SANS\\", \\"SURR\\", \\"SANQ\\", \\"S4LI\\", \\"S535\\", \\"SXJJ\\", \\"R741\\", \\"R300\\", \\"SAFY\\", \\"SLI1\\", \\"S0XN\\", \\"SZBL\\", \\"Y524\\", \\"SJ14\\", \\"V012\\", \\"SL9F\\", \\"R975\\", \\"S402\\", \\"V017\\", \\"SL7L\\", \\"SB41\\", \\"SLTP\\", \\"SL7Q\\", \\"SG84\\", \\"SL7O\\", \\"SH09\\", \\"V027\\", \\"S352\\") OR attributes.inv_stores_3p:ANY(\\"ALL\\", \\"groceries_zone_non-essential_services\\", \\"general_zone\\", \\"groceries_zone_essential_services\\", \\"fashion_zone\\", \\"electronics_zone\\")) AND ( NOT attributes.vertical_code:ANY(\\"ALCOHOL\\"))","canonicalFilter":"attributes.status:ANY(\\"active\\") AND (attributes.mart_availability:ANY(\\"JIO\\", \\"JIO_WA\\")) AND (attributes.available_regions:ANY(\\"PANINDIABOOKS\\", \\"PANINDIACRAFT\\", \\"PANINDIADIGITAL\\", \\"PANINDIAFASHION\\", \\"PANINDIAFURNITURE\\", \\"PANINDIAGROCERIES\\", \\"PANINDIAHOMEANDKITCHEN\\", \\"PANINDIAHOMEIMPROVEMENT\\", \\"PANINDIASTL\\")) AND (attributes.inv_stores_1p:ANY(\\"ALL\\", \\"SANR\\", \\"SANS\\", \\"SURR\\", \\"SANQ\\", \\"S4LI\\", \\"S535\\", \\"SXJJ\\", \\"R741\\", \\"R300\\", \\"SAFY\\", \\"SLI1\\", \\"S0XN\\", \\"SZBL\\", \\"Y524\\", \\"SJ14\\", \\"V012\\", \\"SL9F\\", \\"R975\\", \\"S402\\", \\"V017\\", \\"SL7L\\", \\"SB41\\", \\"SLTP\\", \\"SL7Q\\", \\"SG84\\", \\"SL7O\\", \\"SH09\\", \\"V027\\", \\"S352\\") OR attributes.inv_stores_3p:ANY(\\"ALL\\", \\"groceries_zone_non-essential_services\\", \\"general_zone\\", \\"groceries_zone_essential_services\\", \\"fashion_zone\\", \\"electronics_zone\\")) AND ( NOT attributes.vertical_code:ANY(\\"ALCOHOL\\"))","visitorId":"anonymous-7a1cce40-4a28-493a-bf64-e770d9650310"}'
#response = requests.post('https://www.jiomart.com/trex/search', cookies=cookies, headers=headers, data=data)

import requests
import time
import copy

session = requests.Session()
session.headers.update(headers)

pincodes = ["110001", "400001", "560001", "380000"]

for pincode in pincodes:
    print(f"\n📍 Fetching pincode: {pincode}")

    session.cookies.clear()
    session.cookies.set("nms_mgo_pincode", pincode)

    next_page_token = None
    page_count = 0

    while True:
        payload = copy.deepcopy(json_data)

        # add pageToken ONLY if it exists
        if next_page_token:
            payload["pageToken"] = next_page_token

        response = session.post(
            "https://www.jiomart.com/trex/search",
            json=payload,
            timeout=30
        )

        if response.status_code != 200:
            print("❌ Request failed")
            break

        data = response.json()

        products = data.get("results") or data.get("products") or []
        print(f"  Page {page_count + 1} → {len(products)} products")

        # 🔑 get next token
        next_page_token = data.get("nextPageToken")

        page_count += 1

        # stop condition
        if not next_page_token:
            print("  ⛔ No more pages")
            break

        time.sleep(1)  # avoid rate limiting
