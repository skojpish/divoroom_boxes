from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from boxes.fsm import UserInfoState
from boxes.keyboards import boxes_info_kb, choice_delivery_kb
from boxes.messages import box_info_text, final_text, order_text, user_info_text, choice_delivery_text
from boxes.images import (
    final_photo,
    box_info_photo_1,
    box_info_photo_2,
    box_info_photo_3,
)
from commands.callback_factories import BoxesCF
from custom_things.callback_factories import CustomMagnetsCF, CustomShoppersCF
from paper.callback_factories import PinCF
from settings import MASTER_ID, bot


router = Router()


@router.callback_query(BoxesCF.filter())
async def choice_of_delivery(callback: CallbackQuery, callback_data: BoxesCF, state: FSMContext):
    await callback.answer()
    text = choice_delivery_text()
    await callback.message.answer(text, reply_markup=choice_delivery_kb())

@router.callback_query(F.data == "sdek_delivery")
async def sdek_delivery_handler(callback: CallbackQuery, state: FSMContext):
    await callback.answer()

    text = user_info_text()

    await state.set_state(UserInfoState.text)

    await callback.message.answer(text=text)


async def all_boxes_info(
    callback: CallbackQuery, callback_data: BoxesCF, state: FSMContext
):
    await callback.answer()
    await state.update_data(box_price=callback_data.price)

    if callback_data.price == 1990:
        box_photo = box_info_photo_1
    elif callback_data.price == 2990:
        box_photo = box_info_photo_2
    elif callback_data.price == 4990:
        box_photo = box_info_photo_3

    text = box_info_text(price=callback_data.price)

    await callback.message.answer_photo(
        photo=box_photo, caption=text, reply_markup=boxes_info_kb()
    )


@router.callback_query(PinCF.filter(F.box_price == 1990))
@router.callback_query(CustomMagnetsCF.filter(F.box_price == 2990))
@router.callback_query(CustomShoppersCF.filter())
async def user_info_handler(
    callback: CallbackQuery,
    callback_data: PinCF | CustomMagnetsCF | CustomShoppersCF,
    state: FSMContext,
):
    await callback.answer()

    text = user_info_text()

    await state.set_state(UserInfoState.text)

    price = callback_data.box_price

    if price == 1990:
        await state.update_data(pin=callback_data.name)
    elif price == 2990:
        await state.update_data(magnet=callback_data.name)
    else:
        await state.update_data(shopper=callback_data.name)

    await callback.message.answer(text=text)


@router.message(UserInfoState.text)
async def final_msg_handler(message: Message, state: FSMContext) -> None:
    await state.update_data(user_info=message.text)

    data = await state.get_data()
    text = final_text(data.get("username"))
    await message.answer_photo(photo=final_photo, caption=text)

    text = order_text(**data)
    await bot.send_message(chat_id=MASTER_ID, text=text)

    await state.clear()


@router.callback_query(F.data == "self_delivery")
async def self_delivery_handler(
    callback: CallbackQuery
):
    await callback.answer()

    text = final_text(callback.from_user.username)
    await callback.message.answer_photo(photo=final_photo, caption=text)

    text = order_text(callback.from_user.username)
    await bot.send_message(chat_id=MASTER_ID, text=text)