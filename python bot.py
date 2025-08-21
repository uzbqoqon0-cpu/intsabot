import logging
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = "7494256835:AAHrkgfdYaDepRn6YmgUu2NoWN6CCT4xhXg"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Menyu tugmalari (faqat Ovoz berish va Reyting)
menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✅ Ovoz berish")],
        [KeyboardButton(text="🏆 Reyting")]
    ],
    resize_keyboard=True
)

# /start komandasi
@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer(
        "Salom! Men OpenBudget botman.\nQuyidagi menyudan foydalaning 👇",
        reply_markup=menu_keyboard
    )

# ✅ Ovoz berish tugmasi
@dp.message(F.text == "✅ Ovoz berish")
async def vote_menu(message: Message):
    await message.answer("🗳 Ovoz berish uchun: https://openbudget.uz/boards/voting")

# 🏆 Reyting tugmasi
@dp.message(F.text == "🏆 Reyting")
async def reyting_menu(message: Message):
    await message.answer("🏆 Reyting hali shakllantirilmagan")

# Asosiy ishga tushirish
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
