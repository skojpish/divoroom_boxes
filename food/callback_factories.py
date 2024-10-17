from aiogram.filters.callback_data import CallbackData


class TeaCF(CallbackData, prefix="t"):
    name: str


class ChocolateCF(CallbackData, prefix="ch"):
    name: str


class CandleCF(CallbackData, prefix="c"):
    name: str
