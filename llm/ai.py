from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd


# -------------------- CHROME OPTIONS --------------------
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0.0.0 Safari/537.36"
)

# -------------------- DRIVER SETUP --------------------
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

# -------------------- SEARCH URL --------------------
search_query = "laptop"
base_url = f"https://www.amazon.in/s?k={search_query}"
driver.get(base_url)

time.sleep(5)

# -------------------- DATA STORAGE --------------------
all_data = []
page = 1

while True:
    print(f"Scraping Page {page}...")
    time.sleep(3)

    products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

    for product in products:
        try:
            title = product.find_element(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']").text
        except:
            title = None

        try:
            price = product.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
        except:
            price = None

        try:
            rating = product.find_element(By.XPATH, ".//span[@class='a-icon-alt']").text
        except:
            rating = None

        try:
            reviews = product.find_element(By.XPATH, ".//span[@class='a-size-base s-underline-text']").text
        except:
            reviews = None

        all_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Reviews": reviews
        })

    # -------------------- PAGINATION --------------------
    try:
        next_button = driver.find_element(By.XPATH, "//a[contains(@class,'s-pagination-next')]")
        if "disabled" in next_button.get_attribute("class"):
            print("No more pages.")
            break

        driver.execute_script("arguments[0].scrollIntoView();", next_button)
        time.sleep(2)
        next_button.click()
        page += 1
        time.sleep(5)

    except:
        print("Pagination ended.")
        break


# -------------------- SAVE TO CSV --------------------
df = pd.DataFrame(all_data)
df.to_csv("amazon_products_with_pagination.csv", index=False, encoding="utf-8-sig")

print("Scraping completed! File saved as amazon_products_with_pagination.csv")

driver.quit()
