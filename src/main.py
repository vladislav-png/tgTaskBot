# Copyright (c) 2026 Vlad
# Данный исходный код распространяется под лицензией MIT.
# Полный текст лицензии находится в файле LICENSE в корне проекта.

import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))


async def main() -> None:
    """Starts the bot in long polling mode"""
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


try:
    asyncio.run(main())

except KeyboardInterrupt:
    print("Bot stopped by user")
