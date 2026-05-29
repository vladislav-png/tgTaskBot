import random

from aiogram import Router, filters, types

router = Router()


@router.message(filters.CommandStart())
async def start_bot(message: types.Message) -> None:
    """Handles the start command"""
    greetings = ["Рад тебя видеть", "Приветствую", "Салют", "Здравствуйте"]
    welcome = random.choice(greetings)

    await message.answer(
        f"{welcome}, <b>{message.from_user.full_name}!</b>\n"
        "Добро пожаловать в <b>TaskBot</b>.\n"
        "==============================\n"
        "Перед тем как мы начнем,\n"
        "нам нужно завершить один <u>критически важный</u> шаг — регистрацию. 📝"
        "==============================",
        parse_mode="html",
    )
