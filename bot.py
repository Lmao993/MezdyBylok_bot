import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
import logging
import os

TOKEN = os.getenv("BOT_TOKEN")  # Храним токен в переменных окружения

bot = Bot(token=TOKEN)
dp = Dispatcher()  # Теперь Dispatcher создается без аргументов


@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Привет! Я твой бот на aiogram 3.x")


@dp.message(Command("инфа"))
async def info_handler(message: Message):
    user = message.from_user
    text = (f"*Имя:* {user.first_name} {user.last_name or ''}\n"
            f"*Юзернейм:* @{user.username or '—'}\n"
            f"*ID:* {user.id}\n"
            f"*Длительность в чате:* неизвестно (нужно дописать логику)")
    await message.answer_photo(photo=user.photo, caption=text, parse_mode="Markdown")


async def main():
    dp.include_router(dp)  # Подключаем обработчики
    await bot.delete_webhook(drop_pending_updates=True)  # Чистим апдейты
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())

