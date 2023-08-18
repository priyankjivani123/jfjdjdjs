from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = '6427377780:AAGdcQ65KC2Oq7fFR7fJQp6uLMU9EdawOt0'

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(f"Hi {user.first_name}!")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register the start command handler
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    