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
    # 1. Open site & Navigate
    # -------------------------------
    driver.get("https://gujarathc-casestatus.nic.in/gujarathc/")

    # Wait for page load
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    # Click CASE DETAIL tile
    case_detail = wait.until(
        EC.presence_of_element_located((By.XPATH, "//b[normalize-space()='CASE DETAIL']/ancestor::a")))
    driver.execute_script("arguments[0].click();", case_detail)

    # Wait for form to load
    wait.until(EC.presence_of_element_located((By.ID, "casefr")))
    print("✅ Page loaded.")

    # -------------------------------
    # 2. Fill Form Data
    # -------------------------------
    # Case Mode ('r')
    case_mode_dropdown = Select(driver.find_element(By.ID, "casefr"))
    for option in case_mode_dropdown.options:
        if option.text.strip().lower().startswith("r"):
            case_mode_dropdown.select_by_visible_text(option.text)
            break

    time.sleep(2)  # Wait for reload

    # Case Type ('cr.ma')
    case_type_dropdown = Select(driver.find_element(By.ID, "casetype"))
    for option in case_type_dropdown.options:
        if option.text.strip().lower().startswith("cr.ma"):
            case_type_dropdown.select_by_visible_text(option.text)
            break

    # Number & Year
    driver.find_element(By.ID, "casenumber").send_keys("7510")
    driver.find_element(By.ID, "caseyear").send_keys("2016")

    # -------------------------------
    # 3. HUMAN INTERVENTION (CAPTCHA)
    # -------------------------------
    print("\n" + "=" * 50)
    print("⚠️  PAUSED: Please solve the CAPTCHA and click 'GO' on the browser.")
    print("👉  Once the results appear on screen, press ENTER here to scrape the data.")
    print("=" * 50 + "\n")

    input("Press Enter to continue scraping...")

    # -------------------------------
    # 4. SCRAPE RESULTS
    # -------------------------------
    print("\n🔍 Scraping Case Details...")

    # A. Wait for the results to be visible (Look for 'Status :' text)
    # This ensures the new page has actually loaded
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Status')]")))


    # B. Helper function to safely get text
    def get_text_by_xpath(xpath):
        try:
            return driver.find_element(By.XPATH, xpath).text.strip()
        except:
            return "Not Found"


    # --- Extracting Specific Fields ---

    # 1. Header (Case Title/Number) - Usually in green or centered
    # We look for the main header text often found in a span with green color style or bold class
    case_header = get_text_by_xpath("//span[contains(@style,'color:green') or contains(@class, 'header')]")
    if case_header == "Not Found":
        # Fallback: Try grabbing the first centered text in the results area
        case_header = get_text_by_xpath("//div[@id='show_filing']//center")

    # 2. Status
    # Locates the label 'Status :' and gets the text immediately following it
    status = get_text_by_xpath("//*[contains(text(),'Status :')]/parent::*")

    # 3. CNR Number
    cnr_no = get_text_by_xpath("//*[contains(text(),'CNR No')]/parent::*")

    # 4. Petitioner Name
    # This is usually in a table. We find the "Petitioner Name" header and grab the row content.
    petitioner_info = get_text_by_xpath("//td[contains(text(), 'Petitioner Name')]/ancestor::table[1]")

    # 5. Respondent Name
    respondent_info = get_text_by_xpath("//td[contains(text(), 'Respondent Name')]/ancestor::table[1]")

    # 6. Judges / Hon'ble Judges
    decided_by = get_text_by_xpath("//*[contains(text(),'Decided By') or contains(text(),'Hon')]/parent::*")

    # -------------------------------
    # 5. PRINT OUTPUT
    # -------------------------------
    print("-" * 40)
    print(f"📄 CASE HEADER: {case_header}")
    print(f"📊 STATUS:      {status}")
    print(f"🔢 CNR NO:      {cnr_no}")
    print(f"⚖️  JUDGES:      {decided_by}")
    print("-" * 40)
    print("👤 PETITIONER DETAILS:\n", petitioner_info)
    print("-" * 40)
    print("🏛️  RESPONDENT DETAILS:\n", respondent_info)
    print("-" * 40)

except Exception as e:
    print(f"❌ An error occurred: {e}")

finally:
    # Keep browser open for a few seconds to inspect, then close
    print("Done. Closing in 10 seconds...")
    time.sleep(10)
    driver.quit()