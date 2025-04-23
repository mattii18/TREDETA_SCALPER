import requests
import time
import threading

TOKEN = '7600816191:AAHglqWYgD2aVfiCba6m6m6qS3_aG-prlXQ'
CHAT_ID = '6673294456'
API_URL = f"https://api.telegram.org/bot{TOKEN}"

INSTRUMENTS = ['COCOA', 'COFFEE', 'US100', 'US500', 'DE40', 'OIL.WTI', 'NATGAS']

bot_status = {
    "mode": "auto",
    "instrument": None,
    "capital_percent": None,
    "running": True
}

def send_message(text):
    data = {'chat_id': CHAT_ID, 'text': text}
    requests.post(f"{API_URL}/sendMessage", data=data)

def get_updates(offset=None):
    params = {'timeout': 100, 'offset': offset}
    response = requests.get(f"{API_URL}/getUpdates", params=params)
    return response.json()

def handle_command(command):
    cmd = command.upper().strip()
    
    if cmd == 'HELP':
        send_message(
            "ScalperX Komendy:\n"
            "- COCOA / US100 / ... : Inwestuj tylko w dany instrument\n"
            "- COCOA 70% : Inwestuj % kapitału\n"
            "- RESZTA : Powrót do automatyki\n"
            "- OFF : Zatrzymaj po zamknięciu pozycji\n"
            "- ON : Wznów pracę\n"
            "- STATUS : Pokaż status\n"
            "- LOGI : Wyślij dziennik\n"
            "- PROFIT : Pokaż dzienny zysk\n"
            "- SHUTDOWN : Awaryjne wyłączenie"
        )

    elif cmd == 'RESZTA':
        bot_status.update({"mode": "auto", "instrument": None, "capital_percent": None})
        send_message("ScalperX: Wróciłem do automatycznej analizy wszystkich instrumentów.")

    elif cmd == 'OFF':
        bot_status["mode"] = "off"
        send_message("ScalperX: Zatrzymuję się po zamknięciu pozycji na plusie.")

    elif cmd == 'ON':
        bot_status.update({"mode": "auto", "running": True})
        send_message("ScalperX: Wznawiam automatyczne inwestowanie.")

    elif cmd == 'STATUS':
        status_msg = (
            f"ScalperX Status:\n"
            f"- Tryb: {bot_status['mode']}\n"
            f"- Instrument: {bot_status['instrument']}\n"
            f"- Kapitał: {bot_status['capital_percent'] or 'Standard'}\n"
            f"- Running: {bot_status['running']}"
        )
        send_message(status_msg)

    elif cmd == 'LOGI':
        send_message("ScalperX: Wysyłam dziennik transakcji (symulacja).")

    elif cmd == 'PROFIT':
        send_message("ScalperX: Dzisiejszy zysk: +245 PLN (symulacja).")

    elif cmd == 'SHUTDOWN':
        bot_status["running"] = False
        send_message("ScalperX: Awaryjne wyłączenie. Do zobaczenia!")

    else:
        parts = cmd.split()
        if parts[0] in INSTRUMENTS:
            instrument = parts[0]
            percent = None
            if len(parts) == 2 and parts[1].endswith('%'):
                try:
                    percent = int(parts[1].replace('%', ''))
                    if percent > 100 or percent <= 0:
                        send_message("ScalperX: Procent kapitału musi być w zakresie 1-100%.")
                        return
                except ValueError:
                    send_message("ScalperX: Nieprawidłowy format procentu.")
                    return
            bot_status.update({"mode": "single_instrument", "instrument": instrument, "capital_percent": percent})
            msg = f"ScalperX: Skupiam się na {instrument}"
            if percent:
                msg += f", inwestując {percent}% kapitału."
            else:
                msg += "."
            send_message(msg)
        else:
            send_message("ScalperX: Nie rozpoznano komendy. Wpisz HELP.")

def telegram_listener():
    send_message("ScalperX aktywny. Wpisz HELP, aby zobaczyć dostępne komendy.")
    last_update_id = None
    while bot_status["running"]:
        updates = get_updates(last_update_id)
        if "result" in updates:
            for update in updates["result"]:
                last_update_id = update["update_id"] + 1
                if "message" in update and "text" in update["message"]:
                    handle_command(update["message"]["text"])
        time.sleep(1)

def start_telegram_bot():
    listener_thread = threading.Thread(target=telegram_listener)
    listener_thread.start()