from flask import Flask, request
from telegram import Bot, Update

# Инициализация Flask
app = Flask(__name__)

# Telegram токен
BOT_TOKEN = "7625632118:AAEHZjesJZ64vQ6fQJlsmnXZJg72z5hERrc"
bot = Bot(token=BOT_TOKEN)

# Обработка вебхуков
@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(), bot)
    if update.message:
        chat_id = update.message.chat_id
        bot.send_message(chat_id=chat_id, text="Привет!")
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
