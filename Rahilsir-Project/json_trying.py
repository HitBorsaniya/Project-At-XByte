import requests

cookies = {
    'JSESSIONID': '617CA8448C4B60D1D6FE03D25EBD4CA9',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://gujarathc-casestatus.nic.in',
    'Referer': 'https://gujarathc-casestatus.nic.in/gujarathc/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'JSESSIONID=617CA8448C4B60D1D6FE03D25EBD4CA9',
}

data = {
    'ccin': 'R#44#7510#2016',
    'servicecode': '1',
    'challengeString': '25kuf',
}

session = requests.Session()
session.headers.update(headers)
session.cookies.update(cookies)
# session.data.update(data)

response = session.post('https://gujarathc-casestatus.nic.in/gujarathc/GetData', cookies=cookies, headers=headers, data=data)

print(response.text)