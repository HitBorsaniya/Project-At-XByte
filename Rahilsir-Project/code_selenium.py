from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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
case_detail = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//b[normalize-space()='CASE DETAIL']/ancestor::a")
    )
)

# JS click (safer for govt sites)
driver.execute_script("arguments[0].click();", case_detail)

# -------------------------------
# Confirm Case Detail section loaded
# -------------------------------
wait.until(
    EC.presence_of_element_located((By.ID, "case_type"))
)

print("✅ CASE DETAIL page loaded successfully")

time.sleep(5)
# driver.quit()
