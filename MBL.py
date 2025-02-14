import telebot
from telebot import types

bot = telebot.TeleBot('Token')

def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton('Герои')
    button2 = types.KeyboardButton('Снаряжение')
    button3 = types.KeyboardButton('Советы')
    button4 = types.KeyboardButton('Новости')
    markup.add(button1, button2, button3, button4)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
     with open("piki/mlbb1.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo)
        welcome_text = (
        "Добро пожаловать в бот Mobile Legends! Mobile Legends: Bang Bang — это популярная многопользовательская игра в жанре MOBA "
        "(мобильная онлайн-битва на арене), разработанная компанией Moonton. В игре две команды по пять игроков сражаются друг с другом, "
        "чтобы уничтожить базу противника, при этом зарабатывая золото и опыт, прокачивая героев и развивая стратегию команды. "
        "Игроки выбирают из разнообразных героев с уникальными способностями, каждый из которых занимает определённую роль на поле боя. "
        "Выберите опцию ниже.")
        bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu())

@bot.message_handler(func=lambda message: message.text == "Герои")
def handle_heroes(message):
    otvet = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton("Убийцы", callback_data='hero_assassin')
    button2 = types.InlineKeyboardButton("Стрелки", callback_data='hero_marksman')
    button3 = types.InlineKeyboardButton("Маги", callback_data='hero_mage')
    button4 = types.InlineKeyboardButton("Роум", callback_data='hero_roam')
    button5 = types.InlineKeyboardButton("Боец", callback_data='hero_fighter')
    button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_main')
    otvet.add(button1, button2, button3, button4, button5, button_back)
    bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=otvet)

@bot.message_handler(func=lambda message: message.text == "Советы")
def handle_sovet(message):
    markup99 = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton("Основы игры", callback_data='hero_osn')
    button2 = types.InlineKeyboardButton("Советы для разных ролей", callback_data='hero_roli')
    button3 = types.InlineKeyboardButton("Советы по стратегии", callback_data='hero_strateg')
    button4 = types.InlineKeyboardButton("Советы по контрпикам", callback_data='hero_novich')
    markup99.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=markup99)

@bot.message_handler(func=lambda message: message.text == "Снаряжение")
def handle_equipment(message):
    otvedd = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton("Атака", callback_data='attacka')
    button2 = types.InlineKeyboardButton("Магия", callback_data='magic')
    button3 = types.InlineKeyboardButton("Защита", callback_data='defense')
    button4 = types.InlineKeyboardButton("Передвижение", callback_data='movement')
    button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_main')
    otvedd.add(button1, button2, button3, button4, button_back)
    bot.send_message(message.chat.id, "Вот несколько снаряжений", reply_markup=otvedd)

