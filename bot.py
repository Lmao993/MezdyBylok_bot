import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from flask import Flask
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Выводим все переменные окружения (для отладки)
print("Переменные окружения:", os.environ)
print("BOT_TOKEN из os.environ:", os.environ.get("BOT_TOKEN"))
print("BOT_TOKEN через os.getenv:", os.getenv("BOT_TOKEN"))

# Получаем токен
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    logging.error("⚠️ ОШИБКА: Переменная окружения BOT_TOKEN не установлена!")
    raise ValueError("⚠️ BOT_TOKEN отсутствует! Установите его в Render.")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Flask-приложение
app = Flask(__name__)

@app.route('/')
def home():
    return "Бот работает!"

# Обработчик команды /start
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Я твой Telegram-бот!")

async def main():
    port = int(os.environ.get("PORT", 5000))  # Получаем порт от Render
    loop = asyncio.get_running_loop()

    # Запускаем Flask-сервер в фоне
    from threading import Thread
    def run_flask():
        app.run(host="0.0.0.0", port=port)

    flask_thread = Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Запускаем бота
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())

