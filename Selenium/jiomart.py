import requests

cookies = {
    '_fbp': 'fb.1.1767364027652.1536523600',
    'WZRK_G': '80e6129121bb49e5bf5f938120ab3dc0',
    '_gcl_au': '1.1.1211049607.1767364029',
    '_ga': 'GA1.1.1353623878.1767364029',
    'nms_mgo_pincode': '382418',
    'nms_mgo_city': 'Ahmedabad',
    'nms_mgo_state_code': 'GJ',
    'AKA_A2': 'A',
    '__tr_jr': 'W3sidXRtcyI6Im9yZ2FuaWMiLCJ0cyI6IjIwMjYtMDEtMDNUMDM6NDY6NDEuMzIxWiIsImVuYyI6InllcyJ9XQ==',
    '_gcl_gs': '2.1.k1$i1767411998$u220930947',
    'RT': '"z=1&dm=www.jiomart.com&si=3c60f3dc-fc74-4e39-8698-eb31c3eb19cf&ss=mjxrgxto&sl=2&tt=2jh&obo=1&rl=1"',
    '__tr_luptv': '1767412032955',
    '_gcl_aw': 'GCL.1767412033.Cj0KCQiA9t3KBhCQARIsAJOcR7wqa53wxLvXn9z2W_xLxur6lzKQkb061UxURoPYFS1Y3Zcp5tw7ONoaAtsEEALw_wcB',
    '_ga_XHR9Q2M3VV': 'GS2.1.s1767412002$o2$g1$t1767412033$j29$l0$h1458896991',
    'WZRK_S_88R-W4Z-495Z': '%7B%22p%22%3A3%2C%22s%22%3A1767411985%2C%22t%22%3A1767412033%7D',
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
    # 'cookie': '_fbp=fb.1.1767364027652.1536523600; WZRK_G=80e6129121bb49e5bf5f938120ab3dc0; _gcl_au=1.1.1211049607.1767364029; _ga=GA1.1.1353623878.1767364029; nms_mgo_pincode=382418; nms_mgo_city=Ahmedabad; nms_mgo_state_code=GJ; AKA_A2=A; __tr_jr=W3sidXRtcyI6Im9yZ2FuaWMiLCJ0cyI6IjIwMjYtMDEtMDNUMDM6NDY6NDEuMzIxWiIsImVuYyI6InllcyJ9XQ==; _gcl_gs=2.1.k1$i1767411998$u220930947; RT="z=1&dm=www.jiomart.com&si=3c60f3dc-fc74-4e39-8698-eb31c3eb19cf&ss=mjxrgxto&sl=2&tt=2jh&obo=1&rl=1"; __tr_luptv=1767412032955; _gcl_aw=GCL.1767412033.Cj0KCQiA9t3KBhCQARIsAJOcR7wqa53wxLvXn9z2W_xLxur6lzKQkb061UxURoPYFS1Y3Zcp5tw7ONoaAtsEEALw_wcB; _ga_XHR9Q2M3VV=GS2.1.s1767412002$o2$g1$t1767412033$j29$l0$h1458896991; WZRK_S_88R-W4Z-495Z=%7B%22p%22%3A3%2C%22s%22%3A1767411985%2C%22t%22%3A1767412033%7D',
}

