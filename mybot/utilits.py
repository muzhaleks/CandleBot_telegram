from telebot import types


def generate_keyboard(*answer):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for item in answer:
        button = types.KeyboardButton(item)
        keyboard.add(button)
    return keyboard
