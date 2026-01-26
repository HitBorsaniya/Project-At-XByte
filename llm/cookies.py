import requests
import time
import pydash
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

session = requests.Session()
cookie_lock = Lock()

HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/143.0.0.0 Safari/537.36",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-IN,en;q=0.9",
    "referer": "https://www.klook.com/en-IN/activity/30333-miracle-garden-ticket-dubai/",
    "x-requested-with": "XMLHttpRequest",
    "x-klook-host": "www.klook.com",
    "x-klook-market": "global",
    "x-platform": "desktop",
}

HOME_URL = "https://www.klook.com/en-IN/activity/30333-miracle-garden-ticket-dubai/"
API_URL = (
    "https://www.klook.com/v1/experiencesrv/activity/package_service/"
    "get_package_card_sku_info_sources?"
    "package_ids=328992,333495,334189,341475,349940,381040,459913,613713"
    "&k_lang=en_IN&k_currency=INR&preview=0"
)

COOKIE_LIFE = 300  # 5 minutes
last_cookie_time = 0


# -------------------- REFRESH COOKIES --------------------
def refresh_cookies():
    global last_cookie_time
    with cookie_lock:
        # double-check inside lock
        # if time.time() - last_cookie_time < COOKIE_LIFE:
        #     return

        print("🔄 Refreshing cookies...")
        session.get(HOME_URL, headers=HEADERS, timeout=20)
        print(session.cookies)
        last_cookie_time = time.time()


# -------------------- FETCH API --------------------
def fetch_api(thread_id):
    global last_cookie_time

    # proactive refresh
    if time.time() - last_cookie_time > COOKIE_LIFE:
        refresh_cookies()

    response = session.get(API_URL, headers=HEADERS, timeout=20)

    # detect expiry / block
    if (
        response.status_code in [401, 403, 429]
        or "datadome" in response.text.lower()
        or "captcha" in response.text.lower()
    ):
        print(f"⚠️ Thread {thread_id}: Cookies expired")
        refresh_cookies()
        time.sleep(1)
        response = session.get(API_URL, headers=HEADERS, timeout=20)

    print(f"✅ Thread {thread_id}: Status {response.status_code}")
    return response


# -------------------- THREAD TASK --------------------
def task(thread_id):
    response = fetch_api(thread_id)

    try:
        data = response.json()
        print(data)
        price = pydash.get(data, "result.packages_with_sku[0].price_show.sale_price")
        package_id = pydash.get(data, "result.packages_with_sku[0].package_id")
        print(f"🧵 Thread {thread_id} → Package {package_id} → Price {price}")
    except Exception as e:
        print(f"❌ Thread {thread_id} error:", e)


# -------------------- START --------------------
refresh_cookies()

with ThreadPoolExecutor(max_workers=5) as executor:
    for i in range(100):
        executor.submit(task, i)
        time.sleep(1)  # simulate real traffic
