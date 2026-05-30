from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_inline_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Регистрация", callback_data="start_register")]
    ]
)
geo_inline_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Точное", callback_data="exact_geo"),
            InlineKeyboardButton(text="Приблизительное", callback_data="geo"),
        ]
    ]
)
