import requests
import json
from curl_cffi import requests
import db_config

cookies = {
    'fbcity': '11',
    'fre': '0',
    'rd': '1380000',
    'zl': 'en',
    'fbtrack': 'ce23f71ed76c0cc6902fe0d307561a4d',
    'ltv': '11',
    'lty': '11',
    'locus': '%7B%22addressId%22%3A0%2C%22lat%22%3A23.042662%2C%22lng%22%3A72.566729%2C%22cityId%22%3A11%2C%22ltv%22%3A11%2C%22lty%22%3A%22city%22%2C%22fetchFromGoogle%22%3Afalse%2C%22dszId%22%3A3720%2C%22fen%22%3A%22Ahmedabad%22%7D',
    '_gid': 'GA1.2.1977063359.1765851320',
    '_gcl_au': '1.1.96891728.1765851321',
    '_fbp': 'fb.1.1765851321370.962499039137510034',
    'PHPSESSID': '58766ae7ec0466c2356fe403a87e7912',
    'csrf': '1fc7a859273df81f4066e20364aec6c8',
    'ak_bmsc': '53AD0726870FD2997A1811E375148F13~000000000000000000000000000000~YAAQt4wsMbgz/iSbAQAAfLgTKh4u+dpNfVTdkCtRr6EAnX3qBlJ5GqDHbka1XvmNqhOay2Zx8+2dBFqHCz2kJ5pswKZgZeJnJTzpIL6DCYfe3MW014uGf+MEHZ6yIjUpDkHQcEjUClWLJ3H3kNwmCcSKZgnt7Dn9o+WuCIYcmaAbhTjTR87hzoavA1y2QtqgTlwEfdbuok7z20SRY7KNyiko9FgKGhe0aeywYB8kotkrxNwESTgRr5mdTqmY9GrOZbi9AzjXZwj173Cf5n7wTadh+FrulBMi4WXaWw/tO81PeleuXZwL4KTcHSamolhB0g0ZoiLHYk5lAhG7qSUN9sCqVW8HzvyOaPMKP5eTqkFnwuvvPPRSOkHODVNb+RT9OdYF6e9PR1E8aKfuTwVxGonpGaO7Xk1oR/k=',
    '_gat_global': '1',
    '_gat_city': '1',
    '_gat_country': '1',
    '_ga_2XVFHLPTVP': 'GS2.1.s1765937498$o5$g1$t1765937513$j45$l0$h0',
    '_ga': 'GA1.1.2035771545.1765851320',
    '_ga_X6B66E85ZJ': 'GS2.2.s1765937498$o5$g1$t1765937514$j44$l0$h0',
    '_ga_2NKE6R5GNY': 'GS2.2.s1765937498$o5$g1$t1765937514$j44$l0$h0',
    'g_state': '{"i_l":0,"i_ll":1765937514156,"i_b":"NfwOyQwAa6nVnM688/ofVYJYWjGR1XmB+npi6OlVFUo","i_e":{"enable_itp_optimization":0}}',
    'AWSALBTG': 'QfQtsmNhSXrYj/vsyGUn121plSl62X0+WzHveXYvwPoLi8Os2DxLrntZ4ZIRKL0Ap9jssWLeNarLjwWup1FColZvs7wFvHedz42ijI6a8sJLyoxW1E/4xg9M5uFho1qT/fZReSbbgNTffY1Qu/BmPtYRBRO7gpiXaXgOE9oOMbiM',
    'AWSALBTGCORS': 'QfQtsmNhSXrYj/vsyGUn121plSl62X0+WzHveXYvwPoLi8Os2DxLrntZ4ZIRKL0Ap9jssWLeNarLjwWup1FColZvs7wFvHedz42ijI6a8sJLyoxW1E/4xg9M5uFho1qT/fZReSbbgNTffY1Qu/BmPtYRBRO7gpiXaXgOE9oOMbiM',
    '_dd_s': 'rum=0&expire=1765938445885',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.zomato.com',
    'priority': 'u=1, i',
    'referer': 'https://www.zomato.com/ahmedabad/delivery?dishv2_id=10653&category=1',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'x-zomato-csrft': '1fc7a859273df81f4066e20364aec6c8',
    'cookie': 'fbcity=11; fre=0; rd=1380000; zl=en; fbtrack=ce23f71ed76c0cc6902fe0d307561a4d; ltv=11; lty=11; locus=%7B%22addressId%22%3A0%2C%22lat%22%3A23.042662%2C%22lng%22%3A72.566729%2C%22cityId%22%3A11%2C%22ltv%22%3A11%2C%22lty%22%3A%22city%22%2C%22fetchFromGoogle%22%3Afalse%2C%22dszId%22%3A3720%2C%22fen%22%3A%22Ahmedabad%22%7D; _gid=GA1.2.1977063359.1765851320; _gcl_au=1.1.96891728.1765851321; _fbp=fb.1.1765851321370.962499039137510034; PHPSESSID=58766ae7ec0466c2356fe403a87e7912; csrf=1fc7a859273df81f4066e20364aec6c8; ak_bmsc=53AD0726870FD2997A1811E375148F13~000000000000000000000000000000~YAAQt4wsMbgz/iSbAQAAfLgTKh4u+dpNfVTdkCtRr6EAnX3qBlJ5GqDHbka1XvmNqhOay2Zx8+2dBFqHCz2kJ5pswKZgZeJnJTzpIL6DCYfe3MW014uGf+MEHZ6yIjUpDkHQcEjUClWLJ3H3kNwmCcSKZgnt7Dn9o+WuCIYcmaAbhTjTR87hzoavA1y2QtqgTlwEfdbuok7z20SRY7KNyiko9FgKGhe0aeywYB8kotkrxNwESTgRr5mdTqmY9GrOZbi9AzjXZwj173Cf5n7wTadh+FrulBMi4WXaWw/tO81PeleuXZwL4KTcHSamolhB0g0ZoiLHYk5lAhG7qSUN9sCqVW8HzvyOaPMKP5eTqkFnwuvvPPRSOkHODVNb+RT9OdYF6e9PR1E8aKfuTwVxGonpGaO7Xk1oR/k=; _gat_global=1; _gat_city=1; _gat_country=1; _ga_2XVFHLPTVP=GS2.1.s1765937498$o5$g1$t1765937513$j45$l0$h0; _ga=GA1.1.2035771545.1765851320; _ga_X6B66E85ZJ=GS2.2.s1765937498$o5$g1$t1765937514$j44$l0$h0; _ga_2NKE6R5GNY=GS2.2.s1765937498$o5$g1$t1765937514$j44$l0$h0; g_state={"i_l":0,"i_ll":1765937514156,"i_b":"NfwOyQwAa6nVnM688/ofVYJYWjGR1XmB+npi6OlVFUo","i_e":{"enable_itp_optimization":0}}; AWSALBTG=QfQtsmNhSXrYj/vsyGUn121plSl62X0+WzHveXYvwPoLi8Os2DxLrntZ4ZIRKL0Ap9jssWLeNarLjwWup1FColZvs7wFvHedz42ijI6a8sJLyoxW1E/4xg9M5uFho1qT/fZReSbbgNTffY1Qu/BmPtYRBRO7gpiXaXgOE9oOMbiM; AWSALBTGCORS=QfQtsmNhSXrYj/vsyGUn121plSl62X0+WzHveXYvwPoLi8Os2DxLrntZ4ZIRKL0Ap9jssWLeNarLjwWup1FColZvs7wFvHedz42ijI6a8sJLyoxW1E/4xg9M5uFho1qT/fZReSbbgNTffY1Qu/BmPtYRBRO7gpiXaXgOE9oOMbiM; _dd_s=rum=0&expire=1765938445885',
}

