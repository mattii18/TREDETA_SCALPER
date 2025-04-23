# core/login_bot.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import json


def login_to_xtb(email, password):
    options = Options()
    options.add_argument("--headless")  # Możesz to usunąć, jeśli chcesz widzieć co się dzieje
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.get("https://xstation5.xtb.com")

    time.sleep(5)  # Czekamy na załadowanie strony

    try:
        email_input = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        email_input.send_keys(email)

        password_input = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)

        print("✅ Zalogowano pomyślnie do XTB.")
        return driver
    except Exception as e:
        print(f"❌ Błąd logowania: {e}")
        driver.quit()
        return None


if __name__ == "__main__":
    with open("config.json") as f:
        config = json.load(f)
    login_to_xtb(config["xtb_email"], config["xtb_password"])