@bot.callback_query_handler(func=lambda call: True)
def callback_query_photos(call):
    if call.data == "attacka":
        markupp = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Трезубец", callback_data='cg')
        button2 = types.InlineKeyboardButton("Злобный рык", callback_data='ujr')
        button3 = types.InlineKeyboardButton("Топор войны", callback_data='arfv')
        button4 = types.InlineKeyboardButton("Удар охотника", callback_data='okjm')
        button_back2 = types.InlineKeyboardButton("Назад", callback_data='back_to_equipment')
        markupp.add(button1, button2, button3, button4, button_back2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                             text="Вот несколько снаряжений для атаки:", reply_markup=markupp)
    elif call.data == "cg":
        media = [types.InputMediaPhoto(open('piki/trez1.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        markup09 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Трезубец", callback_data='cg')
        button2 = types.InlineKeyboardButton("Злобный рык", callback_data='ujr')
        button3 = types.InlineKeyboardButton("Топор войны", callback_data='arfv')
        button4 = types.InlineKeyboardButton("Удар охотника", callback_data='okjm')
        button_back3 = types.InlineKeyboardButton("Назад", callback_data='back_to_equipment')
        markup09.add(button1, button2, button3, button4, button_back3)
        bot.send_message(call.message.chat.id, "Выберите снаряжение:", reply_markup=markup09)
    elif call.data == "ujr":
        media = [types.InputMediaPhoto(open('piki/zlob1.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        markup08 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Трезубец", callback_data='cg')
        button2 = types.InlineKeyboardButton("Злобный рык", callback_data='ujr')
        button3 = types.InlineKeyboardButton("Топор войны", callback_data='arfv')
        button4 = types.InlineKeyboardButton("Удар охотника", callback_data='okjm')
        button_back4 = types.InlineKeyboardButton("Назад", callback_data='back_to_equipment')
        markup08.add(button1, button2, button3, button4, button_back4)
        bot.send_message(call.message.chat.id, "Выберите снаряжение:", reply_markup=markup08)
    elif call.data == "arfv":
        media = [types.InputMediaPhoto(open('piki/topor1.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        markup07 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Трезубец", callback_data='cg')
        button2 = types.InlineKeyboardButton("Злобный рык", callback_data='ujr')
        button3 = types.InlineKeyboardButton("Топор войны", callback_data='arfv')
        button4 = types.InlineKeyboardButton("Удар охотника", callback_data='okjm')
        button_back5 = types.InlineKeyboardButton("Назад", callback_data='back_to_equipment')
        markup07.add(button1, button2, button3, button4, button_back5)
        bot.send_message(call.message.chat.id, "Выберите снаряжение:", reply_markup=markup07)
    elif call.data == "okjm":
        media = [types.InputMediaPhoto(open('piki/ydar1.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        markup06 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Трезубец", callback_data='cg')
        button2 = types.InlineKeyboardButton("Злобный рык", callback_data='ujr')
        button3 = types.InlineKeyboardButton("Топор войны", callback_data='arfv')
        button4 = types.InlineKeyboardButton("Удар охотника", callback_data='okjm')
        button_back6 = types.InlineKeyboardButton("Назад", callback_data='back_to_equipment')
        markup06.add(button1, button2, button3, button4, button_back6)
        bot.send_message(call.message.chat.id, "Выберите снаряжение:", reply_markup=markup06)

    elif call.data == "magic":
        markupm = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Пылающий жезл", callback_data='bu')
        button2 = types.InlineKeyboardButton("Божественный меч", callback_data='buy')
        button3 = types.InlineKeyboardButton("Кровавые крылья", callback_data='bur')
        button4 = types.InlineKeyboardButton("Священный кристал", callback_data='bue')
        button_back7 = types.InlineKeyboardButton("Назад", callback_data='back_to_equipment')
        markupm.add(button1, button2, button3, button4, button_back7)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                             text="Вот несколько снаряжений для магии:", reply_markup=markupm)
    
    elif call.data == "bu":
        media = [types.InputMediaPhoto(open('piki/playu1.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        markup05 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Пылающий жезл", callback_data='bu')
        button2 = types.InlineKeyboardButton("Божественный меч", callback_data='buy')
        button3 = types.InlineKeyboardButton("Кровавые крылья", callback_data='bur')
        button4 = types.InlineKeyboardButton("Священный кристал", callback_data='bue')
        button_back8 = types.InlineKeyboardButton("Назад", callback_data='back_to_equipment')
        markup05.add(button1, button2, button3, button4, button_back8)
        bot.send_message(call.message.chat.id, "Выберите снаряжение:", reply_markup=markup05)
    elif call.data == "buy":
        media = [types.InputMediaPhoto(open('piki/mech1.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        markup04 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Пылающий жезл", callback_data='bu')
        button2 = types.InlineKeyboardButton("Божественный меч", callback_data='buy')
        button3 = types.InlineKeyboardButton("Кровавые крылья", callback_data='bur')
        button4 = types.InlineKeyboardButton("Священный кристал", callback_data='bue')
        button_back9 = types.InlineKeyboardButton("Назад", callback_data='back_to_equipment')
        markup04.add(button1, button2, button3, button4, button_back9)
        bot.send_message(call.message.chat.id, "Выберите снаряжение:", reply_markup=markup04)
    elif call.data == "bur":
        media = [types.InputMediaPhoto(open('piki/krov1.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        markup03 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Пылающий жезл", callback_data='bu')
        button2 = types.InlineKeyboardButton("Божественный меч", callback_data='buy')
        button3 = types.InlineKeyboardButton("Кровавые крылья", callback_data='bur')
        button4 = types.InlineKeyboardButton("Священный кристал", callback_data='bue')
        button_back10 = types.InlineKeyboardButton("Назад", callback_data='back_to_equipment')
        markup03.add(button1, button2, button3, button4, button_back10)
        bot.send_message(call.message.chat.id, "Выберите снаряжение:", reply_markup=markup03)
    elif call.data == "bue":
        media = [types.InputMediaPhoto(open('piki/kristal1.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        markup02 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Пылающий жезл", callback_data='bu')
        button2 = types.InlineKeyboardButton("Божественный меч", callback_data='buy')
        button3 = types.InlineKeyboardButton("Кровавые крылья", callback_data='bur')
        button4 = types.InlineKeyboardButton("Священный кристал", callback_data='bue')
        button_back11 = types.InlineKeyboardButton("Назад", callback_data='back_to_equipment')
        markup02.add(button1, button2, button3, button4, button_back11)
        bot.send_message(call.message.chat.id, "Выберите снаряжение:", reply_markup=markup02)
    
    elif call.data == "defense":
        markupa = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Господство льда", callback_data='gl')
        button2 = types.InlineKeyboardButton("Древняя кираса", callback_data='dk')
        button3 = types.InlineKeyboardButton("Щит афины", callback_data='ha')
        button4 = types.InlineKeyboardButton("Бесмертие", callback_data='yi')
        button_back12 = types.InlineKeyboardButton("Назад", callback_data='back_to_equipment')
        markupa.add(button1, button2, button3, button4, button_back12)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                             text="Вот несколько снаряжений для защиты:", reply_markup=markupa)
    elif call.data == "gl":
        media = [types.InputMediaPhoto(open('piki/gospods1.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        markup01 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Господство льда", callback_data='gl')
        button2 = types.InlineKeyboardButton("Древняя кираса", callback_data='dk')
        button3 = types.InlineKeyboardButton("Щит афины", callback_data='ha')
        button4 = types.InlineKeyboardButton("Бесмертие", callback_data='yi')
        button_back13 = types.InlineKeyboardButton("Назад", callback_data='back_to_equipment')
        markup01.add(button1, button2, button3, button4, button_back13)
        bot.send_message(call.message.chat.id, "Выберите снаряжение:", reply_markup=markup01)
    elif call.data == "dk":
        media = [types.InputMediaPhoto(open('piki/kirasa1.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        markup00 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Господство льда", callback_data='gl')
        button2 = types.InlineKeyboardButton("Древняя кираса", callback_data='dk')
        button3 = types.InlineKeyboardButton("Щит афины", callback_data='ha')
        button4 = types.InlineKeyboardButton("Бесмертие", callback_data='yi')
        button_back14 = types.InlineKeyboardButton("Назад", callback_data='back_to_equipment')
        markup00.add(button1, button2, button3, button4, button_back14)
        bot.send_message(call.message.chat.id, "Выберите снаряжение:", reply_markup=markup00)
    elif call.data == "ha":
        media = [types.InputMediaPhoto(open('piki/afin1.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        markup001 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Господство льда", callback_data='gl')
        button2 = types.InlineKeyboardButton("Древняя кираса", callback_data='dk')
        button3 = types.InlineKeyboardButton("Щит афины", callback_data='ha')
        button4 = types.InlineKeyboardButton("Бесмертие", callback_data='yi')
        button_back15 = types.InlineKeyboardButton("Назад", callback_data='back_to_equipment')
        markup001.add(button1, button2, button3, button4, button_back15)
        bot.send_message(call.message.chat.id, "Выберите убийцу:", reply_markup=markup001)
    elif call.data == "yi":
        media = [types.InputMediaPhoto(open('piki/besmer1.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        markup002 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Господство льда", callback_data='gl')
        button2 = types.InlineKeyboardButton("Древняя кираса", callback_data='dk')
        button3 = types.InlineKeyboardButton("Щит афины", callback_data='ha')
        button4 = types.InlineKeyboardButton("Бесмертие", callback_data='yi')
        button_back16 = types.InlineKeyboardButton("Назад", callback_data='back_to_equipment')
        markup002.add(button1, button2, button3, button4, button_back16)
        bot.send_message(call.message.chat.id, "Выберите снаряжение:", reply_markup=markup002)
        
    elif call.data == "movement":
        markupz = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Сапоги воина", callback_data='sp')
        button2 = types.InlineKeyboardButton("Прочные сапоги", callback_data='ps')
        button3 = types.InlineKeyboardButton("Магические ботинки", callback_data='mb')
        button4 = types.InlineKeyboardButton("Сапоги заклинателя", callback_data='sz')
        button_back17 = types.InlineKeyboardButton("Назад", callback_data='back_to_equipment')
        markupz.add(button1, button2, button3, button4, button_back17)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                             text="Вот несколько снаряжений для передвижения", reply_markup=markupz)
    elif call.data == "sp":
        media = [types.InputMediaPhoto(open('piki/spvoin1.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        markup003 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Сапоги воина", callback_data='sp')
        button2 = types.InlineKeyboardButton("Прочные сапоги", callback_data='ps')
        button3 = types.InlineKeyboardButton("Магические ботинки", callback_data='mb')
        button4 = types.InlineKeyboardButton("Сапоги заклинателя", callback_data='sz')
        button_back18 = types.InlineKeyboardButton("Назад", callback_data='back_to_equipment')
        markup003.add(button1, button2, button3, button4, button_back18)
        bot.send_message(call.message.chat.id, "Выберите снаряжение:", reply_markup=markup003)
    elif call.data == "ps":
        media = [types.InputMediaPhoto(open('piki/proch1.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        markup004 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Сапоги воина", callback_data='sp')
        button2 = types.InlineKeyboardButton("Прочные сапоги", callback_data='ps')
        button3 = types.InlineKeyboardButton("Магические ботинки", callback_data='mb')
        button4 = types.InlineKeyboardButton("Сапоги заклинателя", callback_data='sz')
        button_back19 = types.InlineKeyboardButton("Назад", callback_data='back_to_equipment')
        markup004.add(button1, button2, button3, button4, button_back19)
        bot.send_message(call.message.chat.id, "Выберите снаряжение:", reply_markup=markup004)
    elif call.data == "mb":
        media = [types.InputMediaPhoto(open('piki/magbot1.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        markup005 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Сапоги воина", callback_data='sp')
        button2 = types.InlineKeyboardButton("Прочные сапоги", callback_data='ps')
        button3 = types.InlineKeyboardButton("Магические ботинки", callback_data='mb')
        button4 = types.InlineKeyboardButton("Сапоги заклинателя", callback_data='sz')
        button_back20 = types.InlineKeyboardButton("Назад", callback_data='back_to_equipment')
        markup005.add(button1, button2, button3, button4, button_back20)
        bot.send_message(call.message.chat.id, "Выберите снаряжение:", reply_markup=markup005)
    elif call.data == "sz":
        media = [types.InputMediaPhoto(open('piki/zaclin1.jpg', 'rb')),]
        bot.send_media_group(call.message.chat.id, media)
        markup006 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Сапоги воина", callback_data='sp')
        button2 = types.InlineKeyboardButton("Прочные сапоги", callback_data='ps')
        button3 = types.InlineKeyboardButton("Магические ботинки", callback_data='mb')
        button4 = types.InlineKeyboardButton("Сапоги заклинателя", callback_data='sz')
        button_back21 = types.InlineKeyboardButton("Назад", callback_data='back_to_equipment')
        markup006.add(button1, button2, button3, button4, button_back21)
        bot.send_message(call.message.chat.id, "Выберите снаряжение:", reply_markup=markup006)
    
    elif call.data == "hero_assassin":
        markup5 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Хаябуса", callback_data='hero_hayabusa')
        button2 = types.InlineKeyboardButton("Джой", callback_data='hero_joi')
        button3 = types.InlineKeyboardButton("СУ-е", callback_data='hero_sye')
        button4 = types.InlineKeyboardButton("Фанни", callback_data='hero_fanny')
        button5 = types.InlineKeyboardButton("Ланселот", callback_data='hero_lanselot')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup5.add(button1, button2, button3, button4, button5, button_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                             text="Вы выбрали топ 5 убийц и сборки на них:", reply_markup=markup5)
    elif call.data == "hero_hayabusa":
        media = [types.InputMediaPhoto(open('piki/Xay1.jpg', 'rb'), caption="Фото 1"),
                 types.InputMediaPhoto(open('piki/Xay2.jpg', 'rb'), caption="Фото 2"),
                 types.InputMediaPhoto(open('piki/Xay3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup6 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Хаябуса", callback_data='hero_hayabusa')
        button2 = types.InlineKeyboardButton("Джой", callback_data='hero_joi')
        button3 = types.InlineKeyboardButton("СУ-е", callback_data='hero_sye')
        button4 = types.InlineKeyboardButton("Фанни", callback_data='hero_fanny')
        button5 = types.InlineKeyboardButton("Ланселот", callback_data='hero_lanselot')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup6.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите убийцу:", reply_markup=markup6)
    elif call.data == "hero_joi":
        media = [types.InputMediaPhoto(open('piki/djo1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/djo2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/djo3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup7 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Хаябуса", callback_data='hero_hayabusa')
        button2 = types.InlineKeyboardButton("Джой", callback_data='hero_joi')
        button3 = types.InlineKeyboardButton("СУ-е", callback_data='hero_sye')
        button4 = types.InlineKeyboardButton("Фанни", callback_data='hero_fanny')
        button5 = types.InlineKeyboardButton("Ланселот", callback_data='hero_lanselot')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup7.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите убийцу:", reply_markup=markup7)
    elif call.data == "hero_sye":
        media = [types.InputMediaPhoto(open('piki/Sye1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/Sye2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/Sye3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup8 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Хаябуса", callback_data='hero_hayabusa')
        button2 = types.InlineKeyboardButton("Джой", callback_data='hero_joi')
        button3 = types.InlineKeyboardButton("СУ-е", callback_data='hero_sye')
        button4 = types.InlineKeyboardButton("Фанни", callback_data='hero_fanny')
        button5 = types.InlineKeyboardButton("Ланселот", callback_data='hero_lanselot')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup8.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите убийцу:", reply_markup=markup8)
    elif call.data == "hero_fanny":
        media = [types.InputMediaPhoto(open('piki/fan1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/fan2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/fan3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup9 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Хаябуса", callback_data='hero_hayabusa')
        button2 = types.InlineKeyboardButton("Джой", callback_data='hero_joi')
        button3 = types.InlineKeyboardButton("СУ-е", callback_data='hero_sye')
        button4 = types.InlineKeyboardButton("Фанни", callback_data='hero_fanny')
        button5 = types.InlineKeyboardButton("Ланселот", callback_data='hero_lanselot')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup9.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите убийцу:", reply_markup=markup9)
    elif call.data == "hero_lanselot":
        media = [types.InputMediaPhoto(open('piki/lans1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/lans2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/lans3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup10 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Хаябуса", callback_data='hero_hayabusa')
        button2 = types.InlineKeyboardButton("Джой", callback_data='hero_joi')
        button3 = types.InlineKeyboardButton("СУ-е", callback_data='hero_sye')
        button4 = types.InlineKeyboardButton("Фанни", callback_data='hero_fanny')
        button5 = types.InlineKeyboardButton("Ланселот", callback_data='hero_lanselot')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup10.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите убийцу:", reply_markup=markup10)
        
    elif call.data == "back_to_heroes":
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Убийцы", callback_data='hero_assassin')
        button2 = types.InlineKeyboardButton("Стрелки", callback_data='hero_marksman')
        button3 = types.InlineKeyboardButton("Маги", callback_data='hero_mage')
        button4 = types.InlineKeyboardButton("Роум", callback_data='hero_roam')
        button5 = types.InlineKeyboardButton("Боец", callback_data='hero_fighter')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_main')
        markup.add(button1, button2, button3, button4, button5, button_back)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Вот список метовых персонажей",
            reply_markup=markup
        )
    elif call.data == "back_to_main":
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Возвращаемся в главное меню.",
            reply_markup=None)


    elif call.data == "hero_marksman":
        markup11 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Грейнджер", callback_data='hero_greyndger')
        button2 = types.InlineKeyboardButton("Беатрис", callback_data='hero_beatris')
        button3 = types.InlineKeyboardButton("Ван-Ван", callback_data='hero_van-van')
        button4 = types.InlineKeyboardButton("Бруно", callback_data='hero_bruno')
        button5 = types.InlineKeyboardButton("Нотан", callback_data='hero_notan')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup11.add(button1, button2, button3, button4, button5, button_back)
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Вы выбрали топ 5 стрелков и сборки на них:",
                             reply_markup=markup11)
    elif call.data == "hero_greyndger":
        media = [types.InputMediaPhoto(open('piki/gren1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/gren2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/gren3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup12 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Грейнджер", callback_data='hero_greyndger')
        button2 = types.InlineKeyboardButton("Беатрис", callback_data='hero_beatris')
        button3 = types.InlineKeyboardButton("Ван-Ван", callback_data='hero_van-van')
        button4 = types.InlineKeyboardButton("Бруно", callback_data='hero_bruno')
        button5 = types.InlineKeyboardButton("Нотан", callback_data='hero_notan')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup12.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите стрелка:", reply_markup=markup12)
        
    elif call.data == "hero_beatris":
        media = [types.InputMediaPhoto(open('piki/beat1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/beat2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/beat3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup13 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Грейнджер", callback_data='hero_greyndger')
        button2 = types.InlineKeyboardButton("Беатрис", callback_data='hero_beatris')
        button3 = types.InlineKeyboardButton("Ван-Ван", callback_data='hero_van-van')
        button4 = types.InlineKeyboardButton("Бруно", callback_data='hero_bruno')
        button5 = types.InlineKeyboardButton("Нотан", callback_data='hero_notan')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup13.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите стрелка:", reply_markup=markup13)

    elif call.data == "hero_van-van":
        media = [types.InputMediaPhoto(open('piki/van1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/van2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/van3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup14 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Грейнджер", callback_data='hero_greyndger')
        button2 = types.InlineKeyboardButton("Беатрис", callback_data='hero_beatris')
        button3 = types.InlineKeyboardButton("Ван-Ван", callback_data='hero_van-van')
        button4 = types.InlineKeyboardButton("Бруно", callback_data='hero_bruno')
        button5 = types.InlineKeyboardButton("Нотан", callback_data='hero_notan')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup14.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите стрелка:", reply_markup=markup14)

    elif call.data == "hero_bruno":
        media = [types.InputMediaPhoto(open('piki/bru1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/bru2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/bru3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup15 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Грейнджер", callback_data='hero_greyndger')
        button2 = types.InlineKeyboardButton("Беатрис", callback_data='hero_beatris')
        button3 = types.InlineKeyboardButton("Ван-Ван", callback_data='hero_van-van')
        button4 = types.InlineKeyboardButton("Бруно", callback_data='hero_bruno')
        button5 = types.InlineKeyboardButton("Нотан", callback_data='hero_notan')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup15.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите стрелка:", reply_markup=markup15)

    elif call.data == "hero_notan":
        media = [types.InputMediaPhoto(open('piki/nott1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/nott2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/nott3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup16 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Грейнджер", callback_data='hero_greyndger')
        button2 = types.InlineKeyboardButton("Беатрис", callback_data='hero_beatris')
        button3 = types.InlineKeyboardButton("Ван-Ван", callback_data='hero_van-van')
        button4 = types.InlineKeyboardButton("Бруно", callback_data='hero_bruno')
        button5 = types.InlineKeyboardButton("Нотан", callback_data='hero_notan')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup16.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите стрелка:", reply_markup=markup16)

    elif call.data == "back_to_heroes":
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Убийцы", callback_data='hero_assassin')
        button2 = types.InlineKeyboardButton("Стрелки", callback_data='hero_marksman')
        button3 = types.InlineKeyboardButton("Маги", callback_data='hero_mage')
        button4 = types.InlineKeyboardButton("Роум", callback_data='hero_roam')
        button5 = types.InlineKeyboardButton("Боец", callback_data='hero_fighter')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_main')
        markup.add(button1, button2, button3, button4, button5, button_back)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Вот список метовых персонажей",
            reply_markup=markup
        )
    elif call.data == "back_to_main":
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Возвращаемся в главное меню.",
            reply_markup=None)
        
    elif call.data == "hero_mage":
        markup17 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Джусинь", callback_data='hero_dchysin')
        button2 = types.InlineKeyboardButton("Харит", callback_data='hero_xarit')
        button3 = types.InlineKeyboardButton("Ксавьер", callback_data='hero_ksava')
        button4 = types.InlineKeyboardButton("Ив", callback_data='hero_iv')
        button5 = types.InlineKeyboardButton("Сесилион", callback_data='hero_sesilion')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup17.add(button1, button2, button3, button4, button5, button_back)
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Вы выбрали топ 5 магов и сборки на них:",
                             reply_markup=markup17)
    elif call.data == "hero_dchysin":
        media = [types.InputMediaPhoto(open('piki/dchys1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/dchys2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/dchys3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup18 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Джусинь", callback_data='hero_dchysin')
        button2 = types.InlineKeyboardButton("Харит", callback_data='hero_xarit')
        button3 = types.InlineKeyboardButton("Ксавьер", callback_data='hero_ksava')
        button4 = types.InlineKeyboardButton("Ив", callback_data='hero_iv')
        button5 = types.InlineKeyboardButton("Сесилион", callback_data='hero_sesilion')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup18.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите мага:", reply_markup=markup18)

    elif call.data == "hero_xarit":
        media = [types.InputMediaPhoto(open('piki/xarit1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/xarit2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/xarit3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup19 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Джусинь", callback_data='hero_dchysin')
        button2 = types.InlineKeyboardButton("Харит", callback_data='hero_xarit')
        button3 = types.InlineKeyboardButton("Ксавьер", callback_data='hero_ksava')
        button4 = types.InlineKeyboardButton("Ив", callback_data='hero_iv')
        button5 = types.InlineKeyboardButton("Сесилион", callback_data='hero_sesilion')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup19.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите мага:", reply_markup=markup19)

    elif call.data == "hero_ksava":
        media = [types.InputMediaPhoto(open('piki/ksava1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/ksava2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/ksava3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup20 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Джусинь", callback_data='hero_dchysin')
        button2 = types.InlineKeyboardButton("Харит", callback_data='hero_xarit')
        button3 = types.InlineKeyboardButton("Ксавьер", callback_data='hero_ksava')
        button4 = types.InlineKeyboardButton("Ив", callback_data='hero_iv')
        button5 = types.InlineKeyboardButton("Сесилион", callback_data='hero_sesilion')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup20.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите мага:", reply_markup=markup20)

    elif call.data == "hero_iv":
        media = [types.InputMediaPhoto(open('piki/iv1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/iv2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/iv3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup21 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Джусинь", callback_data='hero_dchysin')
        button2 = types.InlineKeyboardButton("Харит", callback_data='hero_xarit')
        button3 = types.InlineKeyboardButton("Ксавьер", callback_data='hero_ksava')
        button4 = types.InlineKeyboardButton("Ив", callback_data='hero_iv')
        button5 = types.InlineKeyboardButton("Сесилион", callback_data='hero_sesilion')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup21.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите мага:", reply_markup=markup21)

    elif call.data == "hero_sesilion":
        media = [types.InputMediaPhoto(open('piki/sesi1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/sesi2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/sesi3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup22 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Джусинь", callback_data='hero_dchysin')
        button2 = types.InlineKeyboardButton("Харит", callback_data='hero_xarit')
        button3 = types.InlineKeyboardButton("Ксавьер", callback_data='hero_ksava')
        button4 = types.InlineKeyboardButton("Ив", callback_data='hero_iv')
        button5 = types.InlineKeyboardButton("Сесилион", callback_data='hero_sesilion')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup22.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите мага:", reply_markup=markup22)

    elif call.data == "back_to_heroes":
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Убийцы", callback_data='hero_assassin')
        button2 = types.InlineKeyboardButton("Стрелки", callback_data='hero_marksman')
        button3 = types.InlineKeyboardButton("Маги", callback_data='hero_mage')
        button4 = types.InlineKeyboardButton("Роум", callback_data='hero_roam')
        button5 = types.InlineKeyboardButton("Боец", callback_data='hero_fighter')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_main')
        markup.add(button1, button2, button3, button4, button5, button_back)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Вот список метовых персонажей",
            reply_markup=markup
        )
    elif call.data == "back_to_main":
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Возвращаемся в главное меню.",
            reply_markup=None
        )
    elif call.data == "hero_roam":
        markup23 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Гатоткача", callback_data='hero_gatot')
        button2 = types.InlineKeyboardButton("Чип", callback_data='hero_chip')
        button3 = types.InlineKeyboardButton("Хилос", callback_data='hero_xilos')
        button4 = types.InlineKeyboardButton("Хильда", callback_data='hero_xilda')
        button5 = types.InlineKeyboardButton("Чу", callback_data='hero_chy')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup23.add(button1, button2, button3, button4, button5, button_back)
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Вы выбрали топ 5 танков и сборки на них:",
                             reply_markup=markup23)
    elif call.data == "hero_gatot":
        media = [types.InputMediaPhoto(open('piki/gat1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/gat2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/gat3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup24 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Гатоткача", callback_data='hero_gatot')
        button2 = types.InlineKeyboardButton("Чип", callback_data='hero_chip')
        button3 = types.InlineKeyboardButton("Хилос", callback_data='hero_xilos')
        button4 = types.InlineKeyboardButton("Хильда", callback_data='hero_xilda')
        button5 = types.InlineKeyboardButton("Чу", callback_data='hero_chy')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup24.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите танка:", reply_markup=markup24)
    elif call.data == "hero_chip":
        media = [types.InputMediaPhoto(open('piki/chip1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/chip2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/chip3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup25 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Гатоткача", callback_data='hero_gatot')
        button2 = types.InlineKeyboardButton("Чип", callback_data='hero_chip')
        button3 = types.InlineKeyboardButton("Хилос", callback_data='hero_xilos')
        button4 = types.InlineKeyboardButton("Хильда", callback_data='hero_xilda')
        button5 = types.InlineKeyboardButton("Чу", callback_data='hero_chy')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup25.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите танка:", reply_markup=markup25)

    elif call.data == "hero_xilos":
        media = [types.InputMediaPhoto(open('piki/xilo1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/xilo2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/xilo3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup26 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Гатоткача", callback_data='hero_gatot')
        button2 = types.InlineKeyboardButton("Чип", callback_data='hero_chip')
        button3 = types.InlineKeyboardButton("Хилос", callback_data='hero_xilos')
        button4 = types.InlineKeyboardButton("Хильда", callback_data='hero_xilda')
        button5 = types.InlineKeyboardButton("Чу", callback_data='hero_chy')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup26.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите танка:", reply_markup=markup26)

    elif call.data == "hero_xilda":
        media = [types.InputMediaPhoto(open('piki/xilda1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/xilda2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/xilda3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup27 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Гатоткача", callback_data='hero_gatot')
        button2 = types.InlineKeyboardButton("Чип", callback_data='hero_chip')
        button3 = types.InlineKeyboardButton("Хилос", callback_data='hero_xilos')
        button4 = types.InlineKeyboardButton("Хильда", callback_data='hero_xilda')
        button5 = types.InlineKeyboardButton("Чу", callback_data='hero_chy')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup27.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите танка:", reply_markup=markup27)

    elif call.data == "hero_chy":
        media = [types.InputMediaPhoto(open('piki/chu1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/chu2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/chu3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup28 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Гатоткача", callback_data='hero_gatot')
        button2 = types.InlineKeyboardButton("Чип", callback_data='hero_chip')
        button3 = types.InlineKeyboardButton("Хилос", callback_data='hero_xilos')
        button4 = types.InlineKeyboardButton("Хильда", callback_data='hero_xilda')
        button5 = types.InlineKeyboardButton("Чу", callback_data='hero_chy')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup28.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите танка:", reply_markup=markup28)

    elif call.data == "back_to_heroes":
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Убийцы", callback_data='hero_assassin')
        button2 = types.InlineKeyboardButton("Стрелки", callback_data='hero_marksman')
        button3 = types.InlineKeyboardButton("Маги", callback_data='hero_mage')
        button4 = types.InlineKeyboardButton("Роум", callback_data='hero_roam')
        button5 = types.InlineKeyboardButton("Боец", callback_data='hero_fighter')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_main')
        markup.add(button1, button2, button3, button4, button5, button_back)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Вот список метовых персонажей",
            reply_markup=markup
        )
    elif call.data == "back_to_main":
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Возвращаемся в главное меню.",
            reply_markup=None)
        
    elif call.data == "hero_fighter":
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Баданг", callback_data='hero_badang')
        button2 = types.InlineKeyboardButton("Чичи", callback_data='hero_lucas')
        button3 = types.InlineKeyboardButton("Глу", callback_data='hero_glu')
        button4 = types.InlineKeyboardButton("Сан", callback_data='hero_san')
        button5 = types.InlineKeyboardButton("Халид", callback_data='hero_halid')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup.add(button1, button2, button3, button4, button5, button_back)
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Вы выбрали топ 5 бойцов и сборки на них:",
                             reply_markup=markup)
    elif call.data == "hero_badang":
        media = [types.InputMediaPhoto(open('piki/badg1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/badg2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/badg3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Баданг", callback_data='hero_badang')
        button2 = types.InlineKeyboardButton("Чичи", callback_data='hero_lucas')
        button3 = types.InlineKeyboardButton("Глу", callback_data='hero_glu')
        button4 = types.InlineKeyboardButton("Сан", callback_data='hero_san')
        button5 = types.InlineKeyboardButton("Халид", callback_data='hero_halid')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите бойца:", reply_markup=markup)

    elif call.data == "hero_lucas":
        media = [types.InputMediaPhoto(open('piki/chi1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/chi2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/chi3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Баданг", callback_data='hero_badang')
        button2 = types.InlineKeyboardButton("Чичи", callback_data='hero_lucas')
        button3 = types.InlineKeyboardButton("Глу", callback_data='hero_glu')
        button4 = types.InlineKeyboardButton("Сан", callback_data='hero_san')
        button5 = types.InlineKeyboardButton("Халид", callback_data='hero_halid')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите бойца:", reply_markup=markup)
    elif call.data == "hero_glu":
        media = [types.InputMediaPhoto(open('piki/glu1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/glu2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/glu3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Баданг", callback_data='hero_badang')
        button2 = types.InlineKeyboardButton("Чичи", callback_data='hero_lucas')
        button3 = types.InlineKeyboardButton("Глу", callback_data='hero_glu')
        button4 = types.InlineKeyboardButton("Сан", callback_data='hero_san')
        button5 = types.InlineKeyboardButton("Халид", callback_data='hero_halid')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите бойца:", reply_markup=markup)
    elif call.data == "hero_san":
        media = [types.InputMediaPhoto(open('piki/san1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/san2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/san3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Баданг", callback_data='hero_badang')
        button2 = types.InlineKeyboardButton("Чичи", callback_data='hero_lucas')
        button3 = types.InlineKeyboardButton("Глу", callback_data='hero_glu')
        button4 = types.InlineKeyboardButton("Сан", callback_data='hero_san')
        button5 = types.InlineKeyboardButton("Халид", callback_data='hero_halid')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите бойца:", reply_markup=markup)
    elif call.data == "hero_halid":
        media = [types.InputMediaPhoto(open('piki/halid1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/halid2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/halid3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Баданг", callback_data='hero_badang')
        button2 = types.InlineKeyboardButton("Чичи", callback_data='hero_lucas')
        button3 = types.InlineKeyboardButton("Глу", callback_data='hero_glu')
        button4 = types.InlineKeyboardButton("Сан", callback_data='hero_san')
        button5 = types.InlineKeyboardButton("Халид", callback_data='hero_halid')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup.add(button1, button2, button3, button4, button5, button_back)
        bot.send_message(call.message.chat.id, "Выберите бойца:", reply_markup=markup)

    elif call.data == "back_to_heroes":
        markup6 = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Убийцы", callback_data='hero_assassin')
        button2 = types.InlineKeyboardButton("Стрелки", callback_data='hero_marksman')
        button3 = types.InlineKeyboardButton("Маги", callback_data='hero_mage')
        button4 = types.InlineKeyboardButton("Роум", callback_data='hero_roam')
        button5 = types.InlineKeyboardButton("Боец", callback_data='hero_fighter')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_main')
        markup6.add(button1, button2, button3, button4, button5, button_back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                             text="Вот список метовых персонажей", reply_markup=markup6)
    elif call.data == "back_to_main":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                             text="Возвращаемся в главное меню.", reply_markup=None)
    elif call.data == "hero_osn":
        markupv = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton(text="Выбор героя", callback_data='zxc')
        button2 = types.InlineKeyboardButton(text="Основы карты", callback_data='zxcv')
        button3 = types.InlineKeyboardButton(text="Фарм и золото", callback_data='zxcvb')
        button4 = types.InlineKeyboardButton(text="Командная работа", callback_data='zxcvbn')
        button_back2 = types.InlineKeyboardButton(text="Назад", callback_data='back_to_sovet')
        markupv.add(button1, button2, button3, button4, button_back2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите категорию:", reply_markup=markupv)
    elif call.data == "zxc":
        bot.answer_callback_query(call.id, "Вы выбрали первый пункт.")
        bot.send_message(call.message.chat.id,
        "\n1. Изучите роли: Каждый герой относится к определённому классу (танк, боец, маг, стрелок, ассасин, поддержка). Начните с героя, который соответствует вашему стилю игры.\n2. ""Лес: Между линиями находится лес, где можно убивать нейтральных монстров для получения золота и опыта.\n3. "
        "Синергия с командой: Выбирайте героя, который дополняет команду. Например, если в команде нет танка, возьмите героя с высокой живучестью.")
    elif call.data == "zxcv":
        bot.answer_callback_query(call.id, "Вы выбрали второй пункт.")
        bot.send_message(call.message.chat.id,
        "\n1. Линии: На карте три линии — верхняя, средняя и нижняя. Каждая линия ведёт к базам команд.\n2. ""Цели: Убивайте лордов, черепах и других нейтральных монстров, чтобы получить преимущество для команды.\n3. "
        "Башни: Башни защищают вашу базу. Уничтожайте вражеские башни, чтобы продвинуться к вражеской базе. ")
    elif call.data == "zxcvb":
        bot.answer_callback_query(call.id, "Вы выбрали третий пункт.")
        bot.send_message(call.message.chat.id,  
        "\n1. Убивайте миньонов: Миньоны — основной источник золота и опыта. Старайтесь не пропускать их.\n2. ""Лес: Между линиями находится лес, где можно убивать нейтральных монстров для получения золота и опыта.\n3. "
        "Не умирайте: Смерть лишает вас золота и опыта, а также даёт преимущество врагу.")
    elif call.data == "zxcvbn":
        bot.answer_callback_query(call.id, "Вы выбрали четвертый пункт.")
        bot.send_message(call.message.chat.id,
        "\n1. Общайтесь: Используйте чат и быстрые сообщения, чтобы координировать действия с командой.\n2. ""Помогайте союзникам: Если видите, что союзник в беде, постарайтесь помочь ему.\n3. "
        "Группируйтесь: В середине и конце игры старайтесь держаться вместе, чтобы избежать разрозненных атак.")

    elif call.data == "hero_roli":
        markupv = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton(text="Танк", callback_data='as')
        button2 = types.InlineKeyboardButton(text="Боец", callback_data='asd')
        button3 = types.InlineKeyboardButton(text="Маг", callback_data='asdf')
        button4 = types.InlineKeyboardButton(text="Стрелок", callback_data='asdfg')
        button5 = types.InlineKeyboardButton(text="Убийца", callback_data='asdfgh')
        button_back2 = types.InlineKeyboardButton(text="Назад", callback_data='back_to_sovet')
        markupv.add(button1, button2, button3, button4, button5, button_back2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите категорию:", reply_markup=markupv)
    elif call.data == "as":
        bot.answer_callback_query(call.id, "Вы выбрали первый пункт.")
        bot.send_message(call.message.chat.id,
        "Всегда находитесь впереди команды, чтобы принимать урон на себя. Используйте свои способности контроля (станы, замедления) для инициации боёв или спасения союзников. Следите за картой и помогайте союзникам, если их атакуют. Не бойтесь жертвовать собой ради спасения ключевых героев (например, стрелков или магов).")
    elif call.data == "asd":
        bot.answer_callback_query(call.id, "Вы выбрали второй пункт.")
        bot.send_message(call.message.chat.id,
        "Фокусируйтесь на фарме в начале игры, чтобы быстрее получить экипировку. Используйте свои способности для быстрого убийства вражеских героев. В боях старайтесь атаковать вражеских стрелков и магов, так как они наносят больше всего урона. Не забывайте помогать команде в захвате целей (лорд, черепаха).")
    elif call.data == "asdf":
        bot.answer_callback_query(call.id, "Вы выбрали третий пункт.")
        bot.send_message(call.message.chat.id,  
        "Держитесь на задней линии, чтобы избежать смерти. Используйте свои способности контроля (станы, замедления) для помощи команде. Фокусируйтесь на вражеских стрелках и магах, чтобы быстро их убить. Не забывайте фармить, чтобы быстрее получить ключевые предметы.")
    elif call.data == "asdfg":
        bot.answer_callback_query(call.id, "Вы выбрали четвертый пункт.")
        bot.send_message(call.message.chat.id,
        "В начале игры сосредоточьтесь на фарме, чтобы быстрее получить экипировку. Держитесь на задней линии в боях, чтобы избежать смерти. Используйте свои способности для нанесения урона и контроля врагов. В поздней игре вы становитесь ключевым героем команды, поэтому старайтесь не умирать.")
    elif call.data == "asdfgh":
        bot.answer_callback_query(call.id, "Вы выбрали четвертый пункт.")
        bot.send_message(call.message.chat.id,
        "Используйте свою мобильность для неожиданных атак. Фокусируйтесь на вражеских героях с низким уровнем здоровья. В боях старайтесь зайти с фланга или сзади, чтобы убить вражеских стрелков или магов. Не забывайте фармить, чтобы быстрее получить экипировку.")

    elif call.data == "hero_strateg":
        markupv = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton(text="Раняя игра", callback_data='nb')
        button2 = types.InlineKeyboardButton(text="Средняя игра", callback_data='nbv')
        button3 = types.InlineKeyboardButton(text="Поздняя игра", callback_data='nbvc')
        button4 = types.InlineKeyboardButton(text="Тактика для командных боев", callback_data='nbvcx')
        button_back2 = types.InlineKeyboardButton(text="Назад", callback_data='back_to_sovet')
        markupv.add(button1, button2, button3, button4, button_back2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите категорию:", reply_markup=markupv)
    elif call.data == "nb":
        bot.answer_callback_query(call.id, "Вы выбрали первый пункт.")
        bot.send_message(call.message.chat.id,
        "\n1. Фарм: Сосредоточьтесь на убийстве миньонов и нейтральных монстров, чтобы получить золото и опыт.\n2. ""Защита линии: Не рискуйте без необходимости. Держитесь ближе к своей башне, чтобы избежать ганков.\n3. "
        "Черепаха: На второй минуте появляется Черепаха. Постарайтесь захватить её, чтобы дать команде дополнительное золото.")
    elif call.data == "nbv":
        bot.answer_callback_query(call.id, "Вы выбрали второй пункт.")
        bot.send_message(call.message.chat.id,
        "\n1. Командные бои: Начинайте группироваться для командных боёв. Старайтесь не действовать в одиночку.\n2. ""Фокус на вражеских стрелках и магах: В первую очередь атакуйте вражеских героев, которые наносят больше всего урона.\n3. "
        "Лорд: После 8-й минуты появляется Лорд. Захватите его, чтобы усилить давление на вражескую базу.")
    elif call.data == "nbvc":
        bot.answer_callback_query(call.id, "Вы выбрали третий пункт.")
        bot.send_message(call.message.chat.id,  
        "\n1. База: Уничтожайте вражеские башни и казармы, чтобы ослабить вражеских миньонов.\n2. ""Лес: Между линиями находится лес, где можно убивать нейтральных монстров для получения золота и опыта.\n3. "
        "Лорд и Черепаха: Продолжайте захватывать ключевые цели, чтобы усилить давление на врага.")
    elif call.data == "nbvcx":
        bot.answer_callback_query(call.id, "Вы выбрали четвертый пункт.")
        bot.send_message(call.message.chat.id,
        "\n1. Защита ключевых героев: Защищайте своих стрелков и магов, так как они наносят основной урон. \n2. ""Инициация: Если вы играете за танка или бойца, инициируйте бой, используя свои способности контроля.\n3. "
        "Отступление: Если бой проигран, отступайте, чтобы не дать врагу дополнительное золото и опыт.")

    elif call.data == "hero_novich":
        markupv = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton(text="Танки", callback_data='gf')
        button2 = types.InlineKeyboardButton(text="Бойцы", callback_data='gfd')
        button3 = types.InlineKeyboardButton(text="Маги", callback_data='gfds')
        button4 = types.InlineKeyboardButton(text="Стрелки", callback_data='gfdsa')
        button5 = types.InlineKeyboardButton(text="Убийцы", callback_data='gfdsaq')
        button_back2 = types.InlineKeyboardButton(text="Назад", callback_data='back_to_sovet')
        markupv.add(button1, button2, button3, button4, button_back2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите категорию:", reply_markup=markupv)
    elif call.data == "gf":
        bot.answer_callback_query(call.id, "Вы выбрали первый пункт.")
        bot.send_message(call.message.chat.id,
        "Танки слабые против: Героев с пронзанием брони (например Керии, Клауд) и магов с высоким уроном (например Эйдора, Аврора).\n"
        "Контрпики: Акай: Его ульт может отталкивать врагов, что полезно против героев, которые полагаются на позиционирование (например Лейла, Мия). Грок: Его способности наносят урон и контролируют врагов, что полезно против магов и стрелков.")
    elif call.data == "gfd":
        bot.answer_callback_query(call.id, "Вы выбрали второй пункт.")
        bot.send_message(call.message.chat.id,
        "Бойцы слабые против: Героев с контролем (например Аврора, Тигрил) и героев с высоким уроном (например Госсен, Ланселот).\n"
        "Контрпики: Чу: Его способности позволяют ему уклоняться от атак и контролировать врагов, что полезно против бойцов и ассасинов. Чонг: Его ульт позволяет ему врываться в бой и наносить урон по области, что полезно против групп врагов.")
    elif call.data == "gfds":
        bot.answer_callback_query(call.id, "Вы выбрали третий пункт.")
        bot.send_message(call.message.chat.id,  
        "Маги слабые против: Героев с высокой мобильностью (например Госсен, Ланселот) и героев с защитой от магического урона (например Атлас, Грок).\n"
        "Контрпики: Эйдора: Её способности позволяют быстро убивать вражеских героев, что полезно против магов и стрелков. Кагура: Её мобильность и контроль позволяют ей эффективно противостоять другим магам.")
    elif call.data == "gfdsa":
        bot.answer_callback_query(call.id, "Вы выбрали четвертый пункт.")
        bot.send_message(call.message.chat.id,
        "Стрелки слабые против: Героев (например Инь, Хаябуса) и героев с контролем (например Кармила, Тигрил).\n"
        "Контрпики: Клауд: Его мобильность и урон позволяют ему эффективно противостоять другим стрелкам. Ван-Ван: Её способности позволяют ей уклоняться от атак и быстро убивать врагов.")
    elif call.data == "gfdsaq":
        bot.answer_callback_query(call.id, "Вы выбрали четвертый пункт.")
        bot.send_message(call.message.chat.id,
        "Убийцы слабые против: Танков (например Франко, Джонсон) и героев с контролем (например Вексана, Силена).\n"
        "Контрпики: Сабер: Его способности позволяют ему быстро убивать вражеских героев, что полезно против убийц и магов. Хаябуса: Его мобильность и урон позволяют ему эффективно противостоять другим убийцам.")
    elif call.data == "back_to_sovet":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                             text="Возвращаемся в главное меню.", reply_markup=None)
        
@bot.message_handler(func=lambda message: message.text == "Новости")
def send_statistics(message):
    bot.reply_to(message, "Вы можете узнать статистику на сайте: [Mobile Legends Stats](https://www.mobilelegends.com/stats)", parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Извините, я не понимаю. Выберите одну из кнопок.")

bot.polling(none_stop=True)
