from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from .callback_factories import CardsInStockCF, HedgehogCF
from .keyboards import cards_in_stock_kb, hedgehog_card_kb, stickers_color_kb
from .messages import cards_in_stock_text, hedgehog_card_text, stickers_color_text
from .images import cards_photo, hedgehog_photos, stickers_color_photo


router = Router()


@router.callback_query(F.data == "let's go")
async def cards_in_stock(callback: CallbackQuery):
    await callback.answer()

    text = cards_in_stock_text()

    await callback.message.answer_photo(
        photo=cards_photo, caption=text, reply_markup=cards_in_stock_kb()
    )


@router.callback_query(CardsInStockCF.filter())
async def hedgehog_card(
    callback: CallbackQuery, callback_data: CardsInStockCF, state: FSMContext
):
    await callback.answer()
    await state.update_data(card=callback_data.name)

    text = hedgehog_card_text()

    await callback.message.answer_media_group(media=hedgehog_photos)
    await callback.message.answer(text=text, reply_markup=hedgehog_card_kb())


@router.callback_query(HedgehogCF.filter())
async def stickers_color(
    callback: CallbackQuery, callback_data: HedgehogCF, state: FSMContext
):
    await callback.answer()
    await state.update_data(hedgehog_card=callback_data.name)

    text = stickers_color_text()

    data = await state.get_data()

    await callback.message.answer_photo(
        photo=stickers_color_photo,
        caption=text,
        reply_markup=stickers_color_kb(
            price=data.get("box_price"), card_in_stock_name=data.get("card")
        ),
    )
