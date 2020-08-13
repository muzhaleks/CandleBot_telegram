from mybot.bot import bot
from mybot.candles_pic import *
from mybot.keyboards import *
from mybot.messages import *


@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.send_message(message.chat.id, message.from_user.first_name + HELLO_MESSAGE, reply_markup=keyboard_for_page_one)


@bot.message_handler(content_types=['text'])
def send_text(message):
    text = 'Найдём нужное?'
    back = 'Возвращаемся назад...'
    if message.text.lower() == 'перемены в жизни':
        bot.send_message(message.chat.id, text, reply_markup=keyboard_for_page_two)
    elif message.text.lower() == 'очищение/чистка':
        bot.send_message(message.chat.id, text, reply_markup=keyboard_for_page_three)
    elif message.text.lower() == 'эмоциональная стабилизация':
        bot.send_message(message.chat.id, text, reply_markup=keyboard_for_page_four)
    elif message.text.lower() == 'любовь/отношения':
        bot.send_message(message.chat.id, text, reply_markup=keyboard_for_page_five)
    elif message.text.lower() == 'финансы':
        bot.send_message(message.chat.id, text, reply_markup=keyboard_for_page_six)
    elif message.text.lower() == 'связаться с мастером':
        bot.send_contact(message.chat.id, MASTER_PHONE, MASTER_NAME)
    elif message.text.lower() == 'назад':
        bot.send_message(message.chat.id, back, reply_markup=keyboard_for_page_one)
    elif message.text.lower() == 'перезагрузка реальности':
        bot.send_photo(message.chat.id, REALITY_RESTART_PIC)
        bot.send_message(message.chat.id, REALITY_RESTART)
    elif message.text.lower() == 'исполнение желаний':
        bot.send_photo(message.chat.id, WISH_SET_PIC)
        bot.send_message(message.chat.id, WISH_SET)
    elif message.text.lower() == 'свеча-прорыв':
        bot.send_photo(message.chat.id, BREAKTHROUGH_CANDLE_PIC)
        bot.send_message(message.chat.id, BREAKTHROUGH_CANDLE)
    elif message.text.lower() == 'полынный сет':
        bot.send_photo(message.chat.id, POLYN_SET_PIC)
        bot.send_message(message.chat.id, POLYN_SET)
    elif message.text.lower() == 'универсальная чистка':
        bot.send_photo(message.chat.id, CLEAR_SET_PIC)
        bot.send_message(message.chat.id, CLEAR_SET)
    elif message.text.lower() == 'в разработке':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJXcV6ljcfnctqSkey5SBKG6Qo1XEQ3AAKoAAPMVEkJBk94075aEAMZBA')
        bot.send_message(message.chat.id, 'Скоро здесь что-то будет)))')
    elif message.text.lower() == 'успокоение':
        bot.send_photo(message.chat.id, KEEP_CALM_PIC)
        bot.send_message(message.chat.id, KEEP_CALM_CANDLE)
    elif message.text.lower() == 'молитва':
        bot.send_photo(message.chat.id, STRONGER_PRAY_CANDLE_PIC)
        bot.send_message(message.chat.id, STRONGER_PRAY_CANDLE)
    elif message.text.lower() == 'от тяжких дум':
        bot.send_photo(message.chat.id, LIGHT_MY_MIND_SET_PIC)
        bot.send_message(message.chat.id, LIGHT_MY_MIND_SET)
    elif message.text.lower() == 'сладкая парочка':
        bot.send_photo(message.chat.id, SWEET_COUPLE_SET_PIC)
        bot.send_message(message.chat.id, SWEET_COUPLE_SET)
    elif message.text.lower() == 'привлечение любви':
        bot.send_photo(message.chat.id, LOVE_MAKE_CANDLE_PIC)
        bot.send_message(message.chat.id, LOVE_MAKE_CANDLE)
    elif message.text.lower() == 'гармонизация отношений':
        bot.send_photo(message.chat.id, LOVE_HARMONISATION_SET_PIC)
        bot.send_message(message.chat.id, LOVE_HARMONISATION_SET)
    elif message.text.lower() == 'денежная':
        bot.send_photo(message.chat.id, GIVE_ME_MONEY_CANDLE_PIC)
        bot.send_message(message.chat.id, GIVE_ME_MONEY_CANDLE)
    elif message.text.lower() == 'чистка фин.потока':
        bot.send_photo(message.chat.id, CLEAN_MY_MONEY_PIC)
        bot.send_message(message.chat.id, CLEAN_MY_MONEY)
    elif message.text.lower() == 'финансовый успех':
        bot.send_photo(message.chat.id, FINANCIAL_SUCCESS_SET_PIC)
        bot.send_message(message.chat.id, FINANCIAL_SUCCESS_SET)


if __name__ == '__main__':
    bot.polling(none_stop=True)
