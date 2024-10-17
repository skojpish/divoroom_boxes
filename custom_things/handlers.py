from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from custom_things.callback_factories import CustomMagnetsCF

from .messages import custom_magnets_text, custom_shoppers_text
from .keyboards import custom_magnets_kb, custom_shoppers_kb
from .images import magnets_photos, shoppers_photos
from paper.callback_factories import StickersColorCF

router = Router()


@router.callback_query(
    StickersColorCF.filter((F.box_price == 2990) | (F.box_price == 4990))
)
async def custom_magnets(
    callback: CallbackQuery, callback_data: StickersColorCF, state: FSMContext
):
    await callback.answer()
    await state.update_data(stickers_color=callback_data.color)

    text = custom_magnets_text()

    data = await state.get_data()

    await callback.message.answer_media_group(media=magnets_photos)
    await callback.message.answer(
        text=text,
        reply_markup=custom_magnets_kb(
            price=data.get("box_price"), hedgehog_card=data.get("hedgehog_card")
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
            price=data.get("box_price"), stickers_color=data.get("stickers_color")
        ),
    )