json_data = {
    'query': 'atta',
    'pageSize': 500,
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
    'filter': 'attributes.status:ANY("active") AND (attributes.mart_availability:ANY("JIO", "JIO_WA")) AND (attributes.available_regions:ANY("PANINDIABOOKS", "PANINDIACRAFT", "PANINDIADIGITAL", "PANINDIAFASHION", "PANINDIAFURNITURE", "6202", "PANINDIAGROCERIES", "PANINDIAHOMEANDKITCHEN", "PANINDIAHOMEIMPROVEMENT", "PANINDIAJEWEL", "PANINDIASTL", "PANINDIAWELLNESS")) AND (attributes.inv_stores_1p:ANY("ALL", "T19P", "SANR", "SANS", "SURR", "SANQ", "S4LI", "S535", "TWQS", "R300", "SLI1", "S2CP", "TG1K", "S2CN", "S2CO", "SLE4", "S3IR", "T4QF", "S0XN", "SZBL", "Y524", "SJ14", "V012", "R975", "S402", "TAQE", "V017", "S2DT", "SB41", "SLTP", "SL7Q", "SH09", "V027", "S3KG", "VLOR", "254", "N09", "60", "270", "SF11", "HX0E", "SF40", "SX9A", "R696", "SE40", "S0BN", "R080", "SK1M", "Y344", "SJ93", "TSF7", "R396", "S573", "SLTY", "V014", "SLKO") OR attributes.inv_stores_3p:ANY("ALL", "groceries_zone_non-essential_services", "general_zone", "groceries_zone_essential_services", "fashion_zone", "electronics_zone")) AND ( NOT attributes.vertical_code:ANY("ALCOHOL")) AND (NOT attributes.vertical_code:ANY("GROCERIES") OR NOT attributes.seller_ids:ANY("1"))',
    'canonicalFilter': 'attributes.status:ANY("active") AND (attributes.mart_availability:ANY("JIO", "JIO_WA")) AND (attributes.available_regions:ANY("PANINDIABOOKS", "PANINDIACRAFT", "PANINDIADIGITAL", "PANINDIAFASHION", "PANINDIAFURNITURE", "6202", "PANINDIAGROCERIES", "PANINDIAHOMEANDKITCHEN", "PANINDIAHOMEIMPROVEMENT", "PANINDIAJEWEL", "PANINDIASTL", "PANINDIAWELLNESS")) AND (attributes.inv_stores_1p:ANY("ALL", "T19P", "SANR", "SANS", "SURR", "SANQ", "S4LI", "S535", "TWQS", "R300", "SLI1", "S2CP", "TG1K", "S2CN", "S2CO", "SLE4", "S3IR", "T4QF", "S0XN", "SZBL", "Y524", "SJ14", "V012", "R975", "S402", "TAQE", "V017", "S2DT", "SB41", "SLTP", "SL7Q", "SH09", "V027", "S3KG", "VLOR", "254", "N09", "60", "270", "SF11", "HX0E", "SF40", "SX9A", "R696", "SE40", "S0BN", "R080", "SK1M", "Y344", "SJ93", "TSF7", "R396", "S573", "SLTY", "V014", "SLKO") OR attributes.inv_stores_3p:ANY("ALL", "groceries_zone_non-essential_services", "general_zone", "groceries_zone_essential_services", "fashion_zone", "electronics_zone")) AND ( NOT attributes.vertical_code:ANY("ALCOHOL")) AND (NOT attributes.vertical_code:ANY("GROCERIES") OR NOT attributes.seller_ids:ANY("1"))',
    'visitorId': 'anonymous-7a1cce40-4a28-493a-bf64-e770d9650310',
}

