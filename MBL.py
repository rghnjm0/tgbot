import telebot
from telebot import types

bot = telebot.TeleBot('Token')

def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton('Герои')
    button2 = types.KeyboardButton('Снаряжение')
    button3 = types.KeyboardButton('Советы')
    button4 = types.KeyboardButton('Статистика')
    markup.add(button1, button2, button3, button4)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать в бот Mobile Legends! Выберите опцию ниже.", reply_markup=main_menu())

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
    bot.send_message(message.chat.id, "Вот список метовых персонажей", reply_markup=otvet)

@bot.message_handler(func=lambda message: message.text == "Снаряжение")
def handle_equipment(message):
    otvedd = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton("Атака", callback_data='equip_attack')
    button2 = types.InlineKeyboardButton("Магия", callback_data='equip_magic')
    button3 = types.InlineKeyboardButton("Защита", callback_data='equip_defense')
    button4 = types.InlineKeyboardButton("Передвижение", callback_data='equip_movement')
    button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_main')
    otvedd.add(button1, button2, button3, button4, button_back)
    bot.send_message(message.chat.id, "Вот несколько снаряжений", reply_markup=otvedd)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "hero_assassin":
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Хаябуса", callback_data='hero_hayabusa')
        button2 = types.InlineKeyboardButton("Джой", callback_data='hero_joi')
        button3 = types.InlineKeyboardButton("СУ-е", callback_data='hero_sye')
        button4 = types.InlineKeyboardButton("Фанни", callback_data='hero_fanny')
        button5 = types.InlineKeyboardButton("Ланселот", callback_data='hero_lanselot')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup.add(button1, button2, button3, button4, button5, button_back)
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Вы выбрали топ 5 Убийц. Вот список:",
                             reply_markup=markup)
    elif call.data == "hero_hayabusa":
        media = [types.InputMediaPhoto(open('piki/Xay1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/Xay2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/Xay3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)

    elif call.data == "hero_joi":
        media = [types.InputMediaPhoto(open('piki/djo1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/djo2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/djo3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
        
    elif call.data == "hero_sye":
        media = [types.InputMediaPhoto(open('piki/Sye1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/Sye2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/Sye3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
    elif call.data == "hero_fanny":
        media = [types.InputMediaPhoto(open('piki/fan1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/fan2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/fan3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
    elif call.data == "hero_lanselot":
        media = [types.InputMediaPhoto(open('piki/lans1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/lans2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/lans3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
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
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Грейнджер", callback_data='hero_greyndger')
        button2 = types.InlineKeyboardButton("Беатрис", callback_data='hero_beatris')
        button3 = types.InlineKeyboardButton("Ван-Ван", callback_data='hero_van-van')
        button4 = types.InlineKeyboardButton("Бруно", callback_data='hero_bruno')
        button5 = types.InlineKeyboardButton("Нотан", callback_data='hero_notan')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup.add(button1, button2, button3, button4, button5, button_back)
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Вы выбрали топ 5 Стрелков. Вот список:",
                             reply_markup=markup)
    elif call.data == "hero_greyndger":
        media = [types.InputMediaPhoto(open('piki/gren1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/gren2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/gren3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
    elif call.data == "hero_beatris":
        media = [types.InputMediaPhoto(open('piki/beat1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/beat2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/beat3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
    elif call.data == "hero_van-van":
        media = [types.InputMediaPhoto(open('piki/van1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/van2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/van3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
    elif call.data == "hero_bruno":
        media = [types.InputMediaPhoto(open('piki/bru1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/bru2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/bru3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
    elif call.data == "hero_notan":
        media = [types.InputMediaPhoto(open('piki/nott1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/nott2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/nott3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
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
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Джусинь", callback_data='hero_dchysin')
        button2 = types.InlineKeyboardButton("Харит", callback_data='hero_xarit')
        button3 = types.InlineKeyboardButton("Ксавьер", callback_data='hero_ksava')
        button4 = types.InlineKeyboardButton("Ив", callback_data='hero_iv')
        button5 = types.InlineKeyboardButton("Сесилион", callback_data='hero_sesilion')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup.add(button1, button2, button3, button4, button5, button_back)
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Вы выбрали топ 5 магов. Вот список:",
                             reply_markup=markup)
    elif call.data == "hero_dchysin":
        media = [types.InputMediaPhoto(open('piki/dchys1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/dchys2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/dchys3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
    elif call.data == "hero_xarit":
        media = [types.InputMediaPhoto(open('piki/xarit1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/xarit2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/xarit3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
    elif call.data == "hero_ksava":
        media = [types.InputMediaPhoto(open('piki/ksava1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/ksava2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/ksava3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
    elif call.data == "hero_iv":
        media = [types.InputMediaPhoto(open('piki/iv1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/iv2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/iv3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
    elif call.data == "hero_sesilion":
        media = [types.InputMediaPhoto(open('piki/sesi1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/sesi2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/sesi3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
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
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Гатоткача", callback_data='hero_gatot')
        button2 = types.InlineKeyboardButton("Чип", callback_data='hero_chip')
        button3 = types.InlineKeyboardButton("Хилос", callback_data='hero_xilos')
        button4 = types.InlineKeyboardButton("Хильда", callback_data='hero_xilda')
        button5 = types.InlineKeyboardButton("Чу", callback_data='hero_chy')
        button_back = types.InlineKeyboardButton("Назад", callback_data='back_to_heroes')
        markup.add(button1, button2, button3, button4, button5, button_back)
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Вы выбрали топ 5 роум. Вот список:",
                             reply_markup=markup)
    elif call.data == "hero_gatot":
        media = [types.InputMediaPhoto(open('piki/gat1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/gat2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/gat3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
    elif call.data == "hero_chip":
        media = [types.InputMediaPhoto(open('piki/chip1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/chip2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/chip3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
    elif call.data == "hero_xilos":
        media = [types.InputMediaPhoto(open('piki/xilo1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/xilo2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/xilo3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
    elif call.data == "hero_xilda":
        media = [types.InputMediaPhoto(open('piki/xilda1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/xilda2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/xilda3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
    elif call.data == "hero_chy":
        media = [types.InputMediaPhoto(open('piki/chu1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/chu2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/chu3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
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
                             text="Вы выбрали топ 5 бойцов. Вот список:",
                             reply_markup=markup)
    elif call.data == "hero_badang":
        media = [types.InputMediaPhoto(open('piki/badg1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/badg2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/badg3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
    elif call.data == "hero_lucas":
        media = [types.InputMediaPhoto(open('piki/chi1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/chi2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/chi3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
    elif call.data == "hero_glu":
        media = [types.InputMediaPhoto(open('piki/glu1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/glu2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/glu3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
    elif call.data == "hero_san":
        media = [types.InputMediaPhoto(open('piki/san1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/san2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/san3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
    elif call.data == "hero_halid":
        media = [types.InputMediaPhoto(open('piki/halid1.jpg', 'rb'), caption="Фото 1"),
            types.InputMediaPhoto(open('piki/halid2.jpg', 'rb'), caption="Фото 2"),
            types.InputMediaPhoto(open('piki/halid3.jpg', 'rb'), caption="Фото 3")]
        bot.send_media_group(call.message.chat.id, media)
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
@bot.message_handler(func=lambda message: message.text == "Советы")
def send_tips(message):
    bot.reply_to(message, "Советы для начинающих:\n1. Изучите всех героев\n2. Играйте с друзьями\n3. Постоянно улучшайте навыки")

@bot.message_handler(func=lambda message: message.text == "Статистика")
def send_statistics(message):
    bot.reply_to(message, "Вы можете узнать статистику на сайте: [Mobile Legends Stats](https://www.mobilelegends.com/stats)", parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Извините, я не понимаю. Выберите одну из кнопок.")

bot.polling(none_stop=True)
