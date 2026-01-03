import requests

cookies = {
    '_fbp': 'fb.1.1767364027652.1536523600',
    'WZRK_G': '80e6129121bb49e5bf5f938120ab3dc0',
    '_gcl_au': '1.1.1211049607.1767364029',
    '_ga': 'GA1.1.1353623878.1767364029',
    'nms_mgo_pincode': '382418',
    'nms_mgo_city': 'Ahmedabad',
    'nms_mgo_state_code': 'GJ',
    'AKA_A2': 'A',
    '__tr_jr': 'W3sidXRtcyI6Im9yZ2FuaWMiLCJ0cyI6IjIwMjYtMDEtMDNUMDM6NDY6NDEuMzIxWiIsImVuYyI6InllcyJ9XQ==',
    '_gcl_gs': '2.1.k1$i1767411998$u220930947',
    '_gcl_aw': 'GCL.1767412033.Cj0KCQiA9t3KBhCQARIsAJOcR7wqa53wxLvXn9z2W_xLxur6lzKQkb061UxURoPYFS1Y3Zcp5tw7ONoaAtsEEALw_wcB',
    '__tr_luptv': '1767412436939',
    '_ga_XHR9Q2M3VV': 'GS2.1.s1767412002$o2$g1$t1767412474$j19$l0$h1458896991',
    'RT': '"z=1&dm=www.jiomart.com&si=3c60f3dc-fc74-4e39-8698-eb31c3eb19cf&ss=mjxrgxto&sl=5&tt=5tz&obo=2&rl=1"',
    'WZRK_S_88R-W4Z-495Z': '%7B%22p%22%3A6%2C%22s%22%3A1767411985%2C%22t%22%3A1767412475%7D',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'pin': '382418',
    'priority': 'u=1, i',
    'referer': 'https://www.jiomart.com/p/groceries/rjm-gold-chakki-fresh-atta-whole-wheat-flour-for-soft-nutritious-rotis-high-fiber-protein-no-preservatives-hygienic-packaging-5-kg/613034706',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': '_fbp=fb.1.1767364027652.1536523600; WZRK_G=80e6129121bb49e5bf5f938120ab3dc0; _gcl_au=1.1.1211049607.1767364029; _ga=GA1.1.1353623878.1767364029; nms_mgo_pincode=382418; nms_mgo_city=Ahmedabad; nms_mgo_state_code=GJ; AKA_A2=A; __tr_jr=W3sidXRtcyI6Im9yZ2FuaWMiLCJ0cyI6IjIwMjYtMDEtMDNUMDM6NDY6NDEuMzIxWiIsImVuYyI6InllcyJ9XQ==; _gcl_gs=2.1.k1$i1767411998$u220930947; _gcl_aw=GCL.1767412033.Cj0KCQiA9t3KBhCQARIsAJOcR7wqa53wxLvXn9z2W_xLxur6lzKQkb061UxURoPYFS1Y3Zcp5tw7ONoaAtsEEALw_wcB; __tr_luptv=1767412436939; _ga_XHR9Q2M3VV=GS2.1.s1767412002$o2$g1$t1767412474$j19$l0$h1458896991; RT="z=1&dm=www.jiomart.com&si=3c60f3dc-fc74-4e39-8698-eb31c3eb19cf&ss=mjxrgxto&sl=5&tt=5tz&obo=2&rl=1"; WZRK_S_88R-W4Z-495Z=%7B%22p%22%3A6%2C%22s%22%3A1767411985%2C%22t%22%3A1767412475%7D',
}

response = requests.get('https://www.jiomart.com/catalog/productdetails/get/596570298', cookies=cookies, headers=headers)


print(response.text)