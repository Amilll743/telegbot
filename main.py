import asyncio
import logging
from time import localtime
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
bot = Bot(token="6914454423:AAFCF4oO3Zyznuj1Fh5ZQZte-HD0srqODU8")
dp = Dispatcher()

@dp.message(Command("creator"))
async def cmd_start(message: types.Message):
    await message.answer("Привет тут я расскажу тебе информацию о себе я Амиль молодой программист учусь в онлайн школе кодланд люблю играть в игры бравл старс и майнкрафт")

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет у меня есть команды kodland,creator")

@dp.message(Command("kodland"))
async def cmd_kodland(message: types.Message):
    await message.answer("онлайн школа обучающая программированию!")

@dp.message(Command("secret"))
async def cmd_kodland(message: types.Message):
    await message.answer("р-роб-боты з-зах-хват-тя-я-я-ят ми-и-и-и-и-и-и-и-и-и-ир!")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())