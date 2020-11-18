import random
from pip._vendor import requests
from telegram import ReplyKeyboardRemove
from markups import first_markup, second_markup


class Handler:
    # Answers
    answers_reload = ['Что-то подсказать?', 'Духи не знают усталости.', 'Опять работа?!', 'Вам меня не жалко?',
                      'Если смертные достают, то достают до смерти, спрашивай', 'Не буди во мне зверя.', 'Да, что хотел?']
    answers_error = ['Когда-нибудь я научусь понимать ваш язык, но видимо это будет не скоро.', 'Уххх, мне не очень понятно.',
                     'Преобразую буквы в цыфры... \nУпс, что-то пошло не так.', 'Я еще не настолько умный, но спасибо что так считаешь.',
                     'А? Я не силен в семиотике. В институте она не нравилась.', 'Какой же толстый этот словарь Ожегова.',
                     'Ненавижу эту работу, повтори еще раз.', 'Я знаю Python, и команды ниже, попробуй еще разок.']

    def __init__(self):
        self.message = None
        self.effective_chat = None

    # Handlers
    def start(self, context):
        chat = self.effective_chat
        context.bot.send_message(chat_id=chat.id,
                                 text="Привет, мне еще не дали имени, я расскажу тебе что там с курсом",
                                 reply_markup=first_markup())

    def converter_start(self, context):
        chat = self.effective_chat
        context.bot.send_message(chat_id=chat.id, text="Во что бы вы хотели перевести?", reply_markup=second_markup())

    async def converter(self, context):
        chat = self.effective_chat
        text = self.message.text
        context.bot.send_message(chat_id=chat.id, text="Напишите число для перевода!")
        try:
            money = float(text)
            requestsCB = requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE'
                                      '&symbol=EURRUB&interval=1min&apikey=UWFL45VWBLIXSZD3').json()
            money = money * float(requestsCB['Global Quote']['05. price'])
            context.bot.send_message(chat_id=chat.id, text=str(money) + '$')
        except:
            context.bot.send_message(chat_id=chat.id, text="Напишите число для перевода!")

    def reload(self, context):
        self.message.reply_text(random.choice(Handler.answers_reload), reply_markup=first_markup())

    def all_message(self, context):
        msg = self.message.text
        if msg == 'Закрыть':
            self.message.reply_text('Если я понадоблюсь нажми /reload', reply_markup=ReplyKeyboardRemove())
        elif msg == 'Назад':
            self.message.reply_text("Выберете что-то одно", reply_markup=first_markup())
        else:
            self.message.reply_text(random.choice(Handler.answers_error))
