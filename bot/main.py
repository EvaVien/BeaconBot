from telegram.ext import ApplicationBuilder, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я здесь, чтобы тебя выслушать.")

def main():
    token = os.getenv("TOKEN")
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()  # Без async/await — Render будет доволен!

if __name__ == "__main__":
    main()