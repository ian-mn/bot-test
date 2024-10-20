import asyncio
import logging

from aiogram import Bot, Dispatcher, F, types

from settings import settings


logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.token.get_secret_value())
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
