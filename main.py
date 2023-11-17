from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update: Update, context) -> start:
    context.bot.send_message(chat_id=update.effective_chat.id, text="Kalkulyator botiga xush kelibsiz!")

def calculate(update: Update, context) -> None:
    expression = update.message.text.replace('/calculate', '')
    try:
        result = eval(expression)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Result: {result}")
    except Exception:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid expression.")

def main() -> None:
    updater = Updater(token="YOUR_BOT_TOKEN", use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    calculate_handler = MessageHandler(Filters.text & (~Filters.command), calculate)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(calculate_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
```

Replace "6984840051:AAE-DsveKqhlK6gnT915iYxrfqcS9MLuRZg" with the actual bot token you obtained from BotFather.

python bot.py
```

Your bot is now active on Telegram. You can search for your bot on Telegram and start using the calculator functionality. Send a message in the format `/calculate <expression>` to the bot, and it will evaluate the expression and reply with the result. For example, sending `/calculate 2+2` will yield a response of `Result: 4`.