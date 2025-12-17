import json

import requests

cookies = {
    'PHPSESSID': 'f7e78b1786d79b75173181633a5d8dac',
    'csrf': 'd9a1e2939e03d2c425adfec5206a45f9',
    'fbcity': '11',
    'fre': '0',
    'rd': '1380000',
    'zl': 'en',
    'fbtrack': 'ce23f71ed76c0cc6902fe0d307561a4d',
    'ltv': '11',
    'lty': '11',
    'locus': '%7B%22addressId%22%3A0%2C%22lat%22%3A23.042662%2C%22lng%22%3A72.566729%2C%22cityId%22%3A11%2C%22ltv%22%3A11%2C%22lty%22%3A%22city%22%2C%22fetchFromGoogle%22%3Afalse%2C%22dszId%22%3A3720%2C%22fen%22%3A%22Ahmedabad%22%7D',
    'ak_bmsc': '22CA15629ED70542E2E80FF1AA957784~000000000000000000000000000000~YAAQ5owsMU+UnwmbAQAAP8jwJB5wP2xLpvIe4A0nssNEY68qIPnWGcu4HrGD5ONvuajy5n6v4AKh8nrzK4lGUuyleVCz3IQJ8QnrT0JhBDP/QcgL8rhOLywQzKTpGiPhkvsKhXfQHLVtwEeXy/fMdvYAnQl8CKem+fwRcOn77Qyt+9qhZH75K1s+j8Un9i8SGHZzcJNN01IkWYoE3z0sjAdVh0+AHikIlE4wqZ3cmOEDzFC8LwcvCLJQ5nAN/B+DS77VLfdD2R6abWzyhQkh2EM9VFdd7J/50MKQSs5bMpCqcVDi+i7lLljpjR0IVrNxqBs3TC1osNU1191uv/Spk/ug2JJ3HWFd3gavsGuHp+YBLBV6VIJ62SQwX25LHl/83NTamSCpJOKD2DHi0K7P/SVxadH5jDFgvbtly3z0E6K+/Q==',
    '_gid': 'GA1.2.1977063359.1765851320',
    '_gcl_au': '1.1.96891728.1765851321',
    '_fbp': 'fb.1.1765851321370.962499039137510034',
    '_ga_2NKE6R5GNY': 'GS2.2.s1765851321$o1$g1$t1765851331$j50$l0$h0',
    '_ga_X6B66E85ZJ': 'GS2.2.s1765851321$o1$g1$t1765851331$j50$l0$h0',
    'g_state': '{"i_l":0,"i_ll":1765851331213,"i_b":"sIJLNmAbwZAT8JgyWFo0EgsnTYaK7bransfqZEQMqig","i_e":{"enable_itp_optimization":0}}',
    '_ga_2XVFHLPTVP': 'GS2.1.s1765851321$o1$g1$t1765851424$j59$l0$h0',
    '_ga': 'GA1.1.2035771545.1765851320',
    '_gat_global': '1',
    '_gat_city': '1',
    '_gat_country': '1',
    '_dd_s': 'rum=0&expire=1765852325433',
    'AWSALBTG': '2+dhSZ5w6Egx6dJjz20oGMvEdeE5ndF7FUIFB/ar4BHn/OlsLU5L+CIe/8k8U42P2KhlQrv5nowqrPv7zqV0qrEuITYJd2HSJ786Q1ddxDpJwmvMt1HiR4TDE5AwgyRjIpv7KNx8EHP2AVxRmwFTrPvfIzypu9vOfM8HDRJPHZyX',
    'AWSALBTGCORS': '2+dhSZ5w6Egx6dJjz20oGMvEdeE5ndF7FUIFB/ar4BHn/OlsLU5L+CIe/8k8U42P2KhlQrv5nowqrPv7zqV0qrEuITYJd2HSJ786Q1ddxDpJwmvMt1HiR4TDE5AwgyRjIpv7KNx8EHP2AVxRmwFTrPvfIzypu9vOfM8HDRJPHZyX',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.zomato.com',
    'priority': 'u=1, i',
    'referer': 'https://www.zomato.com/ahmedabad/delivery/dish-dosa',
    'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'x-zomato-csrft': 'd9a1e2939e03d2c425adfec5206a45f9',
    # 'cookie': 'PHPSESSID=f7e78b1786d79b75173181633a5d8dac; csrf=d9a1e2939e03d2c425adfec5206a45f9; fbcity=11; fre=0; rd=1380000; zl=en; fbtrack=ce23f71ed76c0cc6902fe0d307561a4d; ltv=11; lty=11; locus=%7B%22addressId%22%3A0%2C%22lat%22%3A23.042662%2C%22lng%22%3A72.566729%2C%22cityId%22%3A11%2C%22ltv%22%3A11%2C%22lty%22%3A%22city%22%2C%22fetchFromGoogle%22%3Afalse%2C%22dszId%22%3A3720%2C%22fen%22%3A%22Ahmedabad%22%7D; ak_bmsc=22CA15629ED70542E2E80FF1AA957784~000000000000000000000000000000~YAAQ5owsMU+UnwmbAQAAP8jwJB5wP2xLpvIe4A0nssNEY68qIPnWGcu4HrGD5ONvuajy5n6v4AKh8nrzK4lGUuyleVCz3IQJ8QnrT0JhBDP/QcgL8rhOLywQzKTpGiPhkvsKhXfQHLVtwEeXy/fMdvYAnQl8CKem+fwRcOn77Qyt+9qhZH75K1s+j8Un9i8SGHZzcJNN01IkWYoE3z0sjAdVh0+AHikIlE4wqZ3cmOEDzFC8LwcvCLJQ5nAN/B+DS77VLfdD2R6abWzyhQkh2EM9VFdd7J/50MKQSs5bMpCqcVDi+i7lLljpjR0IVrNxqBs3TC1osNU1191uv/Spk/ug2JJ3HWFd3gavsGuHp+YBLBV6VIJ62SQwX25LHl/83NTamSCpJOKD2DHi0K7P/SVxadH5jDFgvbtly3z0E6K+/Q==; _gid=GA1.2.1977063359.1765851320; _gcl_au=1.1.96891728.1765851321; _fbp=fb.1.1765851321370.962499039137510034; _ga_2NKE6R5GNY=GS2.2.s1765851321$o1$g1$t1765851331$j50$l0$h0; _ga_X6B66E85ZJ=GS2.2.s1765851321$o1$g1$t1765851331$j50$l0$h0; g_state={"i_l":0,"i_ll":1765851331213,"i_b":"sIJLNmAbwZAT8JgyWFo0EgsnTYaK7bransfqZEQMqig","i_e":{"enable_itp_optimization":0}}; _ga_2XVFHLPTVP=GS2.1.s1765851321$o1$g1$t1765851424$j59$l0$h0; _ga=GA1.1.2035771545.1765851320; _gat_global=1; _gat_city=1; _gat_country=1; _dd_s=rum=0&expire=1765852325433; AWSALBTG=2+dhSZ5w6Egx6dJjz20oGMvEdeE5ndF7FUIFB/ar4BHn/OlsLU5L+CIe/8k8U42P2KhlQrv5nowqrPv7zqV0qrEuITYJd2HSJ786Q1ddxDpJwmvMt1HiR4TDE5AwgyRjIpv7KNx8EHP2AVxRmwFTrPvfIzypu9vOfM8HDRJPHZyX; AWSALBTGCORS=2+dhSZ5w6Egx6dJjz20oGMvEdeE5ndF7FUIFB/ar4BHn/OlsLU5L+CIe/8k8U42P2KhlQrv5nowqrPv7zqV0qrEuITYJd2HSJ786Q1ddxDpJwmvMt1HiR4TDE5AwgyRjIpv7KNx8EHP2AVxRmwFTrPvfIzypu9vOfM8HDRJPHZyX',
}


