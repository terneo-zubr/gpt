
import telebot
import openai

# Токены
TELEGRAM_TOKEN = "7625632118:AAEHZjesJZ64vQ6fQJlsmnXZJg72z5hERrc"
OPENAI_API_KEY = "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"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(func=lambda message: True)
def chat_with_gpt(message):
    try:
        # Отправляем сообщение в GPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты бот, который помогает пользователю."},
                {"role": "user", "content": message.text}
            ]
        )

        # Ответ от GPT
        reply = response['choices'][0]['message']['content']
        bot.reply_to(message, reply)

    except Exception as e:
        bot.reply_to(message, f"Упс, что-то пошло не так: {e}")

bot.polling()

