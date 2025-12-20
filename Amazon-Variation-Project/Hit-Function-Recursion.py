import html

import requests
from lxml import html

cookies = {
    'session-id': '520-9192216-1595360',
    'session-id-time': '2082787201l',
    'i18n-prefs': 'INR',
    'lc-acbin': 'en_IN',
    'ubid-acbin': '520-7701473-1452433',
    'session-token': 'fb/Vtzq1ZrqVp6mVUq7h3x2CdeOtDAsJDAWK06qP8RorP+9ZbO6Mw1L+BsQ0MEmyYcsw5OPiAZ71d9YrRtTC7kMZI5djfjY6MD+XtHBvDbilEhsBt3za4Gm2pMKtYjEkCAUnxRJ+ypW8IQ4qWGJFGGpkTbOiqjxw0PkY9f2Xv5AAFP9fjbH8QGN7ZiGOEWS81AlY3TCqcAqA8HcRRruHr3bGdg7TXsaxXWxlc7ITzF2qLSrybHe9BCUAchDYiq3N26bfp34QMyu6fBcHhxqhBHhIzyWaPrTopVcgviBhmdCoOjRZbUcIaTW+ap4ZJ3t2QMRzqJPyF3MiNCfVjBTSJEIxE+E9+TVj',
    'csm-hit': 'tb:8A7GJK6QM9JZKXFMKVRQ+s-W3NCCZ0Q6T8RH6WJX880|1766161581696&t:1766161581696&adb:adblk_no',
    'rxc': 'AMJz47dj02+jkRExIXw',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'device-memory': '8',
    'downlink': '1.5',
    'dpr': '1',
    'ect': '3g',
    'priority': 'u=0, i',
    'referer': 'https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=16101407250810176040&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9300235&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1',
    'rtt': '750',
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
    # 'cookie': 'session-id=520-9192216-1595360; session-id-time=2082787201l; i18n-prefs=INR; lc-acbin=en_IN; ubid-acbin=520-7701473-1452433; session-token=fb/Vtzq1ZrqVp6mVUq7h3x2CdeOtDAsJDAWK06qP8RorP+9ZbO6Mw1L+BsQ0MEmyYcsw5OPiAZ71d9YrRtTC7kMZI5djfjY6MD+XtHBvDbilEhsBt3za4Gm2pMKtYjEkCAUnxRJ+ypW8IQ4qWGJFGGpkTbOiqjxw0PkY9f2Xv5AAFP9fjbH8QGN7ZiGOEWS81AlY3TCqcAqA8HcRRruHr3bGdg7TXsaxXWxlc7ITzF2qLSrybHe9BCUAchDYiq3N26bfp34QMyu6fBcHhxqhBHhIzyWaPrTopVcgviBhmdCoOjRZbUcIaTW+ap4ZJ3t2QMRzqJPyF3MiNCfVjBTSJEIxE+E9+TVj; csm-hit=tb:8A7GJK6QM9JZKXFMKVRQ+s-W3NCCZ0Q6T8RH6WJX880|1766161581696&t:1766161581696&adb:adblk_no; rxc=AMJz47dj02+jkRExIXw',
}


def fetch_data(n):

    url = f'http://amazon.in/s?k=water+bottles&page={n}&crid=HJE1TY7HJAMZ&qid=1766162451&sprefix=bottole%2Caps%2C539&xpid=xFncbG6Ns9pq-&ref=sr_pg_{n}'
    response = requests.get(url, cookies=cookies, headers=headers)
    if response.status_code != 200:
        print("Error..Status Code ",response.status_code)

    tree = html.fromstring(response.content)
    box = tree.xpath('//div[@class="a-section a-spacing-base desktop-grid-content-view"]')

    for item in box:

        p_name = (item.xpath('.//h2/span/text()') or " ")[0].strip()
        pdp_link = (item.xpath('//div[@data-cy="title-recipe"]/a/@href') or " ")[0].strip()
        pdp_link = f"https://www.amazon.in{pdp_link}"
        price = (item.xpath('.//span[@class="a-price-whole"]/text()') or " 00,00 ")[0].strip().replace(",","")

        data = {
            'Product Name': p_name,
            'Price': price,
            'Product URL': pdp_link,
        }

        print(data)

    next = tree.xpath('//a[text()="Next"]/text()')
    if next:
        n+=1
        print(f"..... Fetching Next Page {n} .....")
        fetch_data(n)
    else:
        print("No more data")

if __name__ == '__main__':
    fetch_data(1)