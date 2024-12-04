from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup

from .callback_factories import CustomMagnetsCF, CustomShoppersCF
from paper.callback_factories import PinCF, StickersColorCF


def custom_magnets_kb(price: int, stickers: str) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(
        text="1",
        callback_data=CustomMagnetsCF(name="«Снеговичок»", box_price=price),
    )
    kb.button(
        text="2",
        callback_data=CustomMagnetsCF(name="«Кошка у окошка»", box_price=price),
    )
    kb.button(text="Назад", callback_data=StickersColorCF(color=stickers))
    kb.adjust(2)
    return kb.as_markup()


def custom_shoppers_kb(price: int, pin: str) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(
        text="1",
        callback_data=CustomShoppersCF(name="«Теплые коты»", box_price=price),
    )
    kb.button(
        text="2",
        callback_data=CustomShoppersCF(name="«Трудные времена»", box_price=price),
    )
    kb.button(
        text="3",
        callback_data=CustomShoppersCF(name="«Все переживем!»", box_price=price),
    )
    kb.button(text="4", callback_data=CustomShoppersCF(name="«Чаю?»", box_price=price))
    kb.button(
        text="5", callback_data=CustomShoppersCF(name="«Несу добро»", box_price=price)
    )
    kb.button(
        text="Назад",
        callback_data=PinCF(name=pin, box_price=price),
    )
    kb.adjust(3, 2, 1)
    return kb.as_markup()
