from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from handler import Handler


token = "1385661797:AAEHQRLhai0GBRKT82nv265wcLBjtFYP53M"
updater = Updater(token, use_context=True)


dp = updater.dispatcher
dp.add_handler(CommandHandler("start", Handler.start))
dp.add_handler(CommandHandler("reload", Handler.reload))
dp.add_handler(ConversationHandler(entry_points=[MessageHandler(Filters.regex('Конвертировать'), Handler.converter_start)],
                                   states={},
                                   fallbacks=[]))
dp.add_handler(MessageHandler(Filters.all, Handler.all_message))

updater.start_polling()
updater.idle()
