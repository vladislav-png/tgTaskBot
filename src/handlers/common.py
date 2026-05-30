import random

from aiogram import F, Router, filters, types

import keyboards

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
        reply_markup=keyboards.InlineKeyboard.start_inline_button,
    )


@router.callback_query(F.data == "start_register")
async def register_button_callback(callback: types.CallbackQuery) -> None:
    """Prompts the user to select a location type"""
    await callback.message.edit_text(
        "<b>Выберите один из вариантов определения местоположения:</b>\n"
        "-Точное: доступны все ф-ии сразу\n"
        "-Приблизительное: нужно будет указывать все вручную",
        parse_mode="html",
        reply_markup=keyboards.InlineKeyboard.geo_inline_button,
    )
    await callback.answer()


@router.callback_query(F.data == "exact_geo")
async def exact_geo_callback(callback: types.CallbackQuery) -> None:
    """Shows instructions on how to share location via attachments"""
    await callback.message.edit_text(
        "<b>Чтобы отправить точное местоположение:</b>\n\n"
        "1. Нажмите на иконку 📎 (скрепка) или ➕ рядом с полем ввода.\n"
        "2. Выберите пункт <b>«Геопозиция»</b> (Location).\n"
        "3. Нажмите <b>«Отправить мою геопозицию»</b>.",
        parse_mode="html",
    )
    await callback.answer()
