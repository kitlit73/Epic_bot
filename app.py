import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

# Загружаем токен из .env
load_dotenv()

# Включаем логи, чтобы видеть ошибки в консоли
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(
        f"Привет, {message.from_user.first_name}!\n"
        "Я тестовый бот. Напиши что-нибудь, и я повторю это сообщение."
    )


@dp.message(F.text)
async def echo(message: Message) -> None:
    await message.answer(f"Ты написал: {message.text}")


async def main() -> None:
    print("Бот запущен. Остановить — Ctrl+C")
    # start_polling запускает бесконечный цикл получения обновлений
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Бот остановлен")
