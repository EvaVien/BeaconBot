import os
from telegram.ext import ApplicationBuilder, CommandHandler
from handlers import start

# Получаем токен и URL из переменных окружения
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = os.getenv("WEBHOOK_URL") + WEBHOOK_PATH  # Например: https://beaconbot.onrender.com/webhook

async def main():
    application = ApplicationBuilder().token(TOKEN).build()

    # Добавляем команды
    application.add_handler(CommandHandler("start", start))

    # Устанавливаем вебхук
    await application.bot.set_webhook(WEBHOOK_URL)

    # Запускаем веб-сервер на Render
    await application.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        webhook_path=WEBHOOK_PATH,
    )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())