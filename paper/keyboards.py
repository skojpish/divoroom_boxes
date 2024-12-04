from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup

from .callback_factories import CardsInStockCF, PinCF, StickersColorCF


def cards_in_stock_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="1", callback_data=CardsInStockCF(name="«Трудные времена»"))
    kb.button(text="2", callback_data=CardsInStockCF(name="«Кот под снегом»"))
    kb.button(text="3", callback_data=CardsInStockCF(name="«Кот на розовом»"))
    kb.button(text="4", callback_data=CardsInStockCF(name="«Кот на фиолетовом»"))
    kb.button(text="Назад", callback_data="back_to_menu")
    kb.adjust(4)
    return kb.as_markup()


def stickers_color_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(
        text="1",
        callback_data=StickersColorCF(color="Зеленые"),
    )
    kb.button(
        text="2",
        callback_data=StickersColorCF(color="Красные"),
    )
    kb.button(text="Назад", callback_data="let's go")
    kb.adjust(2)
    return kb.as_markup()


def pin_kb(price: int, card: str) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(
        text="1",
        callback_data=PinCF(name="Зеленая шапочка", box_price=price),
    )
    kb.button(
        text="2",
        callback_data=PinCF(name="Красная шапочка", box_price=price),
    )
    kb.button(text="3", callback_data=PinCF(name="Желтая шапочка", box_price=price))
    kb.button(text="Назад", callback_data=CardsInStockCF(name=card))
    kb.adjust(3)
    return kb.as_markup()
