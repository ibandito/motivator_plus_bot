from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import logging

# Твій Telegram Token (уже вставлено)
API_TOKEN = "7458160287:AAFn3FNZHGr8wQBTV-eKL9YmzeaDi-7Gm8Y"

# Увімкнення логів
logging.basicConfig(level=logging.INFO)

# Ініціалізація бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Стартова команда /start з кнопками
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        KeyboardButton("🔥 Самомотивація"),
        KeyboardButton("🎯 Цілі та фокус")
    )
    keyboard.add(
        KeyboardButton("💪 Сила волі"),
        KeyboardButton("💡 Натхнення")
    )
    await message.answer("Привіт! Обери категорію мотивації:", reply_markup=keyboard)

# Обробники повідомлень-кнопок
@dp.message_handler(lambda message: message.text == "🔥 Самомотивація")
async def handle_self_motivation(message: types.Message):
    await message.answer("🔥 Ти — головна сила свого успіху. Дій!")

@dp.message_handler(lambda message: message.text == "🎯 Цілі та фокус")
async def handle_goals(message: types.Message):
    await message.answer("🎯 Зосередься на одному, але важливому кроці сьогодні.")

@dp.message_handler(lambda message: message.text == "💪 Сила волі")
async def handle_willpower(message: types.Message):
    await message.answer("💪 Роби навіть тоді, коли не хочеться. Саме тоді з’являється сила.")

@dp.message_handler(lambda message: message.text == "💡 Натхнення")
async def handle_inspiration(message: types.Message):
    await message.answer("💡 Натхнення не чекають — його створюють. Створи свій шанс.")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
