import telebot
from telebot import types
import sqlite3
import datetime

bot = telebot.TeleBot('6200404821:AAEiHQQAwR2gLbORrYRT42wWu4kHyCeOrKo')

pol0, ves0, rost0, old0, goal0 = '', 0, 0, 0, 0
name, fit0 = '', ''
tg_id = 0
priem = ''
bluda = []
vidi = []
bludo = ''
kkal_for_that = 0
con = sqlite3.connect('eda.db', check_same_thread=False)
priem_for_print = ''

@bot.message_handler(commands=['start'])
def start(message):
    cur = con.cursor()
    a = cur.execute('''SELECT tg_id FROM users''')
    c = []
    m = f'Доброго времени суток, <i>{message.from_user.first_name}</i>'
    for i in a:
        c.append(*i)
    if message.from_user.id not in c:
        m1 = 'Для начала вам нужно заполнить свои данные, для этого нажмите кпопку "/input_data".' \
         'После заполнения нажмите кнопку "food"'
        bot.send_message(message.chat.id, m, parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton('/input_data')
        markup.add(item1)
    else:
        m1 = 'Нажмите кнопку "food" для записи еды'
        bot.send_message(message.chat.id, m, parse_mode='html')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item2 = types.KeyboardButton('food')
        markup.add(item2)
    bot.send_message(message.chat.id, m1, parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['input_data'])
def input_data(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    pol = types.KeyboardButton('/pol')
    rost = types.KeyboardButton('/rost')
    ves = types.KeyboardButton('/ves')
    old = types.KeyboardButton('/age')
    goal = types.KeyboardButton('/goal')
    end = types.KeyboardButton('/ready')

    markup.add(pol, rost, ves, old, goal, end)
    bot.send_message(message.chat.id, 'Укажите свои данные', reply_markup=markup)


@bot.message_handler(commands=['pol', 'rost', 'ves', 'age', 'goal', 'ready', 'fit'])
def obrabotka_data(message):
    if message.text == '/pol':
        markup1 = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('Мужской', callback_data='man')
        item2 = types.InlineKeyboardButton('Женский', callback_data='woman')

        markup1.add(item1, item2)
        bot.send_message(message.chat.id, 'Какой твой пол?', reply_markup=markup1)

    elif message.text == '/age':
        markup2 = types.InlineKeyboardMarkup(row_width=3)
        item10 = types.InlineKeyboardButton('младше 11', callback_data='<10')
        item11 = types.InlineKeyboardButton('11-18', callback_data='11')
        item19 = types.InlineKeyboardButton('19-29', callback_data='19')
        item30 = types.InlineKeyboardButton('30-39', callback_data='30')
        item40 = types.InlineKeyboardButton('40-59', callback_data='40')
        item60 = types.InlineKeyboardButton('старше 60', callback_data='>60')

        markup2.add(item10, item11, item19, item30, item40, item60)
        bot.send_message(message.chat.id, 'Сколько вам лет?', reply_markup=markup2)

    elif message.text == '/rost':
        markup3 = types.InlineKeyboardMarkup(row_width=3)
        item139 = types.InlineKeyboardButton('меньше 140', callback_data='130')
        item140 = types.InlineKeyboardButton('140-150', callback_data='140')
        item150 = types.InlineKeyboardButton('150-160', callback_data='150')
        item160 = types.InlineKeyboardButton('160-170', callback_data='160')
        item170 = types.InlineKeyboardButton('170-180', callback_data='170')
        item180 = types.InlineKeyboardButton('180-190', callback_data='180')
        item190 = types.InlineKeyboardButton('больше 190', callback_data='190')

        markup3.add(item139, item140, item150, item160, item170, item180, item190)
        bot.send_message(message.chat.id, 'Какой ваш рост?', reply_markup=markup3)

    elif message.text == '/ves':
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

        markup4.add(item400, item41, item46, item51, item56, item61, item66, item71, item76, item81, item86, item90)
        bot.send_message(message.chat.id, 'Сколько вы весите?', reply_markup=markup4)

    elif message.text == '/goal':
        markup5 = types.InlineKeyboardMarkup(row_width=2)
        item012 = types.InlineKeyboardButton('0', callback_data='12')
        item014 = types.InlineKeyboardButton('1–3', callback_data='14')
        item016 = types.InlineKeyboardButton('3–5', callback_data='16')
        item018 = types.InlineKeyboardButton('каждый день', callback_data='18')
        item020 = types.InlineKeyboardButton('2 раза в день', callback_data='20')

        markup5.add(item012, item014, item016, item018, item020)
        bot.send_message(message.chat.id, 'Сколько у вас тренировок в неделю?', reply_markup=markup5)

    elif message.text == '/fit':
        markup6 = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('похудеть', callback_data='slim')
        item2 = types.InlineKeyboardButton('набрать массу', callback_data='xxxl')

        markup6.add(item1, item2)
        bot.send_message(message.chat.id, 'Ваша цель?', reply_markup=markup6)

    elif message.text == '/ready':
        if T_or_F() == True:
            bot.send_message(message.chat.id, f'Вам нужно потреблять {int(calorie_calculation())} в день')
            markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('food')
            markup4.add(item1)

            cur = con.cursor()
            b = cur.execute(f'''SELECT tg_id FROM users''').fetchall()
            resss = []
            for i in b:
                resss.append(*i)
            if message.from_user.id not in resss:
                cur = con.cursor()
                cur.execute("""INSERT INTO users
                                        (name, tg_id, kkal_needed) VALUES (?, ?, ?)""",
                            (message.from_user.first_name, message.from_user.id, int(calorie_calculation())))
                con.commit()
                cur.close()

            bot.send_message(message.chat.id, 'Все готово!', reply_markup=markup4)
        elif T_or_F() == False:
            bot.send_message(message.chat.id, f'Вы не заполнили все пункты')

    else:
        bot.send_message(message.chat.id, 'Извините, я так не умею')


def T_or_F():
    if pol0 != '' and ves0 != 0 and rost0 != 0 and old0 != 0 and goal0 != 0 and fit0 == '':
        return True
    else:
        return False


def calorie_calculation():
    if pol0 == 'man':
        ans = (66 + (13.7 * ves0) + (5 * rost0) - (6.76 * old0)) * goal0 / 10
        if fit0 == 'slim':
            ans -= 400
        return ans
    elif pol0 == 'woman':
        ans = (655 + (9.6 * ves0) + (1.8 * rost0) - (4.7 * old0)) * goal0 / 10
        if fit0 == 'slim':
            ans -= 400
        return ans


@bot.callback_query_handler(func=lambda call: True)
def callback_imline(call):
    global pol0, ves0, rost0, old0, goal0
    try:
        if call.message:
            if call.data == 'man':
                pol0 = 'man'
            elif call.data == 'woman':
                pol0 = 'woman'

            if call.data == '<10':
                old0 = 10
            elif call.data == '11':
                old0 = 11
            elif call.data == '19':
                old0 = 19
            elif call.data == '30':
                old0 = 30
            elif call.data == '40':
                old0 = 40
            elif call.data == '>60':
                old0 = 60

            for i in range(130, 191, 10):
                if call.data == str(i):
                    rost0 = i + 10

            for i in range(36, 92, 5):
                if call.data == str(i):
                    ves0 = i + 4

            for i in range(12, 21, 2):
                if call.data == str(i):
                    goal0 = i
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.delete_message(call.message.chat.id, call.message.message_id - 1)

    except Exception as e:
        print(repr(e))


@bot.message_handler()
def food(message):
    global name, tg_id, priem, bluda, vidi, bludo, kkal_for_that, priem_for_print
    cur = con.cursor()
    a = cur.execute(f'''SELECT name FROM main''').fetchall()
    for i in a:
        bluda.append(*i)

    a = cur.execute(f'''SELECT gotovka FROM main''')
    for i in a:
        vidi.append(*i)
    name = message.from_user.first_name
    tg_id = message.from_user.id
    cur = con.cursor()
    if message.text == 'food':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        zavtrak = types.KeyboardButton('завтрак')
        obed = types.KeyboardButton('обед')
        ujin = types.KeyboardButton('ужин')
        perekus = types.KeyboardButton('перекус')
        markup.add(zavtrak, obed, ujin, perekus)

        bot.send_message(message.chat.id, 'Хорошо, в какой прием пищи вы хотите записать съеденное?', reply_markup=markup)
        print(message.text)
    elif message.text in ['завтрак', 'обед', 'ужин', 'перекус', 'все']:
        print(message.text)
        priem_for_print = message.text
        if message.text != 'все':
            if message.text == 'завтрак':
                priem = 'zavtrak'
            elif message.text == 'обед':
                priem = 'obed'
            elif message.text == 'ужин':
                priem = 'ujin'
            elif message.text == 'перекус':
                priem = 'perekus'
            # res = cur.execute(f'''SELECT {priem} FROM users
            #            WHERE users.name = ? AND users.tg_id = ?''', (name, tg_id))
            bot.send_message(message.chat.id, 'Введите с клавиатуры что вы ели(в иминительном падеже)')
            print(bluda, 1)
    elif message.text.lower() in bluda:
        print(message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        res_2 = cur.execute(f'''SELECT gotovka FROM main
                                WHERE name = ?''', (message.text.lower(),)).fetchall()
        ress = []
        for i in res_2:
            ress.append(*i)
        print(ress)
        if len(ress) != 0:
            for i in ress:
                markup.add(types.KeyboardButton(i))
        if message.text[-1] == 'а':
            bot.send_message(message.chat.id, 'какая именно?', reply_markup=markup)
        elif message.text != 'а':
            bot.send_message(message.chat.id, 'какой именно?', reply_markup=markup)
        elif message.text[-1] == 'о':
            bot.send_message(message.chat.id, 'какое именно?', reply_markup=markup)
        bludo = message.text.lower()
        print(bludo)
    elif message.text in vidi:
        kkal_for_that = int(*cur.execute(f'''SELECT kkal FROM main
                                WHERE name = ? AND gotovka = ?''', (bludo, message.text.lower())).fetchone())
        print(kkal_for_that)
        bot.send_message(message.chat.id, 'сколько грамм?')
    elif message.text.isdigit():
        a = int(message.text)
        a = a // 100
        print(type(kkal_for_that))
        print(type(a))
        kkal_for_that = kkal_for_that * a
        cur = con.cursor()
        b = cur.execute(f"""INSERT INTO userdata (user_id, kkal, priem, date) VALUES (?, ?, ?, ?)""",
                    (message.from_user.id, kkal_for_that, priem, datetime.datetime.now()))
        con.commit()
        cur.close()
        bot.send_message(message.chat.id, f'вы съели {kkal_for_that} ккал')
        bot.send_message(message.chat.id, f'Для записи продуктов в другой прием пищи нажмите food')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(types.KeyboardButton('food'))
        markup.add(types.KeyboardButton(f'{priem_for_print}'))
        bot.send_message(message.chat.id, f'Для продолжения записи продуктув в этот прием пищи нажмите {priem_for_print}', reply_markup=markup)


if __name__ == '__main__':
    bot.polling(none_stop=True)
