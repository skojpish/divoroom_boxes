from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup

from .callback_factories import CustomMagnetsCF, CustomShoppersCF
from paper.callback_factories import HedgehogCF, StickersColorCF


def custom_magnets_kb(price: int, hedgehog_card: str) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(
        text="1",
        callback_data=CustomMagnetsCF(name="«Под ушки - подушки»", box_price=price),
    )
    kb.button(
        text="2",
        callback_data=CustomMagnetsCF(name="«Никуда не идем и спим»", box_price=price),
    )
    kb.button(text="Назад", callback_data=HedgehogCF(name=hedgehog_card))
    kb.adjust(2)
    return kb.as_markup()


def custom_shoppers_kb(price: int, stickers_color: str) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(
        text="1",
        callback_data=CustomShoppersCF(name="«Все переживем»", box_price=price),
    )
    kb.button(text="2", callback_data=CustomShoppersCF(name="«Чаю?»", box_price=price))
    kb.button(
        text="3", callback_data=CustomShoppersCF(name="«Несу добро»", box_price=price)
    )
    kb.button(
        text="Назад",
        callback_data=StickersColorCF(color=stickers_color, box_price=price),
    )
    kb.adjust(3)
    return kb.as_markup()
