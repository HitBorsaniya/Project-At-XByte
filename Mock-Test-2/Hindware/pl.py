import json
import hashlib
import requests
from certifi import contents
import pydash
import db_config
import os

folder = r"E:\XByte\Mock-Test-2\Hindware\pl-page-save"
os.makedirs(folder, exist_ok=True)


cookies = {
    '__cf_bm': '3hV2xTTNAvS7ze1.UIV1x2d2KD5k_T6oPLZ0088uKew-1766291925-1.0.1.1-WV6cU5CrItbnsuNa85IS2EiW46VvAm54kV07W_v_ziWeg9PHd81b_nUGGLM7MqnMgiBqGuJSlgGFVoY_wUDkco1qbNNPdkHldPrJxxzwHw0',
    '_gcl_au': '1.1.1301499358.1766291927',
    '_ga': 'GA1.1.1419172354.1766291928',
    '_clck': '129z0ac%5E2%5Eg21%5E0%5E2181',
    '_clsk': 's4ehuh%5E1766292243511%5E2%5E1%5Ed.clarity.ms%2Fcollect',
    '_ga_LM9T622F68': 'GS2.1.s1766292270$o2$g1$t1766292270$j60$l0$h631557820',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://hindware.com/c/bath/ceiling-showers',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'x-countryid': '1',
    # 'cookie': '__cf_bm=3hV2xTTNAvS7ze1.UIV1x2d2KD5k_T6oPLZ0088uKew-1766291925-1.0.1.1-WV6cU5CrItbnsuNa85IS2EiW46VvAm54kV07W_v_ziWeg9PHd81b_nUGGLM7MqnMgiBqGuJSlgGFVoY_wUDkco1qbNNPdkHldPrJxxzwHw0; _gcl_au=1.1.1301499358.1766291927; _ga=GA1.1.1419172354.1766291928; _clck=129z0ac%5E2%5Eg21%5E0%5E2181; _clsk=s4ehuh%5E1766292243511%5E2%5E1%5Ed.clarity.ms%2Fcollect; _ga_LM9T622F68=GS2.1.s1766292270$o2$g1$t1766292270$j60$l0$h631557820',
}


# response = requests.get ('https://hindware.com/app3/product/list', params=params, cookies=cookies, headers=headers)

def get_pl_data():

    data = db_config.cate.find({'status':'pending'})

    base_url = 'https://hindware.com/app3/product/list'

    for item in data:

        url = item['key']

        enco = url.encode("utf-8")
        hashcode = str(int(hashlib.md5(enco).hexdigest(), 16)%(10**10))
        path_ = f"pl-page-save-{hashcode}.json"
        path = os.path.join(folder, path_)

        if os.path.exists(path):
            print("File is available")
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            print("File is not available")
            last_name = url.rstrip("/").split("/")[-1]
            print(f"[REQUEST] Fetching category: {last_name}")
            params = {
                'pageNo': '1',
                'Limit': '8',
                'filters':  json.dumps({"priceRange": [], "category": last_name}),
                'searchFilters': '{}',
                'sort': json.dumps({"field": "price", "order": "desc"})
            }

            response = requests.get(base_url, params=params, cookies=cookies, headers=headers)

            if response.status_code == 200:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(response.text)
                    content = response.text
            else:
                print(response.status_code)

        tree = json.loads(content)
        rows = tree.get('data', {}).get('rows', [])
        rows1 = tree.get('data', {})

        for val in rows:

            color_labels = val.get('productAttributeDropdown', [])
            color = ""
            shape = ""
            area = ""
            mount_type = ""

            for i in color_labels:
                if i.get("Attribute", {}).get("name") == 'Color':
                    color = (i.get("AttributeOption", {}).get("optionValue"))
                if i.get("Attribute", {}).get("name") == 'Shape':
                    shape = (i.get("AttributeOption", {}).get("optionValue"))
                if i.get("Attribute", {}).get("name") == 'Area':
                    area = (i.get("AttributeOption", {}).get("optionValue"))
                if i.get("Attribute", {}).get("name") == 'Mount Type':
                    area = (i.get("AttributeOption", {}).get("optionValue"))

            last_name = url.rstrip("/").split("/")[-1]

            dict_data = {
                'Category Name ': last_name,
                'Product Name': val.get('product_name') or " ",
                'Price' : val.get('price') or " ",
                'PDP' : f"https://hindware.com/p/bath/{pydash.get(val, 'children[0].alias') or pydash.get(val, 'alias') or " "}",
                'Image': pydash.get(val, 'children[0].hnd_product_images[0].product_image') or pydash.get(val,'hnd_product_images[0].product_image' ) or " ",
                'ProductType': val.get('product_type'),
                'Color': color,
                'Shape': shape,
                'Area': area,
                'Mount Type': area,
                'sku': val.get('sku'),
                'status': 'pending'
            }

            add_data_db(dict_data)
            # print(dict_data)
        update_cate_status(data)

def add_data_db(data):
    try:
        db_config.pl.update_one({'PDP': data['PDP']}, {'$set': data}, upsert=True)
        print("Data DB Inserted")
    except Exception as e:
        print(e)

def update_cate_status(data):
    try:
        db_config.cate.update_one({'key': data['key']}, {'$set' : {'status':'pending'}})
        print(f"{data['key']} status updated")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    get_pl_data()

