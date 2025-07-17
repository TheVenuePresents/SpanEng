from telegram.ext import Updater, MessageHandler, Filters
from googletrans import Translator
import os

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

translator = Translator()

def translate(update, context):
    text = update.message.text
    try:
        detected = translator.detect(text)
        if detected.lang == 'es':
            translated = translator.translate(text, src='es', dest='en')
            reply = f"🇪🇸 Spanish → 🇺🇸 English:\n{translated.text}"
        elif detected.lang == 'en':
            translated = translator.translate(text, src='en', dest='es')
            reply = f"🇺🇸 English → 🇪🇸 Spanish:\n{translated.text}"
        else:
            reply = "❌ Only Spanish and English are supported."
    except Exception as e:
        reply = f"⚠️ Error: {str(e)}"

    update.message.reply_text(reply)

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, translate))
    updater.start_polling()
    print("Bot is running...")
    updater.idle()

if __name__ == '__main__':
    main()
