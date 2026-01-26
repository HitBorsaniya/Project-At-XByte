import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# --- CONFIGURATION ---
CASE_TYPE_PREFIX = "r"  # e.g., Registration
CASE_CODE_PREFIX = "cr.ma"  # e.g., CR.MA
CASE_NUMBER = "7510"
CASE_YEAR = "2016"
OUTPUT_FILENAME = "case_details.html"

# -------------------------------
# BROWSER SETUP
# -------------------------------
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)
wait = WebDriverWait(driver, 30)

try:
    # 1. OPEN SITE
    driver.get("https://gujarathc-casestatus.nic.in/gujarathc/")
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    # 2. NAVIGATE TO CASE DETAILS
    case_detail = wait.until(
        EC.presence_of_element_located((By.XPATH, "//b[normalize-space()='CASE DETAIL']/ancestor::a")))
    driver.execute_script("arguments[0].click();", case_detail)
    wait.until(EC.presence_of_element_located((By.ID, "casefr")))

    # 3. FILL FORM
    # Case Mode
    case_mode_dropdown = Select(driver.find_element(By.ID, "casefr"))
    for option in case_mode_dropdown.options:
        if option.text.strip().lower().startswith(CASE_TYPE_PREFIX):
            case_mode_dropdown.select_by_visible_text(option.text)
            break
    time.sleep(2)

    # Case Type
    case_type_dropdown = Select(driver.find_element(By.ID, "casetype"))
    for option in case_type_dropdown.options:
        if option.text.strip().lower().startswith(CASE_CODE_PREFIX):
            case_type_dropdown.select_by_visible_text(option.text)
            break

    # Number & Year
    driver.find_element(By.ID, "casenumber").send_keys(CASE_NUMBER)
    driver.find_element(By.ID, "caseyear").send_keys(CASE_YEAR)

    # 4. CAPTCHA & SUBMIT
    print("\n" + "=" * 50)
    print("⚠️ PAUSED: Please type the CAPTCHA in the browser.")
    print("👉 Press ENTER here in the terminal when you are done.")
    print("=" * 50)
    input("Waiting for you... Press Enter > ")

    print("✅ Clicking GO...")
    go_btn = driver.find_element(By.ID, "gobutton")
    driver.execute_script("arguments[0].click();", go_btn)

    # 5. WAIT FOR RESULTS
    print("⏳ Waiting for results to load...")
    # We wait until the 'Status' text appears, ensuring the page has fully refreshed with data
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Status')]")))

    # 6. SAVE HTML TO FILE
    print("💾 Saving HTML...")

    # Get the complete HTML source of the current page
    page_html = driver.page_source

    # Write to file with UTF-8 encoding
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
        f.write(page_html)

    print(f"✅ Success! Page saved to: {OUTPUT_FILENAME}")

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    print("Closing browser in 5 seconds...")
    time.sleep(5)
    driver.quit()