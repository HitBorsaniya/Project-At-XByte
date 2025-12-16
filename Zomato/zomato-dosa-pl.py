import json

import requests

cookies = {
    'PHPSESSID': 'f7e78b1786d79b75173181633a5d8dac',
    'csrf': 'd9a1e2939e03d2c425adfec5206a45f9',
    'fbcity': '11',
    'fre': '0',
    'rd': '1380000',
    'zl': 'en',
    'fbtrack': 'ce23f71ed76c0cc6902fe0d307561a4d',
    'ltv': '11',
    'lty': '11',
    'locus': '%7B%22addressId%22%3A0%2C%22lat%22%3A23.042662%2C%22lng%22%3A72.566729%2C%22cityId%22%3A11%2C%22ltv%22%3A11%2C%22lty%22%3A%22city%22%2C%22fetchFromGoogle%22%3Afalse%2C%22dszId%22%3A3720%2C%22fen%22%3A%22Ahmedabad%22%7D',
    'ak_bmsc': '22CA15629ED70542E2E80FF1AA957784~000000000000000000000000000000~YAAQ5owsMU+UnwmbAQAAP8jwJB5wP2xLpvIe4A0nssNEY68qIPnWGcu4HrGD5ONvuajy5n6v4AKh8nrzK4lGUuyleVCz3IQJ8QnrT0JhBDP/QcgL8rhOLywQzKTpGiPhkvsKhXfQHLVtwEeXy/fMdvYAnQl8CKem+fwRcOn77Qyt+9qhZH75K1s+j8Un9i8SGHZzcJNN01IkWYoE3z0sjAdVh0+AHikIlE4wqZ3cmOEDzFC8LwcvCLJQ5nAN/B+DS77VLfdD2R6abWzyhQkh2EM9VFdd7J/50MKQSs5bMpCqcVDi+i7lLljpjR0IVrNxqBs3TC1osNU1191uv/Spk/ug2JJ3HWFd3gavsGuHp+YBLBV6VIJ62SQwX25LHl/83NTamSCpJOKD2DHi0K7P/SVxadH5jDFgvbtly3z0E6K+/Q==',
    '_gid': 'GA1.2.1977063359.1765851320',
    '_gcl_au': '1.1.96891728.1765851321',
    '_fbp': 'fb.1.1765851321370.962499039137510034',
    '_ga_2NKE6R5GNY': 'GS2.2.s1765851321$o1$g1$t1765851331$j50$l0$h0',
    '_ga_X6B66E85ZJ': 'GS2.2.s1765851321$o1$g1$t1765851331$j50$l0$h0',
    'g_state': '{"i_l":0,"i_ll":1765851331213,"i_b":"sIJLNmAbwZAT8JgyWFo0EgsnTYaK7bransfqZEQMqig","i_e":{"enable_itp_optimization":0}}',
    '_ga_2XVFHLPTVP': 'GS2.1.s1765851321$o1$g1$t1765851424$j59$l0$h0',
    '_ga': 'GA1.1.2035771545.1765851320',
    '_gat_global': '1',
    '_gat_city': '1',
    '_gat_country': '1',
    '_dd_s': 'rum=0&expire=1765852325433',
    'AWSALBTG': '2+dhSZ5w6Egx6dJjz20oGMvEdeE5ndF7FUIFB/ar4BHn/OlsLU5L+CIe/8k8U42P2KhlQrv5nowqrPv7zqV0qrEuITYJd2HSJ786Q1ddxDpJwmvMt1HiR4TDE5AwgyRjIpv7KNx8EHP2AVxRmwFTrPvfIzypu9vOfM8HDRJPHZyX',
    'AWSALBTGCORS': '2+dhSZ5w6Egx6dJjz20oGMvEdeE5ndF7FUIFB/ar4BHn/OlsLU5L+CIe/8k8U42P2KhlQrv5nowqrPv7zqV0qrEuITYJd2HSJ786Q1ddxDpJwmvMt1HiR4TDE5AwgyRjIpv7KNx8EHP2AVxRmwFTrPvfIzypu9vOfM8HDRJPHZyX',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.zomato.com',
    'priority': 'u=1, i',
    'referer': 'https://www.zomato.com/ahmedabad/delivery/dish-dosa',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'x-zomato-csrft': 'd9a1e2939e03d2c425adfec5206a45f9',
    # 'cookie': 'PHPSESSID=f7e78b1786d79b75173181633a5d8dac; csrf=d9a1e2939e03d2c425adfec5206a45f9; fbcity=11; fre=0; rd=1380000; zl=en; fbtrack=ce23f71ed76c0cc6902fe0d307561a4d; ltv=11; lty=11; locus=%7B%22addressId%22%3A0%2C%22lat%22%3A23.042662%2C%22lng%22%3A72.566729%2C%22cityId%22%3A11%2C%22ltv%22%3A11%2C%22lty%22%3A%22city%22%2C%22fetchFromGoogle%22%3Afalse%2C%22dszId%22%3A3720%2C%22fen%22%3A%22Ahmedabad%22%7D; ak_bmsc=22CA15629ED70542E2E80FF1AA957784~000000000000000000000000000000~YAAQ5owsMU+UnwmbAQAAP8jwJB5wP2xLpvIe4A0nssNEY68qIPnWGcu4HrGD5ONvuajy5n6v4AKh8nrzK4lGUuyleVCz3IQJ8QnrT0JhBDP/QcgL8rhOLywQzKTpGiPhkvsKhXfQHLVtwEeXy/fMdvYAnQl8CKem+fwRcOn77Qyt+9qhZH75K1s+j8Un9i8SGHZzcJNN01IkWYoE3z0sjAdVh0+AHikIlE4wqZ3cmOEDzFC8LwcvCLJQ5nAN/B+DS77VLfdD2R6abWzyhQkh2EM9VFdd7J/50MKQSs5bMpCqcVDi+i7lLljpjR0IVrNxqBs3TC1osNU1191uv/Spk/ug2JJ3HWFd3gavsGuHp+YBLBV6VIJ62SQwX25LHl/83NTamSCpJOKD2DHi0K7P/SVxadH5jDFgvbtly3z0E6K+/Q==; _gid=GA1.2.1977063359.1765851320; _gcl_au=1.1.96891728.1765851321; _fbp=fb.1.1765851321370.962499039137510034; _ga_2NKE6R5GNY=GS2.2.s1765851321$o1$g1$t1765851331$j50$l0$h0; _ga_X6B66E85ZJ=GS2.2.s1765851321$o1$g1$t1765851331$j50$l0$h0; g_state={"i_l":0,"i_ll":1765851331213,"i_b":"sIJLNmAbwZAT8JgyWFo0EgsnTYaK7bransfqZEQMqig","i_e":{"enable_itp_optimization":0}}; _ga_2XVFHLPTVP=GS2.1.s1765851321$o1$g1$t1765851424$j59$l0$h0; _ga=GA1.1.2035771545.1765851320; _gat_global=1; _gat_city=1; _gat_country=1; _dd_s=rum=0&expire=1765852325433; AWSALBTG=2+dhSZ5w6Egx6dJjz20oGMvEdeE5ndF7FUIFB/ar4BHn/OlsLU5L+CIe/8k8U42P2KhlQrv5nowqrPv7zqV0qrEuITYJd2HSJ786Q1ddxDpJwmvMt1HiR4TDE5AwgyRjIpv7KNx8EHP2AVxRmwFTrPvfIzypu9vOfM8HDRJPHZyX; AWSALBTGCORS=2+dhSZ5w6Egx6dJjz20oGMvEdeE5ndF7FUIFB/ar4BHn/OlsLU5L+CIe/8k8U42P2KhlQrv5nowqrPv7zqV0qrEuITYJd2HSJ786Q1ddxDpJwmvMt1HiR4TDE5AwgyRjIpv7KNx8EHP2AVxRmwFTrPvfIzypu9vOfM8HDRJPHZyX',
}



