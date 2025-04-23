# auto_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def login_to_xtb(email, password):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # Jeśli chcesz headless (bez okna) odkomentuj poniżej:
    # options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.get("https://xstation5.xtb.com")

    try:
        time.sleep(5)  # Czekamy na załadowanie strony

        # Znajdujemy pola logowania
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")

        email_field.send_keys(email)
        password_field.send_keys(password)

        # Klikamy przycisk logowania
        login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Log in")]')
        login_button.click()

        print("✅ Zalogowano do XTB!")

        time.sleep(10)  # Czekamy na pełne załadowanie platformy
        return driver  # Zwracamy driver do dalszej pracy bota

    except Exception as e:
        print(f"❌ Błąd logowania: {e}")
        driver.quit()
        return None
