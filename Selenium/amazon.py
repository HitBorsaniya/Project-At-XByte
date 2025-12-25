from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from PIL import Image


driver = webdriver.Chrome()

driver.get("https://www.amazon.in/")

time.sleep(3)

driver.get("https://www.amazon.in/s?k=gift&crid=2XW25VVPCXW60")
time.sleep(4)

page = 1

# Create folders
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

if not os.path.exists("temp"):
    os.makedirs("temp")

while True:
    print(f"Scraping page {page}")
    time.sleep(3)

    products = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')
    for product in products:
        try:
            name = product.find_element(By.XPATH, './/h2/span').text
            price = product.find_element(By.XPATH, './/span[@class="a-price-whole"]').text
            print({"name": name, "price": price})
        except:
            pass

    # ==========================
    # MULTI-SCREENSHOT CAPTURE
    # ==========================
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    viewport_height = driver.execute_script("return window.innerHeight")

    screenshots = []
    scroll_y = 0
    index = 0

    while scroll_y < scroll_height:
        driver.execute_script(f"window.scrollTo(0, {scroll_y});")
        time.sleep(1)

        file_path = f"temp/page_{page}_{index}.png"
        driver.save_screenshot(file_path)
        screenshots.append(file_path)

        scroll_y += viewport_height
        index += 1

    # ==========================
    # STITCH IMAGES
    # ==========================
    images = [Image.open(img) for img in screenshots]

    total_height = sum(img.height for img in images)
    max_width = max(img.width for img in images)

    final_image = Image.new("RGB", (max_width, total_height))

    y_offset = 0
    for img in images:
        final_image.paste(img, (0, y_offset))
        y_offset += img.height

    final_path = f"screenshots/page_{page}.png"
    final_image.save(final_path)

    print(f"FULL PAGE screenshot saved: {final_path}")

    # Cleanup temp files
    for img in screenshots:
        os.remove(img)

    # ==========================
    # PAGINATION
    # ==========================
    try:
        next_btn = driver.find_element(By.XPATH, '//a[contains(text(),"Next")]')

        if "s-pagination-disabled" in next_btn.get_attribute("class"):
            print("No more pages")
            break

        next_btn.click()
        page += 1
        time.sleep(4)

    except:
        print("Next button not found")
        break

driver.quit()
