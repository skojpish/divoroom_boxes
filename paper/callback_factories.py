from aiogram.filters.callback_data import CallbackData


class CardsInStockCF(CallbackData, prefix="card"):
    name: str


class StickersColorCF(CallbackData, prefix="sc"):
    color: str


class PinCF(CallbackData, prefix="p"):
    name: str
    box_price: int
