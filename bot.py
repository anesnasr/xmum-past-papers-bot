from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio
from aiogram import Bot, Dispatcher, types
from config import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher()
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Hello, I am your bot!")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())