import logging
import random
import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from apscheduler.schedulers.asyncio import AsyncIOScheduler

API_TOKEN = API_TOKEN = "7458160287:AAFn3FNZHGr8wQBTV-eKL9YmzeaDi-7Gm8Y"

ADMIN_ID = 217716970

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
scheduler = AsyncIOScheduler()

conn = sqlite3.connect('subscribers.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS subscribers (user_id INTEGER PRIMARY KEY)''')
conn.commit()

cursor.execute("INSERT OR IGNORE INTO subscribers (user_id) VALUES (?)", (ADMIN_ID,))
conn.commit()

def get_random_quote():
    with open("quotes.txt", encoding="utf-8") as f:
        quotes = f.readlines()
    return random.choice(quotes).strip()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привіт! Я — Мотиватор+ 💪\n/мотивуй\n/підписка\n/відписка")

@dp.message_handler(commands=['мотивуй'])
async def motivate(message: types.Message):
    quote = get_random_quote()
    await message.reply(f"💥 {quote}")

@dp.message_handler(commands=['підписка'])
async def subscribe(message: types.Message):
    user_id = message.from_user.id
    cursor.execute("INSERT OR IGNORE INTO subscribers (user_id) VALUES (?)", (user_id,))
    conn.commit()
    await message.reply("🔔 Ти підписався на щоденну мотивацію!")

@dp.message_handler(commands=['відписка'])
async def unsubscribe(message: types.Message):
    user_id = message.from_user.id
    cursor.execute("DELETE FROM subscribers WHERE user_id = ?", (user_id,))
    conn.commit()
    await message.reply("❌ Ти відписався.")

async def send_daily_quotes():
    cursor.execute("SELECT user_id FROM subscribers")
    users = cursor.fetchall()
    quote = get_random_quote()
    for (user_id,) in users:
        try:
            await bot.send_message(user_id, f"🌞 Добрий ранок!\n💡 {quote}")
        except Exception as e:
            logging.error(f"Не вдалося надіслати {user_id}: {e}")

if __name__ == '__main__':
    scheduler.add_job(send_daily_quotes, 'interval', hours=24)
    scheduler.start()
    executor.start_polling(dp, skip_updates=True)
