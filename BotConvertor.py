from pip._vendor import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Привет, я Ваня и я расскажу тебе что там по курсу")


def all_message(update, context):
    chat = update.effective_chat
    text = update.message.text
    try:
        money = float(text)
        requestsCB = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
        money = money * requestsCB['Valute']['USD']['Value']
        context.bot.send_message(chat_id=chat.id, text=str(money))
    except:
        context.bot.send_message(chat_id=chat.id, text="Напишите число для перевода!")


token = "1385661797:AAEHQRLhai0GBRKT82nv265wcLBjtFYP53M"
updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
# dispatcher.add_handler(CommandHandler("stop", stop))
dispatcher.add_handler(MessageHandler(Filters.all, all_message))

updater.start_polling()
updater.idle()
