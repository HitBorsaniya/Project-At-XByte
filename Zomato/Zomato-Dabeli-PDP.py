import requests
import db_config
from lxml import html


cookies = {
    'fbcity': '11',
    'fre': '0',
    'rd': '1380000',
    'zl': 'en',
    'fbtrack': 'ce23f71ed76c0cc6902fe0d307561a4d',
    'ltv': '11',
    'lty': '11',
    'locus': '%7B%22addressId%22%3A0%2C%22lat%22%3A23.042662%2C%22lng%22%3A72.566729%2C%22cityId%22%3A11%2C%22ltv%22%3A11%2C%22lty%22%3A%22city%22%2C%22fetchFromGoogle%22%3Afalse%2C%22dszId%22%3A3720%2C%22fen%22%3A%22Ahmedabad%22%7D',
    '_gid': 'GA1.2.1977063359.1765851320',
    '_gcl_au': '1.1.96891728.1765851321',
    '_fbp': 'fb.1.1765851321370.962499039137510034',
    'PHPSESSID': '58766ae7ec0466c2356fe403a87e7912',
    'csrf': '1fc7a859273df81f4066e20364aec6c8',
    'ak_bmsc': '53AD0726870FD2997A1811E375148F13~000000000000000000000000000000~YAAQt4wsMbgz/iSbAQAAfLgTKh4u+dpNfVTdkCtRr6EAnX3qBlJ5GqDHbka1XvmNqhOay2Zx8+2dBFqHCz2kJ5pswKZgZeJnJTzpIL6DCYfe3MW014uGf+MEHZ6yIjUpDkHQcEjUClWLJ3H3kNwmCcSKZgnt7Dn9o+WuCIYcmaAbhTjTR87hzoavA1y2QtqgTlwEfdbuok7z20SRY7KNyiko9FgKGhe0aeywYB8kotkrxNwESTgRr5mdTqmY9GrOZbi9AzjXZwj173Cf5n7wTadh+FrulBMi4WXaWw/tO81PeleuXZwL4KTcHSamolhB0g0ZoiLHYk5lAhG7qSUN9sCqVW8HzvyOaPMKP5eTqkFnwuvvPPRSOkHODVNb+RT9OdYF6e9PR1E8aKfuTwVxGonpGaO7Xk1oR/k=',
    'bm_sz': '7C559CC6F39EA639C854355C08036F66~YAAQMxzFF7KJuyWbAQAA4oUmKh75UApMLT/LUAUeTdUVuEYzAkAWAqhIOOv10Ep8NGVHuDZy2DnL6BAFoWZ7/J3moFmzMWAjxNLt2wbg4Sy44XOVzN0q2qAA6gRGdM0m9htLQxsH4Le1R+OFaUlYDcZdqt4V+nY4llMNGciPydXjpQZN9lH8EEAh0r5V7T6rHk6WF+t4n3Ugc6B/N36rmB5Q+2t3/KPu56g2moodb1JYYrLVxf6KxRbAlnebNpgc8MS/T1hldSMZMOM731FdlzGUuw/19uEceR8xsWdkwegAEGCOl9T0HcB0TMcHIXxXdXfzjiqsudTQ1euRY/daDwfj8to0l70cAYg34JgdSYYWlTBTFaa6pDSCDLye3hbVyO1+iDBbfrBd+rubDaI=~3752756~4277813',
    '_abck': '3745ACC1B5ECF0A9FD0C046A08E536E2~-1~YAAQjYwsMd5q7SSbAQAA6CgqKg+Kp29POcXrtqWh6hP+XnqC7X1R0vjgJX1N/1Ryma6gA7yWGFiYFYmvHwaQF0rb8OXP3+cWhZjHRGt82MYHOA/zqMfbZdUrcE9WeFFUi5YwOwezr0XFn9pyvikFMheI+xy60CJsG6nYKcO2j7uTPXH5LbfEGi0elT+IJvzvfqJoqWAdU9BOjtSnJ849QQZKT5Eaxw+vnIPbeeAq5nm3HmwGO2ruO92z/UBuWPXyk2Cy8d3c7PgSUfpXAjsQlp3L+KNyrkdjNv1ItcdKcNMKj+3aLHaeQrvtXaCuFbQvPr1aGAA6oCSGcr75OdHW8QCX8HQAfoq/uiBKALrAPbhgX4w4nmZyIv2lPtR1Owv6K3eTAvGKopdLKizgV+n/9I2tG8gr4quHS1U6j2XX7JN3xOxsxuEqW59UwRSv3mfen0vE/qr9HzrDTpdasC+7kRtnnYYn3uYwqqjIqG5ZE4/2~-1~-1~-1~-1~-1',
    '_ga_2XVFHLPTVP': 'GS2.1.s1765937498$o5$g1$t1765940416$j60$l0$h0',
    '_ga': 'GA1.1.2035771545.1765851320',
    '_gat_global': '1',
    '_gat_city': '1',
    '_gat_country': '1',
    'AWSALBTG': 'IX/WW6H9T1UpJBmOqWo/FcvIHjoeL7k1JIqEPMnEo0RXlq8Hkc12VkoghWsenvjVs1cWUIaurhP14RW2Acr0jRO34nimSMoU/GQwzu8Qj6XuSAR7tIj3c26x9gczBxtBF+SO6YDqLc+FTuwnAu/DiSob2BxVBttxLYwUavbKLIrc',
    'AWSALBTGCORS': 'IX/WW6H9T1UpJBmOqWo/FcvIHjoeL7k1JIqEPMnEo0RXlq8Hkc12VkoghWsenvjVs1cWUIaurhP14RW2Acr0jRO34nimSMoU/GQwzu8Qj6XuSAR7tIj3c26x9gczBxtBF+SO6YDqLc+FTuwnAu/DiSob2BxVBttxLYwUavbKLIrc',
    'g_state': '{"i_l":0,"i_ll":1765940417216,"i_b":"NfwOyQwAa6nVnM688/ofVYJYWjGR1XmB+npi6OlVFUo","i_e":{"enable_itp_optimization":0}}',
    '_ga_X6B66E85ZJ': 'GS2.2.s1765937498$o5$g1$t1765940417$j60$l0$h0',
    '_ga_2NKE6R5GNY': 'GS2.2.s1765937498$o5$g1$t1765940417$j60$l0$h0',
    '_dd_s': 'rum=0&expire=1765941316196',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
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
    # 'cookie': 'fbcity=11; fre=0; rd=1380000; zl=en; fbtrack=ce23f71ed76c0cc6902fe0d307561a4d; ltv=11; lty=11; locus=%7B%22addressId%22%3A0%2C%22lat%22%3A23.042662%2C%22lng%22%3A72.566729%2C%22cityId%22%3A11%2C%22ltv%22%3A11%2C%22lty%22%3A%22city%22%2C%22fetchFromGoogle%22%3Afalse%2C%22dszId%22%3A3720%2C%22fen%22%3A%22Ahmedabad%22%7D; _gid=GA1.2.1977063359.1765851320; _gcl_au=1.1.96891728.1765851321; _fbp=fb.1.1765851321370.962499039137510034; PHPSESSID=58766ae7ec0466c2356fe403a87e7912; csrf=1fc7a859273df81f4066e20364aec6c8; ak_bmsc=53AD0726870FD2997A1811E375148F13~000000000000000000000000000000~YAAQt4wsMbgz/iSbAQAAfLgTKh4u+dpNfVTdkCtRr6EAnX3qBlJ5GqDHbka1XvmNqhOay2Zx8+2dBFqHCz2kJ5pswKZgZeJnJTzpIL6DCYfe3MW014uGf+MEHZ6yIjUpDkHQcEjUClWLJ3H3kNwmCcSKZgnt7Dn9o+WuCIYcmaAbhTjTR87hzoavA1y2QtqgTlwEfdbuok7z20SRY7KNyiko9FgKGhe0aeywYB8kotkrxNwESTgRr5mdTqmY9GrOZbi9AzjXZwj173Cf5n7wTadh+FrulBMi4WXaWw/tO81PeleuXZwL4KTcHSamolhB0g0ZoiLHYk5lAhG7qSUN9sCqVW8HzvyOaPMKP5eTqkFnwuvvPPRSOkHODVNb+RT9OdYF6e9PR1E8aKfuTwVxGonpGaO7Xk1oR/k=; bm_sz=7C559CC6F39EA639C854355C08036F66~YAAQMxzFF7KJuyWbAQAA4oUmKh75UApMLT/LUAUeTdUVuEYzAkAWAqhIOOv10Ep8NGVHuDZy2DnL6BAFoWZ7/J3moFmzMWAjxNLt2wbg4Sy44XOVzN0q2qAA6gRGdM0m9htLQxsH4Le1R+OFaUlYDcZdqt4V+nY4llMNGciPydXjpQZN9lH8EEAh0r5V7T6rHk6WF+t4n3Ugc6B/N36rmB5Q+2t3/KPu56g2moodb1JYYrLVxf6KxRbAlnebNpgc8MS/T1hldSMZMOM731FdlzGUuw/19uEceR8xsWdkwegAEGCOl9T0HcB0TMcHIXxXdXfzjiqsudTQ1euRY/daDwfj8to0l70cAYg34JgdSYYWlTBTFaa6pDSCDLye3hbVyO1+iDBbfrBd+rubDaI=~3752756~4277813; _abck=3745ACC1B5ECF0A9FD0C046A08E536E2~-1~YAAQjYwsMd5q7SSbAQAA6CgqKg+Kp29POcXrtqWh6hP+XnqC7X1R0vjgJX1N/1Ryma6gA7yWGFiYFYmvHwaQF0rb8OXP3+cWhZjHRGt82MYHOA/zqMfbZdUrcE9WeFFUi5YwOwezr0XFn9pyvikFMheI+xy60CJsG6nYKcO2j7uTPXH5LbfEGi0elT+IJvzvfqJoqWAdU9BOjtSnJ849QQZKT5Eaxw+vnIPbeeAq5nm3HmwGO2ruO92z/UBuWPXyk2Cy8d3c7PgSUfpXAjsQlp3L+KNyrkdjNv1ItcdKcNMKj+3aLHaeQrvtXaCuFbQvPr1aGAA6oCSGcr75OdHW8QCX8HQAfoq/uiBKALrAPbhgX4w4nmZyIv2lPtR1Owv6K3eTAvGKopdLKizgV+n/9I2tG8gr4quHS1U6j2XX7JN3xOxsxuEqW59UwRSv3mfen0vE/qr9HzrDTpdasC+7kRtnnYYn3uYwqqjIqG5ZE4/2~-1~-1~-1~-1~-1; _ga_2XVFHLPTVP=GS2.1.s1765937498$o5$g1$t1765940416$j60$l0$h0; _ga=GA1.1.2035771545.1765851320; _gat_global=1; _gat_city=1; _gat_country=1; AWSALBTG=IX/WW6H9T1UpJBmOqWo/FcvIHjoeL7k1JIqEPMnEo0RXlq8Hkc12VkoghWsenvjVs1cWUIaurhP14RW2Acr0jRO34nimSMoU/GQwzu8Qj6XuSAR7tIj3c26x9gczBxtBF+SO6YDqLc+FTuwnAu/DiSob2BxVBttxLYwUavbKLIrc; AWSALBTGCORS=IX/WW6H9T1UpJBmOqWo/FcvIHjoeL7k1JIqEPMnEo0RXlq8Hkc12VkoghWsenvjVs1cWUIaurhP14RW2Acr0jRO34nimSMoU/GQwzu8Qj6XuSAR7tIj3c26x9gczBxtBF+SO6YDqLc+FTuwnAu/DiSob2BxVBttxLYwUavbKLIrc; g_state={"i_l":0,"i_ll":1765940417216,"i_b":"NfwOyQwAa6nVnM688/ofVYJYWjGR1XmB+npi6OlVFUo","i_e":{"enable_itp_optimization":0}}; _ga_X6B66E85ZJ=GS2.2.s1765937498$o5$g1$t1765940417$j60$l0$h0; _ga_2NKE6R5GNY=GS2.2.s1765937498$o5$g1$t1765940417$j60$l0$h0; _dd_s=rum=0&expire=1765941316196',
}

