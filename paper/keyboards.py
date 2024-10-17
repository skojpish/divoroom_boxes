from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup
from .callback_factories import CardsInStockCF, HedgehogCF, StickersColorCF


def cards_in_stock_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="1", callback_data=CardsInStockCF(name="«Кот на розовом»"))
    kb.button(text="2", callback_data=CardsInStockCF(name="«Кот в поезде»"))
    kb.button(text="3", callback_data=CardsInStockCF(name="«PIZDEC»"))
    kb.button(text="4", callback_data=CardsInStockCF(name="«Трудные времена»"))
    kb.button(text="Назад", callback_data="back_to_menu")
    kb.adjust(4)
    return kb.as_markup()


def hedgehog_card_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="1", callback_data=HedgehogCF(name="«Два ежа ...»"))
    kb.button(text="2", callback_data=HedgehogCF(name="«Ты пушистей»"))
    kb.button(text="Назад", callback_data="let's go")
    kb.adjust(2)
    return kb.as_markup()


def stickers_color_kb(price: int, card_in_stock_name: str) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(
        text="1",
        callback_data=StickersColorCF(color="Черно-белый котики", box_price=price),
    )
    kb.button(
        text="2",
        callback_data=StickersColorCF(color="Черно-рыжий котики", box_price=price),
    )
    kb.button(
        text="3", callback_data=StickersColorCF(color="Серые котики", box_price=price)
    )
    kb.button(text="Назад", callback_data=CardsInStockCF(name=card_in_stock_name))
    kb.adjust(3)
    return kb.as_markup()
