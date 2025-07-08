import logging
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '7458160287:AAFn3FNZHGr8wQBTV-eKL9YmzeaDi-7Gm8Y'

# Налаштування логування
logging.basicConfig(level=logging.INFO)

# Ініціалізація бота та диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Завантаження цитат з файлу
with open("quotes.txt", "r", encoding="utf-8") as file:
    quotes = [line.strip() for line in file if line.strip() and not line.startswith('#')]

# Клавіатура з кнопкою внизу
reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("💪 Мотивуй мене!")
)

# /start — надсилає вітання з кнопкою
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привіт! Я готовий тебе мотивувати! Натисни кнопку 👇", reply_markup=reply_keyboard)

# Обробка натискання кнопки-клавіші
@dp.message_handler(lambda message: message.text == "💪 Мотивуй мене!")
async def send_quote(message: types.Message):
    quote = random.choice(quotes)
    await message.answer(quote)

# Запуск
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)