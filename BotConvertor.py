from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from handler import Handler
import const


updater = Updater(const.TOKEN, use_context=True)
dp = updater.dispatcher


def main():
    dp.add_handler(CommandHandler("start", Handler.start))
    dp.add_handler(CommandHandler("reload", Handler.reload))
    dp.add_handler(
        ConversationHandler(entry_points=[MessageHandler(Filters.regex('Конвертировать'), Handler.converter_start)],
                            states={},
                            fallbacks=[]))
    dp.add_handler(MessageHandler(Filters.all, Handler.all_message))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
