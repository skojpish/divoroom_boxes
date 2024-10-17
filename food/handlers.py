from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from custom_things.callback_factories import CustomMagnetsCF, CustomShoppersCF
from food.callback_factories import ChocolateCF, TeaCF
from food.keyboards import chocolate_kb, candle_kb, tea_kb
from food.messages import candle_text, chocolate_text, tea_text
from food.images import tea_photo, chocolate_photo, candle_photos
from paper.callback_factories import StickersColorCF


router = Router()


@router.callback_query(StickersColorCF.filter(F.box_price == 1990))
@router.callback_query(CustomMagnetsCF.filter(F.box_price == 2990))
@router.callback_query(CustomShoppersCF.filter())
async def tea_handler(
    callback: CallbackQuery,
    callback_data: StickersColorCF | CustomMagnetsCF | CustomShoppersCF,
    state: FSMContext,
):
    await callback.answer()

    text = tea_text()

    price = callback_data.box_price

    data = await state.get_data()

    if price == 1990:
        await state.update_data(stickers_color=callback_data.color)
        name = data.get("hedgehog_card")
    elif price == 2990:
        await state.update_data(magnet=callback_data.name)
        name = data.get("stickers_color")
    else:
        await state.update_data(shopper=callback_data.name)
        name = data.get("magnet")

    await callback.message.answer_photo(
        photo=tea_photo, caption=text, reply_markup=tea_kb(price=price, name=name)
    )


@router.callback_query(TeaCF.filter())
async def chocolate_handler(
    callback: CallbackQuery, callback_data: TeaCF, state: FSMContext
):
    await callback.answer()
    await state.update_data(tea=callback_data.name)

    text = chocolate_text()

    data = await state.get_data()

    await callback.message.answer_photo(
        photo=chocolate_photo,
        caption=text,
        reply_markup=chocolate_kb(price=data.get("box_price"), name=data.get("tea")),
    )


@router.callback_query(ChocolateCF.filter())
async def candle_handler(
    callback: CallbackQuery, callback_data: ChocolateCF, state: FSMContext
):
    await callback.answer()
    await state.update_data(chocolate=callback_data.name)

    text = candle_text()

    data = await state.get_data()

    await callback.message.answer_media_group(media=candle_photos)
    await callback.message.answer(
        text=text, reply_markup=candle_kb(name=data.get("tea"))
    )
