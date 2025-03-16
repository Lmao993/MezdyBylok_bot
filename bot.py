import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from flask import Flask
from dotenv import load_dotenv
from threading import Thread

# Логирование
logging.basicConfig(level=logging.INFO)

# Загружаем переменные окружения
load_dotenv()  

# Получаем токен из переменной окружения
TOKEN = os.getenv("8019210319:AAEkPi_tpqON8PoKY563Dq3XpL_tHV5o6pM")

if not TOKEN:
    logging.error("⚠️ ОШИБКА: Переменная окружения BOT_TOKEN не установлена!")
    raise ValueError("⚠️ BOT_TOKEN отсутствует! Установите его в настройках Render.")

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

