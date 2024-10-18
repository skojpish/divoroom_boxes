from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from boxes.fsm import UserInfoState
from boxes.keyboards import boxes_info_kb
from boxes.messages import box_info_text, final_text, order_text, user_info_text
from boxes.images import final_photo, box_info_photo
from commands.callback_factories import BoxesCF
from food.callback_factories import CandleCF
from settings import MASTER_ID, bot


router = Router()


@router.callback_query(BoxesCF.filter())
async def all_boxes_info(
    callback: CallbackQuery, callback_data: BoxesCF, state: FSMContext
):
    await callback.answer()
    await state.update_data(box_price=callback_data.price)

    text = box_info_text()

    await callback.message.answer_photo(photo=box_info_photo, caption=text, reply_markup=boxes_info_kb())


@router.callback_query(CandleCF.filter())
async def user_info_handler(
    callback: CallbackQuery, callback_data: CandleCF, state: FSMContext
):
    await callback.answer()
    await state.update_data(candle=callback_data.name)

    text = user_info_text()

    await state.set_state(UserInfoState.text)

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
