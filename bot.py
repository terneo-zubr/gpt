
import telebot
import openai

# Токены
TELEGRAM_TOKEN = "7625632118:AAEHZjesJZ64vQ6fQJlsmnXZJg72z5hERrc"
OPENAI_API_KEY = "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"

bot = telebot.TeleBot("{625632118:AAEHZjesJZ64vQ6fQJlsmnXZJg72z5hERrc")
openai.api_key = "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"

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

