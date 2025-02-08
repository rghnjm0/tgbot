import telebot
from telebot import types

bot = telebot.TeleBot('Token')  # Замените на ваш токен

# Главное меню
def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton('Герои')
    button2 = types.KeyboardButton('Снаряжение')
    button3 = types.KeyboardButton('Советы')
    button4 = types.KeyboardButton('Статистика')
    markup.add(button1, button2, button3, button4)
    return markup

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать в бот Mobile Legends! Выберите опцию ниже.", reply_markup=main_menu())

# Обработчик кнопки "Герои"
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

# Обработчик кнопки "Снаряжение"
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

# Обработчик callback-запросов
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "hero_assassin":
        # Создаем новую клавиатуру с дополнительной кнопкой
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
        with open('xaybusa.JPG','rb') as f:
            bot.send_photo(chat_id=call.message.chat.id, photo=f)

    elif call.data == "hero_joi":
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Джой — это герой-убийца с уникальными способностями.",
                             reply_markup=None)
    elif call.data == "hero_sye":
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="СУ-е — это герой-убийца с мощными комбо.",
                             reply_markup=None)
    elif call.data == "hero_fanny":
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Фанни — это герой-убийца с высокой сложностью управления.",
                             reply_markup=None)
    elif call.data == "hero_lanselot":
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Ланселот — это герой-убийца с высокой мобильностью и уроном.",
                             reply_markup=None)
    elif call.data == "back_to_heroes":
        # Возвращаемся к списку героев
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
        # Возвращаемся в главное меню
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
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Хаябуса — это герой-убийца с высокой мобильностью.",
                             reply_markup=None)
    elif call.data == "hero_beatris":
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Джой — это герой-убийца с уникальными способностями.",
                             reply_markup=None)
    elif call.data == "hero_van-van":
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="СУ-е — это герой-убийца с мощными комбо.",
                             reply_markup=None)
    elif call.data == "hero_bruno":
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Фанни — это герой-убийца с высокой сложностью управления.",
                             reply_markup=None)
    elif call.data == "hero_notan":
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Ланселот — это герой-убийца с высокой мобильностью и уроном.",
                             reply_markup=None)
    elif call.data == "back_to_heroes":
        # Возвращаемся к списку героев
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
        # Возвращаемся в главное меню
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
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Хаябуса — это герой-убийца с высокой мобильностью.",
                             reply_markup=None)
    elif call.data == "hero_xarit":
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Джой — это герой-убийца с уникальными способностями.",
                             reply_markup=None)
    elif call.data == "hero_ksava":
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="СУ-е — это герой-убийца с мощными комбо.",
                             reply_markup=None)
    elif call.data == "hero_iv":
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Фанни — это герой-убийца с высокой сложностью управления.",
                             reply_markup=None)
    elif call.data == "hero_sesilion":
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Ланселот — это герой-убийца с высокой мобильностью и уроном.",
                             reply_markup=None)
    elif call.data == "back_to_heroes":
        # Возвращаемся к списку героев
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
        # Возвращаемся в главное меню
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
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Хаябуса — это герой-убийца с высокой мобильностью.",
                             reply_markup=None)
    elif call.data == "hero_chip":
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Джой — это герой-убийца с уникальными способностями.",
                             reply_markup=None)
    elif call.data == "hero_xilos":
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="СУ-е — это герой-убийца с мощными комбо.",
                             reply_markup=None)
    elif call.data == "hero_xilda":
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Фанни — это герой-убийца с высокой сложностью управления.",
                             reply_markup=None)
    elif call.data == "hero_chy":
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Ланселот — это герой-убийца с высокой мобильностью и уроном.",
                             reply_markup=None)
    elif call.data == "back_to_heroes":
        # Возвращаемся к списку героев
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
        # Возвращаемся в главное меню
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Возвращаемся в главное меню.",
            reply_markup=None)
        
    elif call.data == "hero_fighter":
        markup = types.InlineKeyboardMarkup(row_width=2)
        button1 = types.InlineKeyboardButton("Баданг", callback_data='hero_badang')
        button2 = types.InlineKeyboardButton("Лукас", callback_data='hero_lucas')
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
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Хаябуса — это герой-убийца с высокой мобильностью.",
                             reply_markup=None)
    elif call.data == "hero_lucas":
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Джой — это герой-убийца с уникальными способностями.",
                             reply_markup=None)
    elif call.data == "hero_glu":
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="СУ-е — это герой-убийца с мощными комбо.",
                             reply_markup=None)
    elif call.data == "hero_san":
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Фанни — это герой-убийца с высокой сложностью управления.",
                             reply_markup=None)
    elif call.data == "hero_halid":
        bot.edit_message_text(chat_id=call.message.chat.id,
                             message_id=call.message.message_id,
                             text="Ланселот — это герой-убийца с высокой мобильностью и уроном.",
                             reply_markup=None)
    elif call.data == "back_to_heroes":
        # Возвращаемся к списку героев
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
        # Возвращаемся в главное меню
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Возвращаемся в главное меню.",
            reply_markup=None
        )
# Обработчик кнопки "Советы"
@bot.message_handler(func=lambda message: message.text == "Советы")
def send_tips(message):
    bot.reply_to(message, "Советы для начинающих:\n1. Изучите всех героев\n2. Играйте с друзьями\n3. Постоянно улучшайте навыки")

# Обработчик кнопки "Статистика"
@bot.message_handler(func=lambda message: message.text == "Статистика")
def send_statistics(message):
    bot.reply_to(message, "Вы можете узнать статистику на сайте: [Mobile Legends Stats](https://www.mobilelegends.com/stats)", parse_mode="Markdown")

# Обработчик неизвестных команд
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Извините, я не понимаю. Выберите одну из кнопок.")

# Запуск бота
bot.polling(none_stop=True)
