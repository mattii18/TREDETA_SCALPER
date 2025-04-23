import time
import threading
import pandas as pd
from telegram_bot import start_telegram_bot, bot_status, send_message
from core import decision_engine
from xtb_webdriver import XTBWebDriver

#Start przeglądarki XTB
xtb = XTBWebDriver()
xtb.start_browser()

# Symulacja danych (normalnie tutaj byłby realny wykres)
def get_mock_data():
    data = {
        'open': [100, 102, 101, 103, 102],
        'high': [102, 103, 104, 105, 106],
        'low': [99, 101, 100, 102, 101],
        'close': [101, 102, 103, 104, 105]
    }
    return pd.DataFrame(data)

def trading_loop():
    while bot_status["running"]:
        if bot_status["mode"] == "off":
            time.sleep(5)
            continue

        if bot_status["mode"] == "single_instrument":
            instrument = bot_status["instrument"]
            capital = bot_status["capital_percent"] or "Standard"

            df = get_mock_data()
            decision = decision_engine.run_decision_engine(df)

            if decision == 'BUY':
                send_message(f"ScalperX: Otwieram pozycję BUY na {instrument} ({capital})")
            elif decision == 'SELL':
                send_message(f"ScalperX: Otwieram pozycję SELL na {instrument} ({capital})")
            else:
                send_message(f"ScalperX: Brak sygnału na {instrument} ({capital})")

        elif bot_status["mode"] == "auto":
            send_message("ScalperX: Analizuję wszystkie instrumenty... (symulacja)")
        
        time.sleep(10) # Odstęp między analizami

if __name__ == "__main__":
    threading.Thread(target=start_telegram_bot).start()
    trading_loop()