def fetch_restaurants():
    session = create_session()
    page_num = 1
    has_more = True

    while has_more and page_num <= 150:
        response = session.post(
            API_URL,
            headers=headers,
            cookies=cookies,
            json=json_data,
            timeout=30
        )

        if response.status_code != 200:
            print(f"❌ Failed on page {page_num} | Status: {response.status_code}")
            break

        data = response.json()
        sections = data.get("sections", {})

        results = sections.get("SECTION_SEARCH_RESULT", [])
        if not results:
            break

        for item in results:
            info = item.get("info", {})
            rating_info = info.get("rating", {})

            restaurant = {
                "Restaurant Name": info.get("name", ""),
                "Res ID": info.get("resId", ""),
                "Cuisines": ", ".join(
                    c.get("name", "") for c in info.get("cuisine", []) if isinstance(c, dict)
                ),
                "Rating": rating_info.get("aggregate_rating", "0"),
                "Reviews": rating_info.get("votes", "0"),
                "Cost for Two": info.get("cft", {}).get("text", ""),
                "Delivery Time": item.get("order", {}).get("deliveryTime", ""),
                "Distance": item.get("distance", ""),
                "Order URL": "https://www.zomato.com"
                + item.get("cardAction", {}).get("clickUrl", ""),
                "Status": "pending",
            }

            print(restaurant)

        meta = sections.get("SECTION_SEARCH_META_INFO", {}).get("searchMetaData", {})
        has_more = meta.get("hasMore", False)

        postback_params = json.loads(meta.get("postbackParams", "{}"))
        processed_ids = postback_params.get("processed_chain_ids", [])

        if has_more:
            filters_dict = json.loads(json_data["filters"])
            postback = json.loads(filters_dict["searchMetadata"]["postbackParams"])

            postback["processed_chain_ids"] = processed_ids
            postback["shown_res_count"] = len(processed_ids)

            filters_dict["searchMetadata"]["postbackParams"] = json.dumps(postback)
            json_data["filters"] = json.dumps(filters_dict)

        page_num += 1


if __name__ == "__main__":
    fetch_restaurants()