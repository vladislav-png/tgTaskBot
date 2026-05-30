import random

from aiogram import F, Router, filters, types

from keyboards.InlineKeyboard import geo_inline_button, start_inline_button

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
        "нам нужно завершить один <u>критически важный</u> шаг — регистрацию. 📝\n"
        "==============================",
        parse_mode="html",
        reply_markup=start_inline_button,
    )


@router.callback_query(F.data == "start_register")
async def register_button_callback(callback: types.CallbackQuery):
    """Prompts the user to select a location type"""
    await callback.message.edit_text(
        "<b>Выберите один из вариантов определения местоположения:</b>\n"
        "-Точное: доступны все ф-ии сразу\n"
        "-Приблизительное: нужно будет указывать все вручную",
        parse_mode="html",
        reply_markup=geo_inline_button,
    )