json_data = {
    'context': 'delivery',
    'filters': '{"searchMetadata":{"previousSearchParams":"{\\"PreviousSearchId\\":\\"b5b03e17-9ec0-4efe-8fdb-51e081605e7f\\",\\"PreviousSearchFilter\\":[\\"{\\\\\\"category_context\\\\\\":\\\\\\"delivery_home\\\\\\"}\\",\\"\\",\\"{\\\\\\"universal_dish_ids\\\\\\":[\\\\\\"10653\\\\\\"]}\\"]}","postbackParams":"{\\"processed_chain_ids\\":[112239,110246,111847,19343453,20396096,111013,19831401,20326160,110227,18438932,20432865,19467188,20745826,18929435,18882960,21434155,20666137,20370428,21563279,110812,111509,18922638,18821023,19298577],\\"shown_res_count\\":24,\\"search_id\\":\\"b5b03e17-9ec0-4efe-8fdb-51e081605e7f\\"}","totalResults":100,"hasMore":true,"getInactive":true},"dineoutAdsMetaData":{},"appliedFilter":[{"filterType":"category_sheet","filterValue":"delivery_home","isHidden":true,"isApplied":true,"postKey":"{\\"category_context\\":\\"delivery_home\\"}"},{"filterType":"universal_dish_id","filterValue":"10653","isApplied":true,"postKey":"{\\"universal_dish_ids\\":[\\"10653\\"]}"}],"urlParamsForAds":{}}',
    'addressId': 0,
    'entityId': 11,
    'entityType': 'city',
    'locationType': '',
    'isOrderLocation': 1,
    'cityId': 11,
    'latitude': '23.0426620000000000',
    'longitude': '72.5667290000000000',
    'userDefinedLatitude': 23.042662,
    'userDefinedLongitude': 72.566729,
    'entityName': 'Ahmedabad',
    'orderLocationName': 'Ahmedabad',
    'cityName': 'Ahmedabad',
    'countryId': 1,
    'countryName': 'India',
    'displayTitle': 'Ahmedabad',
    'o2Serviceable': True,
    'placeId': '3720',
    'cellId': '4133887237286789120',
    'deliverySubzoneId': 3720,
    'placeType': 'DSZ',
    'placeName': 'Ahmedabad',
    'isO2City': True,
    'fetchFromGoogle': False,
    'fetchedFromCookie': True,
    'isO2OnlyCity': False,
    'address_template': [],
    'otherRestaurantsUrl': '',
}

