from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

def userinfo(update: Update, context: CallbackContext):
    user = update.effective_user

    # Для демонстрации: считаем, что пользователь находится в чате с момента 30 дней назад.
    join_date = update.message.date - datetime.timedelta(days=30)
    duration = datetime.datetime.now(datetime.timezone.utc) - join_date
    duration_str = str(duration).split('.')[0]  # убираем микросекунды

    # Формируем HTML-сообщение с данными пользователя
    caption = (
        f"<b>{user.first_name} {user.last_name if user.last_name else ''}</b>\n"
        f"<i>Юзернейм:</i> @{user.username if user.username else 'Нет'}\n"
        f"<i>ID:</i> {user.id}\n"
        f"<i>Длительность нахождения в чате:</i> {duration_str}"
    )

    # Пытаемся получить фото профиля пользователя
    photos = context.bot.get_user_profile_photos(user.id)
    if photos.total_count > 0:
        # Используем последнее (наиболее качественное) фото из первого набора
        photo_file_id = photos.photos[0][-1].file_id
        context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=photo_file_id,
            caption=caption,
            parse_mode=ParseMode.HTML
        )
    else:
        # Если фото отсутствует — отправляем текст
        update.message.reply_text(text=caption, parse_mode=ParseMode.HTML)

def main():
    # Замените 'YOUR_BOT_TOKEN' на токен вашего бота
    updater = Updater(8019210319:AAEkPi_tpqON8PoKY563Dq3XpL_tHV5o6pM)
    dp = updater.dispatcher

    # Регистрируем обработчик команды /userinfo
    dp.add_handler(CommandHandler("userinfo", userinfo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
