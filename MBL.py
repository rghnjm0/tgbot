import telebot
from telebot import types

bot = telebot.TeleBot('7888824558:AAEgA4rSbMuuAoX3LJO1I8f-WqNN9cs8EFc')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать в бот Mobile Legends! Выберите опцию ниже.", reply_markup=main_menu())

def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton('Герои')
    button2 = types.KeyboardButton('Снаряжение')
    button3 = types.KeyboardButton('Советы')
    button4 = types.KeyboardButton('Статистика')
    markup.add(button1, button2, button3, button4)
    return markup

@bot.message_handler(func=lambda message: message.text == "Герои")
def handle_heroes(message):
    otvet = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton("Убийцы", callback_data='hero_assassin')
    button2 = types.InlineKeyboardButton("Стрелки", callback_data='hero_marksman')
    button3 = types.InlineKeyboardButton("Маги", callback_data='hero_mage')
    button4 = types.InlineKeyboardButton("Роум", callback_data='hero_roam')
    button5 = types.InlineKeyboardButton("Боец", callback_data='hero_fighter')
    otvet.add(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id, "Вот список метовых персонажей", reply_markup=otvet)

@bot.message_handler(func=lambda message: message.text == "Снаряжение")
def handle_equipment(message):
    otvedd = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton("Атака", callback_data='equip_attack')
    button2 = types.InlineKeyboardButton("Магия", callback_data='equip_magic')
    button3 = types.InlineKeyboardButton("Защита", callback_data='equip_defense')
    button4 = types.InlineKeyboardButton("Передвижение", callback_data='equip_movement')
    otvedd.add(button1, button2, button3, button4)
    bot.send_message(message.chat.id, "Вот несколько снаряжений", reply_markup=otvedd)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == "hero_assassin":
                bot.send_message(call.message.chat.id, "\n1. Хаябуса \n2. Джой \n3. Су-е \n4. Фани \n5. Ланселот")
            elif call.data == "hero_marksman":
                bot.send_message(call.message.chat.id, "\n1. Беатрис \n2. Лейла \n3. Бруно \n4. Гренджер \n5. Москов")
            elif call.data == "hero_mage":
                bot.send_message(call.message.chat.id, "\n1. Джусинь \n2. Харит \n3. Ксавьер \n4. Ив \n5. Сесилион")
            elif call.data == "hero_roam":
                bot.send_message(call.message.chat.id, "\n1. Гатоткача  \n2. Чу \n3. Чип \n4. Хильда \n5. Хилос")
            elif call.data == "hero_fighter":
                bot.send_message(call.message.chat.id, "\n1. Баданг \n2. Лукас \n3. Глу \n4. Сан \n5. Халид")
            elif call.data == "equip_attack":
                bot.send_message(call.message.chat.id, "\n1. Меч Хаоса \n2. Лезвие Отчаяния \n3. Клинок Семи Ветров")
            elif call.data == "equip_magic":
                bot.send_message(call.message.chat.id, "\n1. Светящийся Жезл \n2. Чары Господства \n3. Книга Мертвых")
            elif call.data == "equip_defense":
                bot.send_message(call.message.chat.id, "\n1. Щит Атласа \n2. Броня Анти-Магии \n3. Шлем Бессмертия")
            elif call.data == "equip_movement":
                bot.send_message(call.message.chat.id, "\n1. Ботинки Странника \n2. Ботинки Волшебника \n3. Ботинки Воина")
    except Exception as e:
        print(repr(e))
        bot.send_message(call.message.chat.id, "Произошла ошибка. Пожалуйста, попробуйте снова.")

@bot.message_handler(func=lambda message: message.text == "События")
def send_events(message):
    bot.reply_to(message, "Сейчас идут следующие события: \n- Событие релиза нового героя \n- Праздничные акции")

@bot.message_handler(func=lambda message: message.text == "Советы")
def send_tips(message):
    bot.reply_to(message, "Советы для начинающих:\n1. Изучите всех героев\n2. Играйте с друзьями\n3. Постоянно улучшайте навыки")

@bot.message_handler(func=lambda message: message.text == "Статистика")
def send_statistics(message):
    bot.reply_to(message, "Вы можете узнать статистику на сайте: [Mobile Legends Stats](https://www.mobilelegends.com/stats)", parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Извините, я не понимаю. Выберите одну из кнопок.")

# Запуск бота
bot.polling(none_stop=True)