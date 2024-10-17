from aiogram.filters.callback_data import CallbackData


class CardsInStockCF(CallbackData, prefix="card"):
    name: str


class HedgehogCF(CallbackData, prefix="hc"):
    name: str


class StickersColorCF(CallbackData, prefix="sc"):
    color: str
    box_price: int
