from aiogram.filters.callback_data import CallbackData


class CustomMagnetsCF(CallbackData, prefix="cm"):
    name: str
    box_price: int


class CustomShoppersCF(CallbackData, prefix="csh"):
    name: str
    box_price: int
