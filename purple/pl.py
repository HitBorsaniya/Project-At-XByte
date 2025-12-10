import requests
import json

cookies = {
    'environment': 'prod',
    'is_robot': 'false',
    'mode_device': 'desktop',
    'is_webview': 'false',
    'lang_code': 'undefined',
    'vernac_ab_flag': 'undefined',
    'client_ip': '152.58.34.247',
    'visitorppl': 'gc5Xe0iB2eMOAsoGh1',
    'device_id': 'gc5Xe0iB2eMOAsoGh1',
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VfaWQiOiJnYzVYZTBpQjJlTU9Bc29HaDEiLCJtb2RlX2RldmljZSI6ImRlc2t0b3AiLCJtb2RlX2RldmljZV90eXBlIjoid2ViIiwiaWF0IjoxNzY1MzgzMjgyLCJleHAiOjE3NzMxNTkyODIsImF1ZCI6IndlYiIsImlzcyI6InRva2VubWljcm9zZXJ2aWNlIn0.Od9qIBCbDtkN4oC8MC3vF5LQIN04CVXkbytU1kag2G4',
    'generic_visitorppl': 'KIwYcVvc80vWvBeuMJ1270011580205867',
    'generic_token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VfaWQiOiJLSXdZY1Z2Yzgwdld2QmV1TUoxMjcwMDExNTgwMjA1ODY3IiwibW9kZV9kZXZpY2UiOiJkZXNrdG9wIiwibW9kZV9kZXZpY2VfdHlwZSI6IndlYiIsImlhdCI6MTU4NDA4NjYzOCwiZXhwIjoyNjkwNjQ3NTI0LCJhdWQiOiJ3ZWIiLCJpc3MiOiJ0b2tlbm1pY3Jvc2VydmljZSJ9.RdrqkTAPBDh0Qe-605a_dOYoXOOPcJe33f6tuMioKi8',
    'session_initiated': 'google',
    'referrer': 'www.google.com',
    'utm_medium': 'organic',
    'utm_campaign': 'google-organic',
    'session_initiator': 'google',
    'GCLB': 'COP5leL5nZOLqwEQAw',
    'sessionCreatedTime': '1765383303',
    '__sessionstorage__downloadStrip': 'true',
    '__storage__modeDevice': 'desktop',
    '__storage__isRobot': 'false',
    '__storage__nc': '{"cc":0}',
    'isSessionDetails': 'true',
    '__storage__supermenuExpiry': '1765383602188',
    '__storage__giftBox': '{"itemCount":0}',
    '__sessionstorage__giftBoxIcon': '0',
    '__storage__screen_ab_testing': '{"listing_ab_testing":[{"value":"j","types":"search,brand,category,landingpages,collections","key":"ab_experiment_listing"}]}',
    '__storage__isEliteUser': 'false',
    '__storage__isLoggedIn': 'false',
    '_gcl_au': '1.1.1057335648.1765383306',
    '_ga': 'GA1.2.145716883.1765383308',
    '_gid': 'GA1.2.338573905.1765383313',
    '__storage__fcm_time_stamp': '1765380600000',
    'utm_source': 'google',
    'is_first_session': 'false',
    '__sessionstorage__PREV_PAGE_FROM_SESSION': '{"page_url":"https://www.purplle.com/skincare/lip-care","page_type":"listing_category","page_type_value":"11"}',
    '_ga_FWGKK004RG': 'GS2.1.s1765383308$o1$g1$t1765383451$j60$l0$h0',
    'sessionExpiryTime': '1765385252',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'is_ssr': 'false',
    'mode_device': 'desktop',
    'ngsw-bypass': 'true',
    'priority': 'u=1, i',
    'referer': 'https://www.purplle.com/skincare/lip-care',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VfaWQiOiJnYzVYZTBpQjJlTU9Bc29HaDEiLCJtb2RlX2RldmljZSI6ImRlc2t0b3AiLCJtb2RlX2RldmljZV90eXBlIjoid2ViIiwiaWF0IjoxNzY1MzgzMjgyLCJleHAiOjE3NzMxNTkyODIsImF1ZCI6IndlYiIsImlzcyI6InRva2VubWljcm9zZXJ2aWNlIn0.Od9qIBCbDtkN4oC8MC3vF5LQIN04CVXkbytU1kag2G4',
    'type': 'desktop',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'visitorppl': 'gc5Xe0iB2eMOAsoGh1',
}

# ---------------- YOUR ORIGINAL REQUEST ----------------
page = 1   # <-- ADDED (keeps pagination working)

while True:

    # <-- ADDED dynamic URL
    response = requests.get(
        f'https://www.purplle.com/neo/merch/items/v2?tenant=PURPLLE_COM&sub_tenant=MAIN_SITE&userType=0&list_type=category&list_type_value=skincare/lip-care&page={page}&sort_by=rel&elite=0&mode_device=desktop&ab_experiment_listing=a&identifier=gc5Xe0iB2eMOAsoGh1',
        cookies=cookies,
        headers=headers,
    )

    tree = json.loads(response.text)

    box = tree['items']
    for item in box:
        name = item['name']
        type = item['type']
        thumb_image_url = item['thumb_image_url']

        data = {
            'name': name,
            'type': type,
            'thumb_image_url': thumb_image_url,
        }

        print(data)

    next = tree['has_more']
    if next:
        page += 1   # <-- ADDED (go to next page)
        continue
    else:
        break
