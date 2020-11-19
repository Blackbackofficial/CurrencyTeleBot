from markups import first_markup, second_markup, re_second_markup
from telegram.ext import ConversationHandler
from telegram import ReplyKeyboardRemove
import requests
import random
import const


class Handler:
    return_flag = True

    def __init__(self):
        self.message = None
        self.effective_chat = None

    # Handlers
    def start(self, context):
        chat = self.effective_chat
        self.message.reply_text(
            "Привет {}, мне еще не дали имени, я расскажу тебе что там с курсом".format(chat.first_name),
            reply_markup=first_markup())

    def reload(self, context):
        self.message.reply_text(random.choice(const.ANSWERS_RELOAD), reply_markup=first_markup())

    def all_message(self, context):
        msg = self.message.text
        if msg == 'Закрыть':
            self.message.reply_text('Если я понадоблюсь нажми /reload', reply_markup=ReplyKeyboardRemove())
        elif msg == 'Назад':
            self.message.reply_text("Выберете что-то одно", reply_markup=first_markup())
        elif msg == '↺':
            if Handler.return_flag:
                self.message.reply_text("Выберете валюту.", reply_markup=re_second_markup())
            else:
                self.message.reply_text("Выберете валюту.", reply_markup=second_markup())
            Handler.return_flag = not Handler.return_flag
        else:
            self.message.reply_text(random.choice(const.ANSWERS_ERRORS))


class Convertor(Handler):

    def convertor_start(self, context):
        self.message.reply_text("Во что бы вы хотели перевести?", reply_markup=second_markup())
        return "currency"

    def convertor_currency(self, context):
        if not self.message.text == '↺' and 'Назад':
            context.user_data['currency'] = self.message.text.replace(" → ", "")
            # context.user_data['currency'] = ' '.join(context.user_data['currency'].split(' ')[::-1]).replace(" ", "")
            self.message.reply_text("Напишите число для перевода!")
            return "value"
        elif self.message.text == 'Назад':
            Handler.all_message(self, context)
            Handler.return_flag = True
            return ConversationHandler.END
        else:
            Handler.all_message(self, context)

    def convertor_value(self, context):
        if self.message.text == 'Назад' and '↺':
            Handler.all_message(self, context)
            Handler.return_flag = True
            return ConversationHandler.END
        value = context.user_data['value'] = float(self.message.text)
        chat = self.effective_chat
        try:
            requestsCB = requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&interval=1'
                                      'min&apikey=UWFL45VWBLIXSZD3'.format(context.user_data['currency'])).json()
            value = value * float(requestsCB['Global Quote']['05. price'])
            context.bot.send_message(chat_id=chat.id, text=str(value) + '$', reply_markup=first_markup())
            return ConversationHandler.END
        except:
            context.bot.send_message(chat_id=chat.id, text="Напишите число для перевода!")
