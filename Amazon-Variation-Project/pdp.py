import requests
import json
import re
import db_config
from lxml import html

cookies = {
    'session-id': '520-9192216-1595360',
    'session-id-time': '2082787201l',
    'i18n-prefs': 'INR',
    'lc-acbin': 'en_IN',
    'ubid-acbin': '520-7701473-1452433',
    'session-token': 'YTEBi3LT2/tURbcGChr79Y7R5/tvN4sMcYzpW4QE3C37QoZRLaVIMAmcxSx5OwLDyQEDbHfazp16Zip25sQClNfO6KBRs7Oqjb2x/Nz5Wl/FBj2lRwsxq5J/rrCUWnFCw7YUaHsyzWRx1LMyyotgM4uSdfz9F+E/UyTbGbVZS02/nzB+tfTmk/DRt8j8yW18vuxl61+V2ess+w8N73hW/7FVb3AQEU4Q7MmZRUdZgRwTjXc2g5XOxVkxfVGXQTPv2EoqftVgsXMSxy9k0Jh4x0iZJVle2+hKEoI/pifGpQaVjuzdzQcGyqB92omZNURcAEW/iNLJJFVmIXXaoswHMS2qvBgacctC',
    'rxc': 'AMJz47ds1GmjkREx1Xs',
    'csm-hit': 'tb:64CACAA2A726G82SNJTJ+sa-S8E4HXHJJ98Q02FFDD1F-X56W86Q12SAT5HFN8NV1|1766030270357&t:1766030270357&adb:adblk_no',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'device-memory': '8',
    'downlink': '2.1',
    'dpr': '1',
    'ect': '4g',
    'priority': 'u=0, i',
    'rtt': '100',
    'sec-ch-device-memory': '8',
    'sec-ch-dpr': '1',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"19.0.0"',
    'sec-ch-viewport-width': '1236',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'viewport-width': '1236',
    # 'cookie': 'session-id=520-9192216-1595360; session-id-time=2082787201l; i18n-prefs=INR; lc-acbin=en_IN; ubid-acbin=520-7701473-1452433; session-token=YTEBi3LT2/tURbcGChr79Y7R5/tvN4sMcYzpW4QE3C37QoZRLaVIMAmcxSx5OwLDyQEDbHfazp16Zip25sQClNfO6KBRs7Oqjb2x/Nz5Wl/FBj2lRwsxq5J/rrCUWnFCw7YUaHsyzWRx1LMyyotgM4uSdfz9F+E/UyTbGbVZS02/nzB+tfTmk/DRt8j8yW18vuxl61+V2ess+w8N73hW/7FVb3AQEU4Q7MmZRUdZgRwTjXc2g5XOxVkxfVGXQTPv2EoqftVgsXMSxy9k0Jh4x0iZJVle2+hKEoI/pifGpQaVjuzdzQcGyqB92omZNURcAEW/iNLJJFVmIXXaoswHMS2qvBgacctC; rxc=AMJz47ds1GmjkREx1Xs; csm-hit=tb:64CACAA2A726G82SNJTJ+sa-S8E4HXHJJ98Q02FFDD1F-X56W86Q12SAT5HFN8NV1|1766030270357&t:1766030270357&adb:adblk_no',
}

params = {
    'th': '1',
    'psc': '1',
}

# response = requests.get('https://www.amazon.in/dp/B0D1G4T12G', params=params, cookies=cookies, headers=headers)

data = db_config.pl.find({'status':'pending'})

for item in data:
    url = f"https://www.amazon.in{item['pdp_link']}"
    if "/dp" not in url:
        continue

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(response.status_code)
        continue

    content = response.text
    tree = html.fromstring(content)

    p_name = tree.xpath('//span[@id="productTitle"]/text()')[0].strip() or " "

    asin = {}

    scripts = tree.xpath(
        '//script[contains(text(),"dimensionValuesDisplayData")]/text()'
    )

    if not scripts:
        asin = {}
    else:
        script_text = scripts[0]

        match = re.search(
            r'"dimensionValuesDisplayData"\s*:\s*(\{.*?\})\s*,\s*"pwASINs"',
            script_text,
            re.DOTALL
        )

        if match:
            asin = json.loads(match.group(1))

    for key, value in asin.items():
        url1 = f"https://www.amazon.in/dp/{key}"

        response1 = requests.get(url1, headers=headers, params=params)
        if response1.status_code != 200:
            print(response1.status_code)
            continue

        tree1 = html.fromstring(response1.text)

        cost = (tree1.xpath('//div[@class="a-section a-spacing-none aok-align-center aok-relative"]//span[@class="a-price-whole"]/text()') or [" "])[0].strip()
        color = (tree1.xpath('//span[contains(text(),"Colour:")]/following-sibling::span/text()') or [" "])[0].strip()
        size = (tree1.xpath('//span[contains(text(),"Size:")]/following-sibling::span/text()') or [" "])[0].strip()

        data1 = {
            'url': url1,
            'Name': p_name,
            'cost': cost,
            'color': color,
            'size': size,
        }

        try:
            db_config.pdp.update_one({'url': url1}, {'$set': data1}, upsert=True)
            print("inserted")
        except Exception as e:
            print(e)

    try:
        db_config.pl.update_one({'_id':item['_id']}, {'$set':{'status':'Done'} })
    except Exception as e:
        print(e)
