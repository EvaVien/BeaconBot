# Основной файл запуска бота

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Мне тревожно", callback_data='anxious')],
        [InlineKeyboardButton("Мне одиноко", callback_data='lonely')],
        [InlineKeyboardButton("Просто поговорить", callback_data='talk')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Чем могу помочь?", reply_markup=reply_markup)

async def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text.lower()
    if 'тревожно' in user_message:
        await update.message.reply_text("Давай поговорим. Ты не один.")
    elif 'одиноко' in user_message:
        await update.message.reply_text("Я здесь, ты не один!")
    else:
        await update.message.reply_text("Что бы ты хотел обсудить?")

async def main():
    application = ApplicationBuilder().token("YOUR_TOKEN").build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    application.add_handler(message_handler)

    print("Бот работает!")
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