API_URL = r'https://www.zomato.com/webroutes/search/home'
# response = requests.post('https://www.zomato.com/webroutes/search/home', cookies=cookies, headers=headers,json=json_data)

#  Note: json_data will not be serialized by requests
#  exactly as it was in the original request.
# data = '{"context":"delivery","filters":"{\\"searchMetadata\\":{\\"previousSearchParams\\":\\"{\\\\\\"PreviousSearchId\\\\\\":\\\\\\"b5b03e17-9ec0-4efe-8fdb-51e081605e7f\\\\\\",\\\\\\"PreviousSearchFilter\\\\\\":[\\\\\\"{\\\\\\\\\\\\\\"category_context\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"delivery_home\\\\\\\\\\\\\\"}\\\\\\",\\\\\\"\\\\\\",\\\\\\"{\\\\\\\\\\\\\\"universal_dish_ids\\\\\\\\\\\\\\":[\\\\\\\\\\\\\\"10653\\\\\\\\\\\\\\"]}\\\\\\"]}\\",\\"postbackParams\\":\\"{\\\\\\"processed_chain_ids\\\\\\":[112239,110246,111847,19343453,20396096,111013,19831401,20326160,110227,18438932,20432865,19467188,20745826,18929435,18882960,21434155,20666137,20370428,21563279,110812,111509,18922638,18821023,19298577],\\\\\\"shown_res_count\\\\\\":24,\\\\\\"search_id\\\\\\":\\\\\\"b5b03e17-9ec0-4efe-8fdb-51e081605e7f\\\\\\"}\\",\\"totalResults\\":100,\\"hasMore\\":true,\\"getInactive\\":true},\\"dineoutAdsMetaData\\":{},\\"appliedFilter\\":[{\\"filterType\\":\\"category_sheet\\",\\"filterValue\\":\\"delivery_home\\",\\"isHidden\\":true,\\"isApplied\\":true,\\"postKey\\":\\"{\\\\\\"category_context\\\\\\":\\\\\\"delivery_home\\\\\\"}\\"},{\\"filterType\\":\\"universal_dish_id\\",\\"filterValue\\":\\"10653\\",\\"isApplied\\":true,\\"postKey\\":\\"{\\\\\\"universal_dish_ids\\\\\\":[\\\\\\"10653\\\\\\"]}\\"}],\\"urlParamsForAds\\":{}}","addressId":0,"entityId":11,"entityType":"city","locationType":"","isOrderLocation":1,"cityId":11,"latitude":"23.0426620000000000","longitude":"72.5667290000000000","userDefinedLatitude":23.042662,"userDefinedLongitude":72.566729,"entityName":"Ahmedabad","orderLocationName":"Ahmedabad","cityName":"Ahmedabad","countryId":1,"countryName":"India","displayTitle":"Ahmedabad","o2Serviceable":true,"placeId":"3720","cellId":"4133887237286789120","deliverySubzoneId":3720,"placeType":"DSZ","placeName":"Ahmedabad","isO2City":true,"fetchFromGoogle":false,"fetchedFromCookie":true,"isO2OnlyCity":false,"address_template":[],"otherRestaurantsUrl":""}'
# response = requests.post('https://www.zomato.com/webroutes/search/home', cookies=cookies, headers=headers, data=data)