response = requests.post('https://www.jiomart.com/trex/search', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"query":"milk","pageSize":50,"facetSpecs":[{"facetKey":{"key":"brands"},"limit":500,"excludedFilterKeys":["brands"]},{"facetKey":{"key":"categories"},"limit":500,"excludedFilterKeys":["categories"]},{"facetKey":{"key":"attributes.category_level_4"},"limit":500,"excludedFilterKeys":["attributes.category_level_4"]},{"facetKey":{"key":"attributes.category_level_1"},"excludedFilterKeys":["attributes.category_level_4"]},{"facetKey":{"key":"attributes.avg_selling_price","return_min_max":true,"intervals":[{"minimum":0.1,"maximum":100000000}]}},{"facetKey":{"key":"attributes.avg_discount_pct","return_min_max":true,"intervals":[{"minimum":0,"maximum":99}]}}],"variantRollupKeys":["variantId"],"branch":"projects/sr-project-jiomart-jfront-prod/locations/global/catalogs/default_catalog/branches/0","queryExpansionSpec":{"condition":"AUTO","pinUnexpandedResults":true},"userInfo":{"userId":null},"spellCorrectionSpec":{"mode":"AUTO"},"filter":"attributes.status:ANY(\\"active\\") AND (attributes.mart_availability:ANY(\\"JIO\\", \\"JIO_WA\\")) AND (attributes.available_regions:ANY(\\"PANINDIABOOKS\\", \\"PANINDIACRAFT\\", \\"PANINDIADIGITAL\\", \\"PANINDIAFASHION\\", \\"PANINDIAFURNITURE\\", \\"6202\\", \\"PANINDIAGROCERIES\\", \\"PANINDIAHOMEANDKITCHEN\\", \\"PANINDIAHOMEIMPROVEMENT\\", \\"PANINDIAJEWEL\\", \\"PANINDIASTL\\", \\"PANINDIAWELLNESS\\")) AND (attributes.inv_stores_1p:ANY(\\"ALL\\", \\"T19P\\", \\"SANR\\", \\"SANS\\", \\"SURR\\", \\"SANQ\\", \\"S4LI\\", \\"S535\\", \\"TWQS\\", \\"R300\\", \\"SLI1\\", \\"S2CP\\", \\"TG1K\\", \\"S2CN\\", \\"S2CO\\", \\"SLE4\\", \\"S3IR\\", \\"T4QF\\", \\"S0XN\\", \\"SZBL\\", \\"Y524\\", \\"SJ14\\", \\"V012\\", \\"R975\\", \\"S402\\", \\"TAQE\\", \\"V017\\", \\"S2DT\\", \\"SB41\\", \\"SLTP\\", \\"SL7Q\\", \\"SH09\\", \\"V027\\", \\"S3KG\\", \\"VLOR\\", \\"254\\", \\"N09\\", \\"60\\", \\"270\\", \\"SF11\\", \\"HX0E\\", \\"SF40\\", \\"SX9A\\", \\"R696\\", \\"SE40\\", \\"S0BN\\", \\"R080\\", \\"SK1M\\", \\"Y344\\", \\"SJ93\\", \\"TSF7\\", \\"R396\\", \\"S573\\", \\"SLTY\\", \\"V014\\", \\"SLKO\\") OR attributes.inv_stores_3p:ANY(\\"ALL\\", \\"groceries_zone_non-essential_services\\", \\"general_zone\\", \\"groceries_zone_essential_services\\", \\"fashion_zone\\", \\"electronics_zone\\")) AND ( NOT attributes.vertical_code:ANY(\\"ALCOHOL\\")) AND (NOT attributes.vertical_code:ANY(\\"GROCERIES\\") OR NOT attributes.seller_ids:ANY(\\"1\\"))","canonicalFilter":"attributes.status:ANY(\\"active\\") AND (attributes.mart_availability:ANY(\\"JIO\\", \\"JIO_WA\\")) AND (attributes.available_regions:ANY(\\"PANINDIABOOKS\\", \\"PANINDIACRAFT\\", \\"PANINDIADIGITAL\\", \\"PANINDIAFASHION\\", \\"PANINDIAFURNITURE\\", \\"6202\\", \\"PANINDIAGROCERIES\\", \\"PANINDIAHOMEANDKITCHEN\\", \\"PANINDIAHOMEIMPROVEMENT\\", \\"PANINDIAJEWEL\\", \\"PANINDIASTL\\", \\"PANINDIAWELLNESS\\")) AND (attributes.inv_stores_1p:ANY(\\"ALL\\", \\"T19P\\", \\"SANR\\", \\"SANS\\", \\"SURR\\", \\"SANQ\\", \\"S4LI\\", \\"S535\\", \\"TWQS\\", \\"R300\\", \\"SLI1\\", \\"S2CP\\", \\"TG1K\\", \\"S2CN\\", \\"S2CO\\", \\"SLE4\\", \\"S3IR\\", \\"T4QF\\", \\"S0XN\\", \\"SZBL\\", \\"Y524\\", \\"SJ14\\", \\"V012\\", \\"R975\\", \\"S402\\", \\"TAQE\\", \\"V017\\", \\"S2DT\\", \\"SB41\\", \\"SLTP\\", \\"SL7Q\\", \\"SH09\\", \\"V027\\", \\"S3KG\\", \\"VLOR\\", \\"254\\", \\"N09\\", \\"60\\", \\"270\\", \\"SF11\\", \\"HX0E\\", \\"SF40\\", \\"SX9A\\", \\"R696\\", \\"SE40\\", \\"S0BN\\", \\"R080\\", \\"SK1M\\", \\"Y344\\", \\"SJ93\\", \\"TSF7\\", \\"R396\\", \\"S573\\", \\"SLTY\\", \\"V014\\", \\"SLKO\\") OR attributes.inv_stores_3p:ANY(\\"ALL\\", \\"groceries_zone_non-essential_services\\", \\"general_zone\\", \\"groceries_zone_essential_services\\", \\"fashion_zone\\", \\"electronics_zone\\")) AND ( NOT attributes.vertical_code:ANY(\\"ALCOHOL\\")) AND (NOT attributes.vertical_code:ANY(\\"GROCERIES\\") OR NOT attributes.seller_ids:ANY(\\"1\\"))","visitorId":"anonymous-7a1cce40-4a28-493a-bf64-e770d9650310"}'
#response = requests.post('https://www.jiomart.com/trex/search', cookies=cookies, headers=headers, data=data)

# print(response.text)


import requests
import time

URL = "https://www.jiomart.com/trex/search"

all_products = []
next_page_token = None

while True:
    # inject pageToken only if it exists
    if next_page_token:
        json_data["pageToken"] = next_page_token
    else:
        json_data.pop("pageToken", None)

    response = requests.post(
        URL,
        headers=headers,
        cookies=cookies,
        json=json_data,
        timeout=30
    )

    response.raise_for_status()
    data = response.json()
    products = data.get("results", [])
    if not products:
        print("No more products.")
        break

    all_products.extend(products)
    print(20*"-")
    print(f"Fetched {len(products)} | Total: {len(all_products)}")
    print(20 * "-")

    for i in products:
        print(i.get("product",{}).get("title"))
    # get cursor for next page

    next_page_token = data.get("nextPageToken")
    print(f"Next Page Token: {next_page_token}")

    if not next_page_token:
        print("No nextPageToken found. Finished.")
        break

    time.sleep(0.5)  # prevent rate limiting

print("TOTAL PRODUCTS FETCHED:", len(all_products))



# import requests
#
# all_products = []
# page = 0
# page_size = 500
#
# while True:
#     json_data["pageNumber"] = page
#     json_data["pageSize"] = page_size
#
#     response = requests.post(
#         "https://www.jiomart.com/trex/search",
#         headers=headers,
#         cookies=cookies,
#         json=json_data,
#         timeout=30
#     )
#
#     data = response.json()
#
#     products = data.get("results", [])
#     if not products:
#         break
#
#     all_products.extend(products)
#     print(f"Fetched page {page}, total so far: {len(all_products)}")
#
#     # stop if last page
#     if len(products) < page_size:
#         break
#
#     page += 1
#
# print("TOTAL PRODUCTS:", len(all_products))
