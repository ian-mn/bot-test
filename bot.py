import asyncio
import logging
from tempfile import TemporaryDirectory

from aiogram import Bot, Dispatcher, F, types
from PIL import Image, ImageEnhance
from pyzbar.pyzbar import decode

from settings import settings

logging.basicConfig(level=logging.INFO)
bot = Bot(token=settings.token.get_secret_value())
dp = Dispatcher()


@dp.message(F.photo)
async def photo_handler(message: types.Message):
    with TemporaryDirectory() as dir:
        temp_fname = f"{dir}/temp.jpg"
        await message.bot.download(
            file=message.photo[-1].file_id,
            destination=temp_fname,
        )
        image = Image.open(temp_fname)

        enhancer = ImageEnhance.Sharpness(image)
        image = enhancer.enhance(2)
        image = image.convert("1")

        decoded = decode(image)
        if decoded:
            first_decoded = decoded[0]
            await message.answer(text=first_decoded.data)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
