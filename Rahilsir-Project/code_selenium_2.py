from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# -------------------------------
# Browser setup
# -------------------------------
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

wait = WebDriverWait(driver, 30)

try:
    # -------------------------------
    # Open site
    # -------------------------------
    driver.get("https://gujarathc-casestatus.nic.in/gujarathc/")

    # -------------------------------
    # WAIT until JS is fully loaded
    # -------------------------------
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    # -------------------------------
    # Click CASE DETAIL tile
    # -------------------------------
    # We wait for the tile to be present
    case_detail = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//b[normalize-space()='CASE DETAIL']/ancestor::a")
        )
    )

    # JS click is often safer for these tiles as they might be intercepted by overlays
    driver.execute_script("arguments[0].click();", case_detail)

    # -------------------------------
    # Confirm Case Detail section loaded
    # -------------------------------
    # Wait for the 'Case Mode' dropdown to appear
    wait.until(EC.presence_of_element_located((By.ID, "casefr")))
    print("✅ CASE DETAIL page loaded successfully")

    # -------------------------------
    # FILL THE FORM DATA
    # -------------------------------

    # 1. Select CASE MODE (Starts with "r")
    case_mode_dropdown = Select(driver.find_element(By.ID, "casefr"))

    found_mode = False
    for option in case_mode_dropdown.options:
        # Check if option text starts with 'r' (case insensitive)
        if option.text.strip().lower().startswith("r"):
            case_mode_dropdown.select_by_visible_text(option.text)
            print(f"✅ Selected Case Mode: {option.text}")
            found_mode = True
            break

    if not found_mode:
        print("⚠️ Could not find a Case Mode starting with 'r'")

    # Small pause to allow page to refresh Case Type list if necessary (common in NIC sites)
    time.sleep(2)

    # 2. Select CASE TYPE (Starts with "cr.ma")
    # Re-find the element to avoid StaleElementReferenceException if the page refreshed
    case_type_dropdown = Select(driver.find_element(By.ID, "casetype"))

    found_type = False
    for option in case_type_dropdown.options:
        # Check if option text starts with 'cr.ma' (case insensitive)
        if option.text.strip().lower().startswith("cr.ma"):
            case_type_dropdown.select_by_visible_text(option.text)
            print(f"✅ Selected Case Type: {option.text}")
            found_type = True
            break

    if not found_type:
        print("⚠️ Could not find a Case Type starting with 'cr.ma'")

    # 3. Enter CASE NUMBER
    case_number_input = driver.find_element(By.ID, "casenumber")
    case_number_input.clear()
    case_number_input.send_keys("7510")
    print("✅ Entered Case Number: 7510")

    # 4. Enter CASE YEAR
    case_year_input = driver.find_element(By.ID, "caseyear")
    case_year_input.clear()
    case_year_input.send_keys("2016")
    print("✅ Entered Case Year: 2016")

    # -------------------------------
    # Finalize
    # -------------------------------
    print("\n------------------------------------------------")
    print("🛑 PAUSING: Please manually enter the CAPTCHA and click 'GO'")
    print("------------------------------------------------")

    # Keep the browser open for you to verify and finish
    input("Press Enter in this terminal to close the browser...")

except Exception as e:
    print(f"❌ An error occurred: {e}")

finally:
    driver.quit()