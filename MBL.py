import telebot
from telebot import types

# Замените 'YOUR_TOKEN_HERE' на токен вашего бота
TOKEN = '7888824558:AAEgA4rSbMuuAoX3LJO1I8f-WqNN9cs8EFc'
bot = telebot.TeleBot(TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать в бот Mobile Legends! Выберите опцию ниже.", reply_markup=main_menu())

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    butt1 = types.KeyboardButton("Герои")
    butt2 = types.KeyboardButton("События")
    butt3 = types.KeyboardButton("Советы")
    butt4 = types.KeyboardButton("Статистика")
    markup.add(butt1, butt2, butt3, butt4)
    return markup
@bot.message_handler(func=lambda message: message.text == "Герои")
def send_heroes(message):
    bot.reply_to(message, "Вот список метовых персонажей: \n1. Убийцы \n2. Лейла \n3. Миа \n4. Гатоткача")

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'btn1':
        bot.send_message(callback.message.chat.id, 'Хаябуса')
@bot.message_handler(func=lambda message: message.text == "События")
def send_events(message):
    bot.reply_to(message, "Сейчас идут следующие события: \n- Событие релиза нового героя \n- Праздничные акции")

@bot.message_handler(func=lambda message: message.text == "Советы")
def send_tips(message):
    bot.reply_to(message, "Советы для начинающих:\n1. Изучите всех героев\n2. Играйте с друзьями\n3. Постоянно улучшайте навыки")

@bot.message_handler(func=lambda message: message.text == "Статистика")
def send_statistics(message):
    bot.reply_to(message, "Вы можете узнать статистику на сайте: [Mobile Legends Stats](https://www.mobilelegends.com/stats)")

# Обработка неизвестных команд
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Извините, я не понимаю. Выберите одну из кнопок.")

# Запуск бота
bot.polling()