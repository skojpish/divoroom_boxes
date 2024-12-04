from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from .callback_factories import CardsInStockCF, StickersColorCF
from .keyboards import cards_in_stock_kb, pin_kb, stickers_color_kb
from .messages import cards_in_stock_text, pin_text, stickers_color_text
from .images import cards_photo, stickers_color_photos, pin_photo


router = Router()


@router.callback_query(F.data == "let's go")
async def cards_in_stock(callback: CallbackQuery):
    await callback.answer()

    text = cards_in_stock_text()

    await callback.message.answer_photo(
        photo=cards_photo, caption=text, reply_markup=cards_in_stock_kb()
    )


@router.callback_query(CardsInStockCF.filter())
async def stickers_color(
    callback: CallbackQuery, callback_data: CardsInStockCF, state: FSMContext
):
    await callback.answer()
    await state.update_data(card=callback_data.name)

    text = stickers_color_text()

    await callback.message.answer_media_group(media=stickers_color_photos)
    await callback.message.answer(
        text=text,
        reply_markup=stickers_color_kb(),
    )


@router.callback_query(StickersColorCF.filter())
async def pin_handler(
    callback: CallbackQuery, callback_data: StickersColorCF, state: FSMContext
):
    await callback.answer()
    await state.update_data(stickers_color=callback_data.color)

    text = pin_text()

    data = await state.get_data()

    await callback.message.answer_photo(
        photo=pin_photo,
        caption=text,
        reply_markup=pin_kb(price=data.get("box_price"), card=data.get("card")),
    )
