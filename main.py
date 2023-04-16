import telebot
from telebot import types

bot = telebot.TeleBot('6200404821:AAEiHQQAwR2gLbORrYRT42wWu4kHyCeOrKo')


@bot.message_handler(commands=['start'])
def start(message):
    m = f'Доброго времени суток, {message.from_user.first_name}'
    bot.send_message(message.chat.id, m, parse_mode='html')
    markup = types.ReplyKeyboardMarkup()
    start = types.KeyboardButton('записать съеденное')
    markup.add(start)
    bot.send_message(message.chat.id, 'Что хотите сделать?', reply_markup=markup)


@bot.message_handler()
def zapis(message):
    if message.text == 'записать съеденное':
        markup = types.ReplyKeyboardMarkup()
        zavtrak = types.KeyboardButton('завтрак')
        obed = types.KeyboardButton('обед')
        ujin = types.KeyboardButton('ужин')
        perekus = types.KeyboardButton('перекус')
        markup.add(zavtrak, obed, ujin, perekus)
        bot.send_message(message.chat.id, 'Хорошо, в какой прием пищи?', reply_markup=markup)
    elif message.text == 'завтрак':
        pass
    else:
        bot.send_message(message.chat.id, 'Извините, я так не умею')


bot.polling(none_stop=True)
