import time
import json
import datetime
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
    full_case_type_text = ""
    for option in case_type_dropdown.options:
        if option.text.strip().lower().startswith(CASE_CODE_PREFIX):
            case_type_dropdown.select_by_visible_text(option.text)
            full_case_type_text = option.text  # Store for JSON
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

    # 5. SCRAPE DATA
    print("⏳ Waiting for results to load...")
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Status')]")))


    # Helper function to clean text
    def get_text(xpath):
        try:
            return driver.find_element(By.XPATH, xpath).text.strip()
        except:
            return ""


    # --- EXTRACTION LOGIC ---

    # 1. Status
    raw_status = get_text("//*[contains(text(),'Status :')]/parent::*").replace("Status :", "").strip()

    # 2. Dates (Disposal or Next Hearing)
    disposal_date = get_text("//*[contains(text(),'Disposal Date:')]/parent::*").replace("Disposal Date:", "").strip()

    # 3. CNR
    cnr_no = get_text("//*[contains(text(),'CNR No')]/parent::*").replace("CNR No :", "").strip()

    # 4. Petitioner & Respondent
    # Note: These are in tables, we try to grab the first row name
    petitioner_table = get_text("//td[contains(text(), 'Petitioner Name')]/ancestor::table[1]")
    respondent_table = get_text("//td[contains(text(), 'Respondent Name')]/ancestor::table[1]")

    # Clean up names (Basic logic: split by new line and take the 2nd line which is usually the name)
    p_lines = petitioner_table.split('\n')
    r_lines = respondent_table.split('\n')

    # Trying to find the name after the header
    petitioner_name = p_lines[1] if len(p_lines) > 1 else "Unknown"
    respondent_name = r_lines[1] if len(r_lines) > 1 else "Unknown"

    # 5. Judges
    judges = get_text("//*[contains(text(),'Decided By') or contains(text(),'Hon')]/parent::*").replace("Decided By:",
                                                                                                        "").strip()

    # -------------------------------
    # 6. BUILD JSON OBJECT
    # -------------------------------

    # We construct the dictionary using the structure you requested
    case_data = {
        "Court Name": "HIGH COURT OF GUJARAT",
        "Case Type/Case Number/Case Year": f"{full_case_type_text}/{CASE_NUMBER}/{CASE_YEAR}",
        "Case Number": int(CASE_NUMBER),
        "Case Year": int(CASE_YEAR),
        "Petitioner Name versus Respondent Name": f"{petitioner_name} Vs {respondent_name}",
        "case_status/case_stage": raw_status,
        "Decision Date / Next Hearing Date / Next Date": disposal_date,
        "Hash id": cnr_no,  # Mapping CNR to Hash ID as per your example
        "State": "Gujarat",
        "Hon'ble Judges": judges,
        "Update Time": datetime.datetime.now().strftime("%Y_%m_%d_%H_%M"),
        "crawling_status": 1
    }

    # -------------------------------
    # 7. OUTPUT RESULT
    # -------------------------------
    print("\n" + "=" * 50)
    print("📊 FINAL JSON DATA")
    print("=" * 50)

    # Print as formatted JSON string
    print(json.dumps(case_data, indent=4, default=str))
    print("=" * 50)

except Exception as e:
    print(f"❌ Error: {e}")

finally:
    print("Closing browser...")
    driver.quit()