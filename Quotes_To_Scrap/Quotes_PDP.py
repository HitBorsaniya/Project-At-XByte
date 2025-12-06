import db_quotes
from lxml import html
import requests

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8,gu;q=0.7',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
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

data = db_quotes.Quotes_pl_table.find({'status':'pending'})

for quote in data:

    link = quote['link']
    response = requests.get(link, headers=headers)

    if response.status_code == 200:
        tree = html.fromstring(response.text)

        author = tree.xpath('//h3[@class="author-title"]/text()')[0].strip()
        author_born_date = tree.xpath('//span[@class="author-born-date"]/text()')[0].strip()
        author_born_place = tree.xpath('//span[@class="author-born-location"]/text()')[0].strip()
        Description = tree.xpath('//div[@class="author-description"]/text()')[0].strip()

        data = {
            'author': author,
            'author_born_date': author_born_date,
            'author_born_place': author_born_place,
            'description': Description,
            'original_pl_id': quote['_id']
        }

        try :

            db_quotes.Quotes_pdp_table.insert_one(data)
            db_quotes.Quotes_pl_table.update_one({'_id': quote['_id']}, {'$set': {'status': 'done'}})

        except Exception as e:
            print(e)

        print(data)

    else :
        print(response.status_code)