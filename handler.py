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
        if self.message.text in const.CURRENCY:
            if not self.message.text == '↺' and not self.message.text == 'Назад':
                context.user_data['currency'] = self.message.text.replace(" → ", "")
                self.message.reply_text("Напишите число для перевода!")
                return "value"
            elif self.message.text == 'Назад':
                Handler.all_message(self, context)
                Handler.return_flag = True
                return ConversationHandler.END
            else:
                Handler.all_message(self, context)
        else:
            self.message.reply_text("Вы не выбрани ни одной кнопки!")

    def convertor_value(self, context):
        try:
            if self.message.text == 'Назад':
                Handler.all_message(self, context)
                Handler.return_flag = True
                return ConversationHandler.END
            value = context.user_data['value'] = float(self.message.text)
            chat = self.effective_chat
            requestsCB = requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&interval=1'
                                      'min&apikey=UWFL45VWBLIXSZD3'.format(context.user_data['currency'])).json()
            value = value * float(requestsCB['Global Quote']['05. price'])
            context.bot.send_message(chat_id=chat.id, text=str(value), reply_markup=first_markup())
            return ConversationHandler.END
        except ValueError:
            self.message.reply_text("Вы меня сломали!", reply_markup=first_markup())
            return ConversationHandler.END
