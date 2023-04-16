import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('6200404821:AAEiHQQAwR2gLbORrYRT42wWu4kHyCeOrKo')

con = sqlite3.connect('eda.db', check_same_thread=False)


@bot.message_handler(commands=['start'])
def start(message):
    m = f'Доброго времени суток, {message.from_user.first_name}'
    bot.send_message(message.chat.id, m, parse_mode='html')
    markup = types.ReplyKeyboardMarkup()
    start = types.KeyboardButton('записать съеденное')

    cur = con.cursor()
    cur.execute("""INSERT INTO users
            (name, tg_id) VALUES (?, ?)""", (message.from_user.first_name, message.from_user.id))
    cur.close()

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
    else:
        bot.send_message(message.chat.id, 'Извините, я так не умею')


@bot.message_handler()
def poest(message):
    if message.text != 'записать съеденное' and message.text in ['завтрак', 'обед', 'ужин', 'перекус']:
        pass
    else:
        bot.send_message(message.chat.id, 'Извините, я так не умею')

bot.polling(none_stop=True)
