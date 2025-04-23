from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class XTBWebDriver:
    def __init__(self):
        self.driver = None

    def start_browser(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        # Na serwerze użyjemy: options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service('chromedriver.exe'), options=options)
        self.driver.get("https://xstation5.xtb.com")
        print("Przeglądarka uruchomiona. Zaloguj się ręcznie do XTB...")

        # Czekamy aż użytkownik się zaloguje (np. wykrycie panelu po zalogowaniu)
        self.wait_for_login()

    def wait_for_login(self):
        # Czekamy aż pojawi się element widoczny tylko po zalogowaniu
        while True:
            try:
                # Przykładowy selektor – trzeba dostosować po testach!
                if self.driver.find_element(By.ID, "mainChartContainer"):
                    print("Zalogowano! ScalperX przejmuje kontrolę.")
                    break
            except:
                pass
            time.sleep(2)

    def click_buy(self):
        try:
            buy_button = self.driver.find_element(By.CLASS_NAME, "tradeButtonBuy")  # Przykładowy selektor
            buy_button.click()
            print("Kliknięto BUY")
        except:
            print("Nie znaleziono przycisku BUY")

    def click_sell(self):
        try:
            sell_button = self.driver.find_element(By.CLASS_NAME, "tradeButtonSell")
            sell_button.click()
            print("Kliknięto SELL")
        except:
            print("Nie znaleziono przycisku SELL")

    def click_close(self):
        try:
            close_button = self.driver.find_element(By.CLASS_NAME, "closePositionButton")
            close_button.click()
            print("Kliknięto ZAMKNIJ")
        except:
            print("Nie znaleziono przycisku ZAMKNIJ")

    def stop(self):
        self.driver.quit()
        print("Przeglądarka zamknięta.")