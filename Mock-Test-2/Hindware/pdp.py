import requests

cookies = {
    '_gcl_au': '1.1.1301499358.1766291927',
    '_ga': 'GA1.1.1419172354.1766291928',
    '_clck': '129z0ac%5E2%5Eg21%5E0%5E2181',
    '__cf_bm': 'Gyf2Pba5O_tIDbUxR8L681q_LeLaDytwkpLZPFj0uBY-1766296636-1.0.1.1-g6QGsVHWGW0kIMXMPQsp_W0PVMkDn9Lw8la48EwTR9b7Dl9lmL8opIQMjJl7zAnaN_DjNG5.Eiv749HYDFs5vaqcjo1QzUHLPMVZzPOYvDM',
    '_ga_LM9T622F68': 'GS2.1.s1766296637$o4$g1$t1766296650$j47$l0$h719453867',
    '_clsk': 's4ehuh%5E1766297513638%5E21%5E1%5Ed.clarity.ms%2Fcollect',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    # 'cookie': '_gcl_au=1.1.1301499358.1766291927; _ga=GA1.1.1419172354.1766291928; _clck=129z0ac%5E2%5Eg21%5E0%5E2181; __cf_bm=Gyf2Pba5O_tIDbUxR8L681q_LeLaDytwkpLZPFj0uBY-1766296636-1.0.1.1-g6QGsVHWGW0kIMXMPQsp_W0PVMkDn9Lw8la48EwTR9b7Dl9lmL8opIQMjJl7zAnaN_DjNG5.Eiv749HYDFs5vaqcjo1QzUHLPMVZzPOYvDM; _ga_LM9T622F68=GS2.1.s1766296637$o4$g1$t1766296650$j47$l0$h719453867; _clsk=s4ehuh%5E1766297513638%5E21%5E1%5Ed.clarity.ms%2Fcollect',
}

response = requests.get('https://hindware.com/p/bath/shower-sliding-bar-with-soap-dish-round', cookies=cookies, headers=headers)

if response.status_code == 200:
    print(response.text)
else:
    print(response.status_code)