count = 0
page_num = 1
has_more = True

session = requests.Session(impersonate="chrome120", timeout=30, verify=False)

while has_more:
    response = session.post(API_URL, headers=headers, cookies=cookies, json=json_data)
    if response.status_code != 200:
        print(f"Failed at page {page_num}, status code: {response.status_code}")
        break
    data_json = response.json()
    sections = data_json.get("sections", {})
    items = sections.get("SECTION_SEARCH_RESULT", [])
    if not items:
        break
    for item in items:
        info = item.get("info", {})
        cuisine_list = info.get("cuisine", [])
        cuisines = ", ".join([c.get("name", "") for c in cuisine_list if isinstance(c, dict)]) if isinstance(
            cuisine_list, list) else ""
        rating = info.get("rating", {}).get("aggregate_rating", "0") if isinstance(info.get("rating"), dict) else "0"
        votes = info.get("rating", {}).get("votes", "0") if isinstance(info.get("rating"), dict) else "0"
        cost = info.get("cft", {}).get("text", "") if isinstance(info.get("cft"), dict) else ""
        delivery_time = item.get("order", {}).get("deliveryTime", "") if isinstance(item.get("order"), dict) else ""
        offers = ", ".join([o.get("text", "") for o in item.get("bulkOffers", []) if isinstance(o, dict)]) if item.get(
            "bulkOffers") else ""
        distance = item.get("distance", "")
        # sections.SECTION_SEARCH_RESULT[0].order.actionInfo
        order_url = "https://www.zomato.com" + item.get("order", {}).get("actionInfo", {}).get("clickUrl","").replace("/order","") or  ""
        restaurant_data = {"Restaurant Name": info.get("name", ""),
                           "Res_id": info.get("resId", ""),
                           "Cuisines": cuisines,
                           "Rating": rating,
                           "Reviews": votes,
                           "Cost for Two": cost,
                           "Delivery Time": delivery_time,
                           "Offers": offers,
                           "Distance": distance,
                           "Order URL": order_url,
                           "status": "pending"
                           }

        try:
            db_config.pl.update_one({'Restaurant Name':info.get("name", "")},{'$set':restaurant_data}, upsert=True)
            print(f"Insert restaurant data for {restaurant_data}")
        except Exception as e:
            print(e)
        # print(restaurant_data)

    meta = sections.get('SECTION_SEARCH_META_INFO', {}).get('searchMetaData', {})
    has_more = meta.get('hasMore', False)
    postback = meta.get('postbackParams', '{}')
    postback_data = json.loads(postback) if postback else {}
    processed_ids = postback_data.get("processed_chain_ids", [])
    if has_more:
        filters_dict = json.loads(json_data['filters'])
        postback_dict = json.loads(filters_dict['searchMetadata']['postbackParams'])
        postback_dict['processed_chain_ids'] = processed_ids
        postback_dict['shown_res_count'] = len(processed_ids)
        filters_dict['searchMetadata']['postbackParams'] = json.dumps(postback_dict)
        json_data['filters'] = json.dumps(filters_dict)
        page_num += 1
