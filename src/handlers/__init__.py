from aiogram import Dispatcher

from handlers.common import router as start_router


def register_router(dp: Dispatcher) -> None:
    """Registers all application routers in the main dispatcher"""
    dp.include_routers(
        start_router,
    )
