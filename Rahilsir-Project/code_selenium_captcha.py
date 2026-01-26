import io
import time
import numpy as np
import easyocr
from PIL import Image, ImageSequence
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# -------------------------------
# YOUR CAPTCHA SOLVER FUNCTION
# -------------------------------
def captcha_easy_ocr(image_bytes):
    """
    Takes image bytes, converts to numpy array, and runs EasyOCR.
    """
    print("🧠 Initializing EasyOCR (this may take a moment)...")
    # Initialize reader (gpu=False if you don't have CUDA setup, safer for general compatibility)
    reader = easyocr.Reader(['en'], gpu=False)

    captcha_text = ''
    try:
        gif = Image.open(io.BytesIO(image_bytes))

        # Iterate through frames (works for static images too, usually just 1 frame)
        for i, frame in enumerate(ImageSequence.Iterator(gif)):
            frame = frame.convert("RGB")
            frame_array = np.array(frame)

            # Read text
            frame_text = reader.readtext(frame_array)

            # Extract text if found
            if frame_text:
                # frame_text is a list of tuples, we want the text part [1] of the first result [0]
                text_found = frame_text[0][1]

                # clean the text
                clean_text = str(text_found).replace(' ', '').replace(':', '').strip()

                if clean_text:
                    captcha_text = clean_text
                    print(f"   Frame {i} Text Found: {captcha_text}")
                    # If we found a good candidate, we can often break, or let it loop to find better ones
                    # For this specific site, usually the first read is sufficient.
                    break
    except Exception as e:
        print(f"⚠️ OCR Error: {e}")

    return captcha_text


# -------------------------------
# BROWSER SETUP
# -------------------------------
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless") # Uncomment to run in background

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)
wait = WebDriverWait(driver, 30)

try:
    # 1. Open Site
    driver.get("https://gujarathc-casestatus.nic.in/gujarathc/")
    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

    # 2. Navigate to Case Detail
    case_detail = wait.until(
        EC.presence_of_element_located((By.XPATH, "//b[normalize-space()='CASE DETAIL']/ancestor::a")))
    driver.execute_script("arguments[0].click();", case_detail)

    # Wait for form
    wait.until(EC.presence_of_element_located((By.ID, "casefr")))
    print("✅ Page loaded.")

    # 3. Fill Form Fields
    # Select Case Mode 'r'
    case_mode = Select(driver.find_element(By.ID, "casefr"))
    for opt in case_mode.options:
        if opt.text.strip().lower().startswith("r"):
            case_mode.select_by_visible_text(opt.text)
            break

    time.sleep(2)  # Allow refresh

    # Select Case Type 'cr.ma'
    case_type = Select(driver.find_element(By.ID, "casetype"))
    for opt in case_type.options:
        if opt.text.strip().lower().startswith("cr.ma"):
            case_type.select_by_visible_text(opt.text)
            break

    # Enter Number & Year
    driver.find_element(By.ID, "casenumber").send_keys("7510")
    driver.find_element(By.ID, "caseyear").send_keys("2016")

    # -------------------------------
    # 4. SOLVE CAPTCHA AUTOMATICALLY
    # -------------------------------
    print("📷 Capturing CAPTCHA image...")

    # Locate the CAPTCHA image.
    # Based on site structure, it's usually inside the div with id='captcha_image' or similar.
    # We look for the image tag that is NOT the refresh button.
    captcha_img_element = driver.find_element(By.XPATH, "//img[@id='stringCaptcha']")

    # Take screenshot of JUST the element
    captcha_screenshot = captcha_img_element.screenshot_as_png

    # Send to your OCR function
    solved_text = captcha_easy_ocr(captcha_screenshot)
    print(f"🤖 OCR Solution: {solved_text}")

    if not solved_text:
        print("❌ OCR failed to read text. Exiting.")
        exit()

    # Enter the solved text
    # Finding the input box (usually just below or next to image)
    # Based on your first screenshot, the input is next to the image with name/id that likely contains 'captcha'
    # Searching for the input type='text' in that same area or by specific ID if known
    # Usually ID is "captchaval" or similar. We'll use a generic robust search:
    captcha_input = driver.find_element(By.XPATH,
                                        "//input[@type='text' and (contains(@id, 'code') or contains(@name, 'code') or @maxlength='6')]")

    captcha_input.clear()
    captcha_input.send_keys(solved_text)

    # Click GO
    go_btn = driver.find_element(By.ID, "go")  # usually ID is 'go' or 'submit'
    driver.execute_script("arguments[0].click();", go_btn)

    # -------------------------------
    # 5. SCRAPE RESULTS
    # -------------------------------
    print("⏳ Waiting for results...")

    # Wait for 'Status' text to appear
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Status')]")))
    print("✅ Results loaded successfully!")


    # --- Scraping Logic ---
    def get_text(xpath):
        try:
            return driver.find_element(By.XPATH, xpath).text.strip()
        except:
            return "Not Found"


    status = get_text("//*[contains(text(),'Status :')]/parent::*")
    petitioner = get_text("//td[contains(text(), 'Petitioner Name')]/ancestor::table[1]")
    respondent = get_text("//td[contains(text(), 'Respondent Name')]/ancestor::table[1]")

    print("\n" + "=" * 40)
    print(f"RESULTS FOR {solved_text}")
    print("=" * 40)
    print(f"STATUS: {status}")
    print("-" * 40)
    print("PETITIONER:\n", petitioner)
    print("-" * 40)
    print("RESPONDENT:\n", respondent)
    print("=" * 40)

except Exception as e:
    print(f"❌ Error: {e}")
    # Optional: Take a screenshot if it fails
    driver.save_screenshot("error_debug.png")

finally:
    # driver.quit()
    pass