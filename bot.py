import asyncio
import os
import yt_dlp
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message, FSInputFile
from yt_dlp.utils import DownloadError

# ✅ Telegram API token
API_TOKEN = "7851053334:AAF8AfwRJqseBC_2WGcW181FHaA_z34zfW8"

# ✅ Instagram login/parol
INSTAGRAM_USERNAME = "Morf_x30"
INSTAGRAM_PASSWORD = "Shax3010"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()

# /start komandasi
@router.message(lambda msg: msg.text == "/start")
async def start(message: Message):
    await message.answer("Salom 👋 Menga Instagram link yuboring, men sizga yuklab beraman 📥")

# Instagram yuklab olish
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
            "username": INSTAGRAM_USERNAME,
            "password": INSTAGRAM_PASSWORD
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

        # FSInputFile orqali yuboramiz
        video = FSInputFile(file_path)
        await message.answer_video(video=video, caption="✅ Yuklab olindi!")

        os.remove(file_path)  # yuborilgandan keyin faylni o‘chiramiz

    except DownloadError as e:
        await message.answer(f"⚠️ Yuklab bo‘lmadi: {e}")
    except Exception as e:
        await message.answer(f"⚠️ Xatolik: {e}")

# Main
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
