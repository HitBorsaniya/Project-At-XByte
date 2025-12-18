import os.path
import hashlib
from http.client import responses
from lxml import html
import requests
import os
import db_config

def pl_logic():

    folder = r"E:\XByte\Amazon-Variation-Project\pl-pagesave"
    if os.path.exists(folder):
        print("Folder exists")
    else:
        os.mkdir(folder)
        print("Folder created")

    cookies = {
        'session-id': '520-9192216-1595360',
        'session-id-time': '2082787201l',
        'i18n-prefs': 'INR',
        'lc-acbin': 'en_IN',
        'ubid-acbin': '520-7701473-1452433',
        'csm-hit': 'tb:s-W28301BGB14T94CPPZ1E|1766026652913&t:1766026654251&adb:adblk_no',
        'session-token': 'XzFv3cdenoFooEnlKn5roFowrQJJjyj7n1jetQFlrXN8IJbjHE8CxBfnMXsp6ZkKaSOrVDVrcMlKLnBkD0O+feeFQilk/U2gfTjG+DXqKkSiGjaUczdjnNTKnfIpISD4LwlwFgi6/KiaCXfea2uSjAqVVL43LJYlMfOmen63oK3iRzDF1UOF/9sLhWyAxjKtfxMUJoGSyutB0Z6+XX5jIIWtwF4MZ6bVod9LsYWr+uhipH8a4L3jX1PrP7e0f9i6yNUgd6m1uzguvtIsHEhmpCxhMPWNuu5ncilCirKYBHpDRpSuymN8JE6PyoR+RFpTCM/k1TmGilC26VWlcl6LESle95gnWszQ',
        'rxc': 'AMJz47d9wmmjkREx5X4',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'device-memory': '8',
        'downlink': '10',
        'dpr': '1.25',
        'ect': '4g',
        'priority': 'u=0, i',
        'referer': 'https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=8786493352339843000&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9300235&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1',
        'rtt': '100',
        'sec-ch-device-memory': '8',
        'sec-ch-dpr': '1.25',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"19.0.0"',
        'sec-ch-viewport-width': '989',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
        'viewport-width': '989',
        # 'cookie': 'session-id=520-9192216-1595360; session-id-time=2082787201l; i18n-prefs=INR; lc-acbin=en_IN; ubid-acbin=520-7701473-1452433; csm-hit=tb:s-W28301BGB14T94CPPZ1E|1766026652913&t:1766026654251&adb:adblk_no; session-token=XzFv3cdenoFooEnlKn5roFowrQJJjyj7n1jetQFlrXN8IJbjHE8CxBfnMXsp6ZkKaSOrVDVrcMlKLnBkD0O+feeFQilk/U2gfTjG+DXqKkSiGjaUczdjnNTKnfIpISD4LwlwFgi6/KiaCXfea2uSjAqVVL43LJYlMfOmen63oK3iRzDF1UOF/9sLhWyAxjKtfxMUJoGSyutB0Z6+XX5jIIWtwF4MZ6bVod9LsYWr+uhipH8a4L3jX1PrP7e0f9i6yNUgd6m1uzguvtIsHEhmpCxhMPWNuu5ncilCirKYBHpDRpSuymN8JE6PyoR+RFpTCM/k1TmGilC26VWlcl6LESle95gnWszQ; rxc=AMJz47d9wmmjkREx5X4',
    }

    params = {
        'k': 'shirt',
        'crid': '39INON120KAG7',
        'sprefix': 'shirt,aps,306',
        'ref': 'nb_sb_noss_2',
    }

    n=1
    while True:

        url = f'https://www.amazon.in/s?k=shirt&page={n}&xpid=d3XTS0sD5qTYo&crid=39INON120KAG7&qid=1766026675&sprefix=shirt%2Caps%2C306&ref=sr_pg_{n}'
        # response = requests.get('https://www.amazon.in/s', params=params, cookies=cookies, headers=headers)
        enco = url.encode('utf-8')
        hashcode = str(int(hashlib.md5(enco).hexdigest(), 16)%(10**10))
        path_ = f"pl-page-save-{hashcode}.html"
        path = os.path.join(folder, path_)

        if os.path.exists(path):
            print("File exists")
            with open(path, "r", encoding='utf-8') as f:
                content = f.read()
        else:
            print("File not exists")
            response = requests.get(url, headers=headers, params=params, cookies=cookies)
            if response.status_code == 200:
                print("Response 200 got")
                with open(path, "w", encoding='utf-8') as f:
                    content = response.text
                    f.write(content)
            else:
                print("Response status code error")
                print(response.status_code)

        tree = html.fromstring(content)
        box = tree.xpath('//div[@class="puis-card-container s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis puis-v1z7yzsvs3lrxw29kft2yw47by6 s-latency-cf-section puis-card-border"]')

        for items in box:

            pdp_link = items.xpath('.//div[@data-cy="title-recipe"]//a[@class="a-link-normal s-line-clamp-2 s-line-clamp-3-for-col-12 s-link-style a-text-normal"]/@href')[0].strip() or " "

            data = {
                'pdp_link': pdp_link,
                'status':'pending',
            }

            insert_data(data)


        next = tree.xpath('//a[text()="Next"]/text()')
        if next:
            n=n+1
            continue
        else:
            print("Execution Over")
            break

def insert_data(data):
    try:
        db_config.pl.insert_one(data)
        print("Data inserted")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    pl_logic()