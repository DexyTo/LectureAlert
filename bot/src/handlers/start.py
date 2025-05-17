from aiogram import Router, types
from aiogram.filters import CommandStart
from markup import get_schedule_keyboard, get_settings_keyboard
from database.crud import get_student


router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    user_exist = await get_student(message.chat.id)
    if user_exist:
        await message.answer("Ты уже зарегистрирован! Может хочешь настроить уведомления?",
                             reply_markup=get_settings_keyboard())
    else:
        await message.answer(
            "Привет! Нажми кнопку ниже, чтобы загрузить расписание:",
            reply_markup=get_schedule_keyboard()
        )