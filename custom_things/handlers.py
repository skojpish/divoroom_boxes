from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from custom_things.callback_factories import CustomMagnetsCF

from .messages import custom_magnets_text, custom_shoppers_text
from .keyboards import custom_magnets_kb, custom_shoppers_kb
from .images import magnets_photo, shoppers_photos
from paper.callback_factories import PinCF

router = Router()


@router.callback_query(PinCF.filter((F.box_price == 2990) | (F.box_price == 4990)))
async def custom_magnets(
    callback: CallbackQuery, callback_data: PinCF, state: FSMContext
):
    await callback.answer()
    await state.update_data(pin=callback_data.name)

    text = custom_magnets_text()

    data = await state.get_data()

    await callback.message.answer_photo(
        photo=magnets_photo,
        caption=text,
        reply_markup=custom_magnets_kb(
            price=data.get("box_price"), stickers=data.get("stickers_color")
        ),
    )


@router.callback_query(CustomMagnetsCF.filter(F.box_price == 4990))
async def custom_shoppers(
    callback: CallbackQuery, callback_data: CustomMagnetsCF, state: FSMContext
):
    await callback.answer()
    await state.update_data(magnet=callback_data.name)

    text = custom_shoppers_text()

    data = await state.get_data()

    await callback.message.answer_media_group(media=shoppers_photos)
    await callback.message.answer(
        text=text,
        reply_markup=custom_shoppers_kb(
            price=data.get("box_price"), pin=data.get("pin")
        ),
    )
