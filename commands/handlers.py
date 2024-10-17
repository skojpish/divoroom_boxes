from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from commands.keyboards import menu_kb
from commands.messages import start_message


router = Router()


@router.message((F.text == "/start") | (F.text == "/menu"))
async def cmd_start(message: Message, state: FSMContext) -> None:
    await state.clear()
    await state.update_data(username=message.from_user.username)
    text = start_message()
    await message.answer(text=text, reply_markup=menu_kb())


@router.callback_query(F.data == "back_to_menu")
async def back_to_menu(callback: CallbackQuery) -> None:
    await callback.answer()
    text = start_message()
    await callback.message.answer(text=text, reply_markup=menu_kb())


@router.message(F.photo)
async def admin_photo(msg: Message) -> None:
    if msg.from_user.id == 317325310:
        await msg.answer(msg.photo[-1].file_id)
    else:
        pass