# response = requests.get('https://www.zomato.com/ahmedabad/davda-dabeli-and-kadak-sola', cookies=cookies, headers=headers)

data = db_config.pl.find({'status':'pending'})

for item in data:
    url = item['Order URL']

    response = requests.get(url, headers=headers, cookies=cookies)
    if response.status_code != 200:
        print("Error....")
        print(response.status_code)
        continue


    tree = html.fromstring(response.text)

    image = tree.xpath('//img[@class="sc-s1isp7-5 eQUAyn"]/@src')
    image = " | ".join(img for img in image) or " "
    address = tree.xpath('//div[@class="sc-clNaTc ckqoPM"]/text()') or ''
    time = tree.xpath('//span[@class="sc-kasBVs dfwCXs"]/text()') or " "
    Avg_Cost = tree.xpath('//p[@class="sc-1hez2tp-0 sc-bocRTG iZcldW"]/text()') or " "
    mobile = tree.xpath('//a[@class="sc-bFADNz leEVAg"]/text()') or ''
    Cuisines = tree.xpath('//div[text()="Cuisines"]/following-sibling::div/a/div/text()') or " "
    More_Info = tree.xpath('//h3[text()="More Info"]/following-sibling::div//div/p/text()') or ''
    More_Info = " | ".join(data for data in More_Info) if More_Info else ''
    Related_Content = tree.xpath('//h6[contains(text(),"Related to ")]/following-sibling::div[@class="sc-iWadT XrbmL"]/a/text()') or " "
    print(Related_Content)
    Related_Content = " ".join(data for data in Related_Content if data) or ''
    Around_Resto = tree.xpath('//h6[contains(text(),"Restaurants around")]/following-sibling::div[@class="sc-iWadT XrbmL"]/a/text()') or " "
    Around_Resto = " ".join(data for data in Around_Resto if data) or ''
    Frenchises = tree.xpath('//h6[contains(text(),"Frequent searches leading")]/following-sibling::div[@class="sc-iWadT XrbmL"]/a/text()') or " "
    Frenchises = " ".join(data for data in Frenchises if data) or ''

    data = {
        'image': image,
        'address': address[0].strip(),
        'time': time[0].strip(),
        'Avg_Cost': Avg_Cost[0].strip(),
        'mobile': mobile[0].strip(),
        'Cuisines': Cuisines[0].strip(),
        'More_Info': More_Info,
        'Related_Content': Related_Content,
        'Around_Resto': Around_Resto,
        'Frenchises': Frenchises,
    }

    # print(data)






