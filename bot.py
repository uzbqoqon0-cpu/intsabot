import asyncio
import os
import yt_dlp
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, FSInputFile

API_TOKEN = "8160786685:AAGtvjo5UHG7OpxwXwvAn1QoWcMgtX6c_lM"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()

@router.message(lambda msg: msg.text == "/start")
async def start(message: Message):
    await message.answer("Salom 👋 Menga Instagram link yuboring, men sizga yuklab beraman 📥")

@router.message()
async def download_instagram(message: Message):
    url = message.text.strip()

    if "instagram.com" not in url:
        await message.answer("❌ Bu Instagram link emas!")
        return

    await message.answer("⏳ Yuklanmoqda... kuting.")

    try:
        filename = "insta.%(ext)s"
        ydl_opts = {
            "outtmpl": filename,
            "format": "mp4/best",
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

        # FSInputFile orqali yuboramiz
        video = FSInputFile(file_path)
        await message.answer_video(video=video, caption="✅ Yuklab olindi!")

        os.remove(file_path)  # yuborilgandan keyin o‘chiramiz

    except Exception as e:
        await message.answer(f"⚠️ Xatolik: {e}")

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
