from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup


def boxes_info_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Поехали!", callback_data="let's go")
    kb.button(text="Назад", callback_data="back_to_menu")
    kb.adjust(1)
    return kb.as_markup()

def choice_delivery_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Доставка по России", callback_data="sdek_delivery")
    kb.button(text="Самовывоз из Санкт-Петербурга", callback_data="self_delivery")
    kb.adjust(1)
    return kb.as_markup()