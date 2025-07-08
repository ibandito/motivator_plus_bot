import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

API_TOKEN = '7458160287:AAFn3FNZHGr8wQBTV-eKL9YmzeaDi-7Gm8Y'

# Налаштування логування
logging.basicConfig(level=logging.INFO)

# Ініціалізація бота та диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Завантаження всіх цитат з файлу (ігноруємо порожні рядки та теги)
with open("quotes.txt", "r", encoding="utf-8") as file:
    quotes = [line.strip() for line in file if line.strip() and not line.startswith('#')]

# Одна кнопка
keyboard = InlineKeyboardMarkup().add(
    InlineKeyboardButton("💪 Мотивуй мене!", callback_data="motivate")
)

# /start — привітання з кнопкою
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привіт! Натисни кнопку, щоб отримати мотивацію 👇", reply_markup=keyboard)

# Обробка натискання кнопки
@dp.callback_query_handler(lambda c: c.data == 'motivate')
async def process_motivation(callback_query: types.CallbackQuery):
    quote = random.choice(quotes)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, quote)

# Запуск
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)