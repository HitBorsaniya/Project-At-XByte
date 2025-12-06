from lxml import html
import requests
import db_quotes

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8,gu;q=0.7',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://quotes.toscrape.com/page/2/',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
}

n=1
while True:
    response = requests.get(f'https://quotes.toscrape.com/page/{n}/', headers=headers, timeout=5)
    if response.status_code == 200:
        tree = html.fromstring(response.content)
        box = tree.xpath('//div[@class="quote"]')
        for i in box:
            quote = i.xpath('.//span[@class="text"]/text()')[0].strip()
            author = i.xpath('.//small[@class="author"]/text()')[0].strip()
            link = i.xpath('.//small[@class="author"]/following-sibling::a/@href')[0].strip()
            link_ = f"https://quotes.toscrape.com{link}"
            tag =  i.xpath('.//a[@class="tag"]/text()')
            tag_ = " # ".join(tag)
            data = {
                'quote': quote,
                'author': author,
                'link': link_,
                'tag': tag_,
                'status' : 'pending',
            }
            try :
                db_quotes.Quotes_pl_table.insert_one(data)
                print("Record inserted successfully!!")

            except Exception as e:
                print(e)

            print(data)
            print(f"page number : {n}")

        page = tree.xpath('//ul/li[@class="next"]/a/text()')
        if page:
            n += 1
            continue
        else:
            break

    else:
        print(response.status_code)



