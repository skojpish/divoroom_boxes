from aiogram.fsm.state import StatesGroup, State


class UserInfoState(StatesGroup):
    text = State()
