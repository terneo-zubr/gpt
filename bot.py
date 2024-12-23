

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Функция для старта бота
def start(update, context):
    # Создаем клавиатуру с кнопками
    keyboard = [
        [InlineKeyboardButton("Кнопка 1", callback_data='1')],
        [InlineKeyboardButton("Кнопка 2", callback_data='2')],
        [InlineKeyboardButton("Кнопка 3", callback_data='3')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text('Выберите кнопку:', reply_markup=reply_markup)

# Обработчик нажатий на кнопки
def button(update, context):
    query = update.callback_query
    query.answer()  # Отвечаем на запрос
    query.edit_message_text(text=f"Вы нажали кнопку {query.data}")

def main():
    # Здесь вставь свой токен от бота
    updater = Updater("7625632118:AAEHZjesJZ64vQ6fQJlsmnXZJg72z5hERrc", use_context=True)
    
    # Регистрируем обработчики
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


