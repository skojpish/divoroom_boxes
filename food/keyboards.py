# from aiogram.utils.keyboard import InlineKeyboardBuilder
# from aiogram.types import InlineKeyboardMarkup

# from custom_things.callback_factories import CustomMagnetsCF, CustomShoppersCF
# from food.callback_factories import ChocolateCF, CandleCF, TeaCF
# from paper.callback_factories import HedgehogCF, StickersColorCF


# def tea_kb(price: int, name: str) -> InlineKeyboardMarkup:
#     kb = InlineKeyboardBuilder()

#     if price == 1990:
#         callback_data = HedgehogCF(name=name, box_price=price)
#     elif price == 2990:
#         callback_data = StickersColorCF(color=name, box_price=price)
#     else:
#         callback_data = CustomMagnetsCF(name=name, box_price=price)

#     kb.button(text="1", callback_data=TeaCF(name="«Гранатовый пунш»"))
#     kb.button(text="2", callback_data=TeaCF(name="«Облепиховый пунш»"))
#     kb.button(text="Назад", callback_data=callback_data)
#     kb.adjust(2)
#     return kb.as_markup()


# def chocolate_kb(price: int, name: str) -> InlineKeyboardMarkup:
#     kb = InlineKeyboardBuilder()

#     if price == 1990:
#         callback_data = StickersColorCF(color=name, box_price=price)
#     elif price == 2990:
#         callback_data = CustomMagnetsCF(name=name, box_price=price)
#     else:
#         callback_data = CustomShoppersCF(name=name, box_price=price)

#     kb.button(text="1", callback_data=ChocolateCF(name="Молочный с кофе"))
#     kb.button(text="2", callback_data=ChocolateCF(name="Молочный с клубникой"))
#     kb.button(text="3", callback_data=ChocolateCF(name="Белый с фисташкой и клубникой"))
#     kb.button(text="Назад", callback_data=callback_data)
#     kb.adjust(3)
#     return kb.as_markup()


# def candle_kb(name: str) -> InlineKeyboardMarkup:
#     kb = InlineKeyboardBuilder()
#     kb.button(text="1", callback_data=CandleCF(name="«Тыквенный пирог»"))
#     kb.button(text="2", callback_data=CandleCF(name="«Пряная груша»"))
#     kb.button(text="3", callback_data=CandleCF(name="«Черничный маффин»"))
#     kb.button(text="Назад", callback_data=TeaCF(name=name))
#     kb.adjust(3)
#     return kb.as_markup()
