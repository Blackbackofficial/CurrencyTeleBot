from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from functional.handler import Handler, Convertor
from functional.course import Course
import const


updater = Updater(const.TOKEN, use_context=True)
dp = updater.dispatcher


def main():
    dp.add_handler(CommandHandler("start", Handler.start))
    dp.add_handler(CommandHandler("reload", Handler.reload))
    dp.add_handler(
        ConversationHandler(entry_points=[MessageHandler(Filters.regex('Конвертировать'), Convertor.convertor_start)],
                            states={
                                "currency": [MessageHandler(Filters.text, Convertor.convertor_currency)],
                                "value": [MessageHandler(Filters.text, Convertor.convertor_value)]
                            }, fallbacks=[]))
    dp.add_handler(
        ConversationHandler(entry_points=[MessageHandler(Filters.regex('Курс'), Course.start_course)],
                            states={"currency": [MessageHandler(Filters.text, Course.enter_currency)]}, fallbacks=[]))
    dp.add_handler(MessageHandler(Filters.all, Handler.all_message))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
