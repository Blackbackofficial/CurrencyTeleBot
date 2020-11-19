from telegram import ReplyKeyboardMarkup
from telegram import KeyboardButton


def first_markup():
    first_markup_btn1 = KeyboardButton('Конвертировать🔄')
    first_markup_btn2 = KeyboardButton('Курс📈')
    first_markup_btn3 = KeyboardButton('Закрыть')
    base_markup = ReplyKeyboardMarkup([[first_markup_btn1, first_markup_btn2], [first_markup_btn3]],
                                      resize_keyboard=True)
    return base_markup


def second_markup():
    rewrite_course_btn1 = KeyboardButton('USD → RUB')
    rewrite_course_btn2 = KeyboardButton('EUR → RUB')
    rewrite_course_btn3 = KeyboardButton('CHF → RUB')
    rewrite_course_btn4 = KeyboardButton('TRY → RUB')
    rewrite_course_btn5 = KeyboardButton('JPY → RUB')
    rewrite_course_btn6 = KeyboardButton('BTC → RUB')
    rewrite_course = ReplyKeyboardMarkup([[rewrite_course_btn1, rewrite_course_btn2, rewrite_course_btn3],
                                          [rewrite_course_btn4, rewrite_course_btn5, rewrite_course_btn6],
                                          ['↺', 'Назад']], resize_keyboard=True)
    return rewrite_course


def re_second_markup():
    course_markup_btn1 = KeyboardButton('RUB → USD')
    course_markup_btn2 = KeyboardButton('RUB → EUR')
    course_markup_btn3 = KeyboardButton('RUB → CHF')
    course_markup_btn4 = KeyboardButton('RUB → TRY')
    course_markup_btn5 = KeyboardButton('RUB → JPY')
    course_markup_btn6 = KeyboardButton('RUB → BTC')
    course_markup = ReplyKeyboardMarkup([[course_markup_btn1, course_markup_btn2, course_markup_btn3],
                                         [course_markup_btn4, course_markup_btn5, course_markup_btn6],
                                         ['↺', 'Назад']], resize_keyboard=True)
    return course_markup
