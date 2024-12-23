import telebot

TOKEN = "твой_токен_бота"
bot = telebot.TeleBot("7625632118:AAEHZjesJZ64vQ6fQJlsmnXZJg72z5hERrc")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я Telegram-бот.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
