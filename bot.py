import logging
import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.types import InputFile
from aiogram.utils import executor

# Токен бота (замени на свой)
TOKEN = "8019210319:AAEkPi_tpqON8PoKY563Dq3XpL_tHV5o6pM"

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Логирование (для отладки)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=["инфа"])
async def send_user_info(message: types.Message):
    user = message.from_user
    chat = await bot.get_chat_member(message.chat.id, user.id)
    
    # Получаем дату входа пользователя в чат
    if chat.joined_date:
        join_date = datetime.datetime.utcfromtimestamp(chat.joined_date).strftime('%Y-%m-%d %H:%M:%S')
        duration = (datetime.datetime.utcnow() - datetime.datetime.utcfromtimestamp(chat.joined_date)).days
    else:
        join_date = "Неизвестно"
        duration = "Неизвестно"

    # Получаем фото профиля
    photos = await bot.get_user_profile_photos(user.id)
    
    if photos.photos:
        photo_id = photos.photos[0][-1].file_id  # Берём последнюю загруженную фотографию
        await bot.send_photo(
            chat_id=message.chat.id, 
            photo=photo_id,
            caption=f"👤 *Информация о пользователе:*\n"
                    f"🔹 *Имя:* {user.first_name} {user.last_name or ''}\n"
                    f"🔹 *Юзернейм:* @{user.username or 'Нет'}\n"
                    f"🔹 *ID:* {user.id}\n"
                    f"🔹 *Дата входа в чат:* {join_date}\n"
                    f"🔹 *Дней в чате:* {duration}",
            parse_mode="Markdown"
        )
    else:
        await message.reply(
            f"👤 *Информация о пользователе:*\n"
            f"🔹 *Имя:* {user.first_name} {user.last_name or ''}\n"
            f"🔹 *Юзернейм:* @{user.username or 'Нет'}\n"
            f"🔹 *ID:* {user.id}\n"
            f"🔹 *Дата входа в чат:* {join_date}\n"
            f"🔹 *Дней в чате:* {duration}",
            parse_mode="Markdown"
        )

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
