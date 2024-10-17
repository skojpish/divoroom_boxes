from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup
from .callback_factories import BoxesCF


def menu_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Бокс за 1990", callback_data=BoxesCF(price=1990))
    kb.button(text="Бокс за 2990", callback_data=BoxesCF(price=2990))
    kb.button(text="Бокс за 4990", callback_data=BoxesCF(price=4990))
    kb.adjust(1)
    return kb.as_markup()
