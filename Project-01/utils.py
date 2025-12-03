import random
import string
import time
from difflib import SequenceMatcher

# ------------------ AUTO FORMAT ------------------
def format_text(text):
    return " ".join(word.capitalize() for word in text.strip().split())

# ------------------ AUTO CATEGORY DETECT ------------------
def detect_category(title):
    title = title.lower()
    if "python" in title or "java" in title or "programming" in title:
        return "Programming"
    if "data" in title or "machine learning" in title:
        return "Data Science"
    if "network" in title or "security" in title:
        return "Networking"
    return "General"

# ------------------ SMART BOOK ID GENERATOR ------------------
def generate_book_id():
    year = time.strftime("%Y")
    rand = "".join(random.choices(string.digits, k=3))
    return f"BK-{year}-{rand}"

# ------------------ SIMILAR TITLE CHECK ------------------
def is_title_similar(new_title, existing_title):
    score = SequenceMatcher(None, new_title.lower(), existing_title.lower()).ratio()
    return score > 0.80

# ------------------ CAPTCHA SYSTEM ------------------
def captcha_check():
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    print(f"\nCAPTCHA: {a} + {b} = ?")
    user = int(input("Enter answer: "))
    return user == a + b

# ------------------ INPUT VALIDATOR ------------------
def validate_name(name):
    return name.replace(" ", "").isalpha()
