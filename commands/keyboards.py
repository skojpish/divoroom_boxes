from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup
from .callback_factories import BoxesCF


def menu_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Купить", callback_data=BoxesCF(price=2500))
    kb.adjust(1)
    return kb.as_markup()
