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
    course_markup_btn1 = KeyboardButton('RUS → USD')
    course_markup_btn2 = KeyboardButton('RUS → EUR')
    course_markup_btn3 = KeyboardButton('RUS → CHF')
    course_markup_btn4 = KeyboardButton('RUS → TRY')
    course_markup_btn5 = KeyboardButton('RUS → JPY')
    course_markup_btn6 = KeyboardButton('RUS → BTC')
    course_markup = ReplyKeyboardMarkup([[course_markup_btn1, course_markup_btn2, course_markup_btn3],
                                         [course_markup_btn4, course_markup_btn5, course_markup_btn6],
                                         ['↺', 'Назад']], resize_keyboard=True)
    return course_markup


def re_second_markup():
    rewrite_course_btn1 = KeyboardButton('USD → RUS')
    rewrite_course_btn2 = KeyboardButton('EUR → RUS')
    rewrite_course_btn3 = KeyboardButton('CHF → RUS')
    rewrite_course_btn4 = KeyboardButton('TRY → RUS')
    rewrite_course_btn5 = KeyboardButton('JPY → RUS')
    rewrite_course_btn6 = KeyboardButton('BTC → RUS')
    rewrite_course = ReplyKeyboardMarkup([[rewrite_course_btn1, rewrite_course_btn2, rewrite_course_btn3],
                                         [rewrite_course_btn4, rewrite_course_btn5, rewrite_course_btn6],
                                         ['↺', 'Назад']], resize_keyboard=True)
    return rewrite_course
