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
    course_markup_btn1 = KeyboardButton('₽ → $')
    course_markup_btn2 = KeyboardButton('₽ → €')
    course_markup_btn3 = KeyboardButton('₽ → ₣')
    course_markup_btn4 = KeyboardButton('₽ → ₺')
    course_markup_btn5 = KeyboardButton('₽ → ¥')
    course_markup_btn6 = KeyboardButton('₽ → ₿')
    course_markup = ReplyKeyboardMarkup([[course_markup_btn1, course_markup_btn2, course_markup_btn3],
                                         [course_markup_btn4, course_markup_btn5, course_markup_btn6],
                                         ['В обратную сторону🔃', 'Назад']], resize_keyboard=True)
    return course_markup
