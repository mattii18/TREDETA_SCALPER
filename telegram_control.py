# telegram_control.py
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Ustawienia tokena i ID (w razie potrzeby dynamicznie wczytywane z configu)
TELEGRAM_TOKEN = "7600816191:AAHglqWYgD2aVfiCba6m6m6qS3_aG-prlXQ"
CHAT_ID = "6673294456"

# Zmienna globalna do przechowywania aktywnego trybu
current_mode = "auto"  # "auto" lub nazwa konkretnego instrumentu

# Obsługa wiadomości z Telegrama
async def handle_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_mode
    text = update.message.text.strip().lower()

    if text in ["reszta", "all", "auto"]:
        current_mode = "auto"
        await update.message.reply_text("🔁 Tryb automatyczny: inwestuję we wszystkie instrumenty.")
    elif text in ["us100", "us500", "de40", "oil", "natgas", "cocoa", "coffee"]:
        current_mode = text
        await update.message.reply_text(f"🎯 Tryb selektywny: inwestuję tylko w {text.upper()}.")
    else:
        await update.message.reply_text("❓ Nieznana komenda. Podaj np. `cocoa`, `us100` lub `reszta`.")

# Uruchomienie bota
async def run_telegram_listener():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_command))
    await app.run_polling()

# Funkcja do pobrania aktualnego trybu dla decision_engine
def get_current_mode():
    return current_mode
