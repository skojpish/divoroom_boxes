from aiogram.filters.callback_data import CallbackData


class BoxesCF(CallbackData, prefix="box"):
    price: int