# response = requests.post('https://www.zomato.com/webroutes/search/home', cookies=cookies, headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"context":"delivery","filters":"{\\"searchMetadata\\":{\\"previousSearchParams\\":\\"{\\\\\\"PreviousSearchId\\\\\\":\\\\\\"0c86c715-1486-41a7-b022-2b8ee29b7333\\\\\\",\\\\\\"PreviousSearchFilter\\\\\\":[\\\\\\"{\\\\\\\\\\\\\\"category_context\\\\\\\\\\\\\\":\\\\\\\\\\\\\\"delivery_home\\\\\\\\\\\\\\"}\\\\\\",\\\\\\"\\\\\\",\\\\\\"{\\\\\\\\\\\\\\"universal_dish_ids\\\\\\\\\\\\\\":[\\\\\\\\\\\\\\"10296\\\\\\\\\\\\\\"]}\\\\\\"]}\\",\\"postbackParams\\":\\"{\\\\\\"processed_chain_ids\\\\\\":[21171501,19703510,21097703,21304818,112140,19866286,19876219,21966768,19185677],\\\\\\"shown_res_count\\\\\\":9,\\\\\\"search_id\\\\\\":\\\\\\"0c86c715-1486-41a7-b022-2b8ee29b7333\\\\\\"}\\",\\"totalResults\\":35,\\"hasMore\\":true,\\"getInactive\\":false},\\"dineoutAdsMetaData\\":{},\\"appliedFilter\\":[{\\"filterType\\":\\"category_sheet\\",\\"filterValue\\":\\"delivery_home\\",\\"isHidden\\":true,\\"isApplied\\":true,\\"postKey\\":\\"{\\\\\\"category_context\\\\\\":\\\\\\"delivery_home\\\\\\"}\\"},{\\"filterType\\":\\"universal_dish_id\\",\\"filterValue\\":\\"10296\\",\\"isApplied\\":true,\\"postKey\\":\\"{\\\\\\"universal_dish_ids\\\\\\":[\\\\\\"10296\\\\\\"]}\\"}],\\"urlParamsForAds\\":{}}","addressId":0,"entityId":11,"entityType":"city","locationType":"","isOrderLocation":1,"cityId":11,"latitude":"23.0426620000000000","longitude":"72.5667290000000000","userDefinedLatitude":23.042662,"userDefinedLongitude":72.566729,"entityName":"Ahmedabad","orderLocationName":"Ahmedabad","cityName":"Ahmedabad","countryId":1,"countryName":"India","displayTitle":"Ahmedabad","o2Serviceable":true,"placeId":"3720","cellId":"4133887237286789120","deliverySubzoneId":3720,"placeType":"DSZ","placeName":"Ahmedabad","isO2City":true,"fetchFromGoogle":false,"fetchedFromCookie":true,"isO2OnlyCity":false,"address_template":[],"otherRestaurantsUrl":""}'
#response = requests.post('https://www.zomato.com/webroutes/search/home', cookies=cookies, headers=headers, data=data)

