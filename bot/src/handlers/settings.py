from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from bot.src.states import Form
from bot.src.markup import (
    get_notification_settings_keyboard,
    get_schedule_keyboard
)
from database.crud import get_student

router = Router()


@router.message(lambda message: message.text == "⚙️Настройки")
async def settings_button_handler(message: types.Message, state: FSMContext):
    student = await get_student(message.chat.id)
    if student:
        status_text = "включены🔔" if student.is_active else "выключены🔕"
        hour_word = (
            "час" if student.notification_time == 1
            else "часа" if 1 < student.notification_time < 5
            else "часов"
        )
        await message.answer(f"Текущие настройки:\nУведомления {status_text}\n"
                             f"Время оповещений: за {student.notification_time} {hour_word} до начала занятия\n"
                             f"Отправление фото: {"Да" if student.is_sending_photo else "Нет"}\n\n"
                             "Что ты хочешь изменить?",
                             reply_markup=get_notification_settings_keyboard())

        await state.set_state(Form.setting_notifications)
    else:
        await message.answer(
            "Привет! Нажми кнопку ниже, чтобы загрузить расписание:",
            reply_markup=get_schedule_keyboard()
        )
