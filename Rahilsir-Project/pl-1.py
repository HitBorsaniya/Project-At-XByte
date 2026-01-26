import os
import time
import hashlib
import requests
from lxml import html

import db_config


# ==========================
# CONFIGURATION
# ==========================

BASE_URL = "https://gujarathc-casestatus.nic.in/gujarathc/SearchLCFIR"

FOLDER_NAME = "ahmedabad-crime-data-dcb"
os.makedirs(FOLDER_NAME, exist_ok=True)

COOKIES = {
    "JSESSIONID": "158A997970D67768DCCA82E26CF55E77",
}

HEADERS = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://gujarathc-casestatus.nic.in",
    "Referer": "https://gujarathc-casestatus.nic.in/gujarathc/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/144.0.0.0 Safari/537.36"
    ),
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}


# ==========================
# DATABASE FUNCTION
# ==========================

def add_data_db(data: dict):
    """Insert scraped data into MongoDB"""
    try:
        db_config.collection1.insert_one(data)
        print("✔ Data inserted")
    except Exception as e:
        print("❌ DB Error:", e)


# ==========================
# SCRAPING FUNCTION
# ==========================

def scrap_data_pl_ahmedabad():
    counter = 1

    while True:
        payload = {
            "policestationcode": "120145",
            "firtype": "select",
            "firnumber": "",
            "firyear": "",
            "counter": str(counter),
        }

        # Create unique file hash
        hash_code = int(
            hashlib.md5(BASE_URL.encode("utf-8")).hexdigest(), 16
        ) % (10**109)

        file_name = (
            f"page-save-data-{hash_code}-"
            f"{payload['counter']}-{payload['policestationcode']}.html"
        )
        file_path = os.path.join(FOLDER_NAME, file_name)

        # ==========================
        # LOAD OR FETCH DATA
        # ==========================

        if os.path.exists(file_path):
            print("📁 Loading from saved file")
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        else:
            print("🌐 Scraping new page...")
            time.sleep(3)

            response = requests.post(
                BASE_URL,
                cookies=COOKIES,
                headers=HEADERS,
                data=payload,
                timeout=15,
            )

            if response.status_code != 200:
                print("❌ Failed to fetch data")
                break

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(response.text)

            content = response.text

        # ==========================
        # PARSE HTML
        # ==========================

        tree = html.fromstring(content)
        rows = tree.xpath('//tr[@style="cursor: pointer;"]')

        print(f"📄 Page {counter} | Records found: {len(rows)}")

        if not rows:
            print("🚫 No more data found")
            break

        # ==========================
        # EXTRACT DATA
        # ==========================

        page_data = []

        for row in rows:
            lowercourt_name = (row.xpath(".//td[1]/text()") or [""])[0].strip()
            judgement_date = (row.xpath(".//td[2]/text()") or [""])[0].strip()
            lowercourt_case = (row.xpath(".//td[3]/text()") or [""])[0].strip()
            main_case = (row.xpath(".//td[4]/text()") or [""])[0].strip()
            fir_detail = (row.xpath(".//td[5]/text()") or [""])[0].strip()

            fir_type = fir_detail.split("/")[0].strip()

            record = {
                "LOWERCOURT_NAME": lowercourt_name,
                "JUDGEMENT_DATE": judgement_date,
                "LOWERCOURT_CASEDETAIL": lowercourt_case,
                "MAIN_CASEDETAIL": main_case,
                "FIR_DETAIL": fir_detail,
                "FIR_TYPE": fir_type,
            }

            add_data_db(record)
            page_data.append(record)

        print(f"✅ Saved {len(page_data)} records")
        counter += 1


# ==========================
# MAIN ENTRY POINT
# ==========================

if __name__ == "__main__":
    scrap_data_pl_ahmedabad()
