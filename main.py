import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('6200404821:AAEiHQQAwR2gLbORrYRT42wWu4kHyCeOrKo')

con = sqlite3.connect('eda.db', check_same_thread=False)
name = ''
tg_id = 0
priem = ''
bluda = []


@bot.message_handler(commands=['start'])
def start(message):
    global bluda
    cur = con.cursor()
    a = cur.execute(f'''SELECT name FROM main''').fetchall()
    for i in a:
        bluda.append(*i)
    m = f'Доброго времени суток, {message.from_user.first_name}'
    bot.send_message(message.chat.id, m, parse_mode='html')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    pol = types.KeyboardButton('пол')
    rost = types.KeyboardButton('рост')
    ves = types.KeyboardButton('вес')
    old = types.KeyboardButton('возраст')

    markup.add(pol, rost, ves, old)
    bot.send_message(message.chat.id, 'Укажите свои данные', reply_markup=markup)


@bot.message_handler()
def obrabotka_data(message):
    if message.text == 'пол':
        markup1 = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('Мужской', callback_data='man')
        item2 = types.InlineKeyboardButton('Женский', callback_data='woman')

        markup1.add(item1, item2)
        bot.send_message(message.chat.id, 'Какой твой пол?', reply_markup=markup1)

    elif message.text == 'возраст':
        markup2 = types.InlineKeyboardMarkup(row_width=3)
        item10 = types.InlineKeyboardButton('младше 11', callback_data='<10')
        item11 = types.InlineKeyboardButton('11-18', callback_data='11')
        item19 = types.InlineKeyboardButton('19-29', callback_data='19')
        item30 = types.InlineKeyboardButton('30-39', callback_data='30')
        item40 = types.InlineKeyboardButton('40-59', callback_data='40')
        item60 = types.InlineKeyboardButton('старше 60', callback_data='>60')

        markup2.add(item10, item11, item60, item40, item30, item19)
        bot.send_message(message.chat.id, 'Сколько вам лет?', reply_markup=markup2)

    elif message.text == 'рост':
        markup3 = types.InlineKeyboardMarkup(row_width=3)
        item139 = types.InlineKeyboardButton('меньше 140', callback_data='130')
        item140 = types.InlineKeyboardButton('140-150', callback_data='140')
        item150 = types.InlineKeyboardButton('150-160', callback_data='150')
        item160 = types.InlineKeyboardButton('160-170', callback_data='160')
        item170 = types.InlineKeyboardButton('170-180', callback_data='170')
        item180 = types.InlineKeyboardButton('180-190', callback_data='180')
        item190 = types.InlineKeyboardButton('больше 190', callback_data='190')

        markup3.add(item139, item190, item140, item180, item170, item160, item150)
        bot.send_message(message.chat.id, 'Какой ваш рост?', reply_markup=markup3)

    elif message.text == 'вес':
        markup4 = types.InlineKeyboardMarkup(row_width=3)
        item400 = types.InlineKeyboardButton('меньше 40', callback_data='36')
        item41 = types.InlineKeyboardButton('41-45', callback_data='41')
        item46 = types.InlineKeyboardButton('46-50', callback_data='46')
        item51 = types.InlineKeyboardButton('51-55', callback_data='51')
        item56 = types.InlineKeyboardButton('56-60', callback_data='56')
        item61 = types.InlineKeyboardButton('61-65', callback_data='61')
        item66 = types.InlineKeyboardButton('66-70', callback_data='66')
        item71 = types.InlineKeyboardButton('71-75', callback_data='71')
        item76 = types.InlineKeyboardButton('76-80', callback_data='76')
        item81 = types.InlineKeyboardButton('81-85', callback_data='81')
        item86 = types.InlineKeyboardButton('86-90', callback_data='86')
        item90 = types.InlineKeyboardButton('больше 90', callback_data='91')

        markup4.add(item90, item76, item86, item400, item56, item51, item71, item81, item66, item61, item46, item41)
        bot.send_message(message.chat.id, 'Сколько вы весите?', reply_markup=markup4)

    else:
        bot.send_message(message.chat.id, 'Извините, я так не умею')


@bot.callback_query_handler(func=lambda call: True)
def callback_imline(call):
    global pol, ves, rost, old
    try:
        if call.message:
            if call.data == 'man':
                pol = 'man'
            elif call.data == 'woman':
                pol = 'woman'

            if call.data == '<10':
                old = 10
            elif call.data == '11':
                old = 11
            elif call.data == '19':
                old = 19
            elif call.data == '30':
                old = 30
            elif call.data == '40':
                old = 40
            elif call.data == '>60':
                old = 60

            for i in range(130, 191, 10):
                if call.data == str(i):
                    rost = i

            for i in range(36, 92, 5):
                if call.data == str(i):
                    ves = i

    except Exception as e:
        print(repr(e))


@bot.message_handler(commands=['zapis'])
def zapis(message):
    global name, tg_id, priem, bluda
    name = message.from_user.first_name
    tg_id = message.from_user.id
    cur = con.cursor()
    if message.text == '/zapis':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        zavtrak = types.KeyboardButton('завтрак')
        obed = types.KeyboardButton('обед')
        ujin = types.KeyboardButton('ужин')
        perekus = types.KeyboardButton('перекус')
        markup.add(zavtrak, obed, ujin, perekus)

        b = cur.execute(f'''SELECT tg_id FROM users''').fetchall()
        resss = []
        for i in b:
            resss.append(*i)
        if message.from_user.id not in resss:
            cur = con.cursor()
            cur.execute("""INSERT INTO users
                        (name, tg_id) VALUES (?, ?)""", (message.from_user.first_name, message.from_user.id))
            con.commit()
            cur.close()

        bot.send_message(message.chat.id, 'Хорошо, в какой прием пищи?', reply_markup=markup)
        print(message.text)
    elif message.text in ['завтрак', 'обед', 'ужин', 'перекус', 'все']:
        print(message.text)
        if message.text != 'все':
            if message.text == 'завтрак':
                priem = 'zavtrak'
            elif message.text == 'обед':
                priem = 'obed'
            elif message.text == 'ужин':
                priem = 'ujin'
            elif message.text == 'перекус':
                priem = 'perekus'
            res = cur.execute(f'''SELECT {priem} FROM users
                       WHERE users.name = ? AND users.tg_id = ?''', (name, tg_id))
            bot.send_message(message.chat.id, 'Что вы ели?')
            print(bluda)
    elif message.text in bluda:
        print(message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        res_2 = cur.execute(f'''SELECT gotovka FROM main
                                WHERE name = ?''', (message.text,)).fetchall()
        ress = []
        for i in res_2:
            ress.append(*i)
        if len(ress) > 1:
            for i in ress:
                markup.add(types.KeyboardButton(i))
        if message.text[-1] == 'а':
            bot.send_message(message.chat.id, 'какую именно?', reply_markup=markup)
        elif message.text != 'а':
            bot.send_message(message.chat.id, 'какой именно?', reply_markup=markup)


bot.polling(none_stop=True)