inc = 9
while True:
    json_data = {
        'context': 'delivery',
        'filters': '{"searchMetadata":{"previousSearchParams":"{\\"PreviousSearchId\\":\\"0c86c715-1486-41a7-b022-2b8ee29b7333\\",\\"PreviousSearchFilter\\":[\\"{\\\\\\"category_context\\\\\\":\\\\\\"delivery_home\\\\\\"}\\",\\"\\",\\"{\\\\\\"universal_dish_ids\\\\\\":[\\\\\\"10296\\\\\\"]}\\"]}","postbackParams":"{\\"processed_chain_ids\\":[21171501,19703510,21097703,21304818,112140,19866286,19876219,21966768,19185677],\\"shown_res_count\\":'+str(inc)+',\\"search_id\\":\\"0c86c715-1486-41a7-b022-2b8ee29b7333\\"}","totalResults":35,"hasMore":true,"getInactive":false},"dineoutAdsMetaData":{},"appliedFilter":[{"filterType":"category_sheet","filterValue":"delivery_home","isHidden":true,"isApplied":true,"postKey":"{\\"category_context\\":\\"delivery_home\\"}"},{"filterType":"universal_dish_id","filterValue":"10296","isApplied":true,"postKey":"{\\"universal_dish_ids\\":[\\"10296\\"]}"}],"urlParamsForAds":{}}',
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

    url = 'https://www.zomato.com/webroutes/search/home'

    response = requests.post(url, cookies=cookies, headers=headers, json=json_data)
    if response.status_code == 200:

        tree = json.loads(response.text)
        box = tree['sections']['SECTION_SEARCH_RESULT']

        for item in box:
            name = item['info']['name']
            print(name)

        next = tree['sections']['SECTION_SEARCH_META_INFO']['searchMetaData']['hasMore']
        if next:
            inc = inc + 12
            continue
        else:
            break
    else:
        print(response.status_code)