import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

# Логирование
logging.basicConfig(level=logging.INFO)

# Получаем токен из переменной окружения
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    logging.error("⚠️ ОШИБКА: Переменная окружения BOT_TOKEN не установлена!")
    raise ValueError("⚠️ BOT_TOKEN отсутствует! Установите его в настройках Render.")

bot = Bot(token=TOKEN)
dp = Dispatcher()  # Исправил тут

# Обработчик команды /start
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Я твой Telegram-бот!")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logging.error(f"🔥 ОШИБКА В БОТЕ: {e}")



if __name__ == "__main__":
    asyncio.run(main())

