from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from bot.src.states import Form
from bot.src.markup import get_settings_keyboard
from database.crud import (
    toggle_notification_status,
    toggle_sending_photo_status,
    update_notification_time
)

router = Router()


@router.callback_query(Form.setting_notifications)
async def manage_notification(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.delete()  # type: ignore

    if callback.message:
        if callback.data == "change_notification_status":
            new_status = await toggle_notification_status(callback.message.chat.id)
            await callback.message.answer(
                "Уведомления включены!" if new_status
                else "Уведомления выключены!"
            )
            await state.clear()
        elif callback.data == "change_sending_photo_status":
            new_status = await toggle_sending_photo_status(callback.message.chat.id)
            await callback.message.answer(
                "К сообщению будет прикрепляться фото!" if new_status
                else "К сообщению не будет прикрепляться фото!"
            )
            await state.clear()
        elif callback.data == "change_notification_time":
            await callback.message.answer("За сколько часов (От 1 до 24) до начала занятия тебе присылать уведомление?")
            await state.set_state(Form.waiting_for_new_notification_time)


@router.message(Form.waiting_for_new_notification_time)
async def process_new_notification_time(message: types.Message, state: FSMContext):
    try:
        hours = int(message.text)  # type: ignore
        if 1 <= hours <= 24:
            hour_word = "час" if hours == 1 else "часа" if 1 < hours < 5 else "часов"
            await update_notification_time(message.chat.id, hours)
            await message.answer(
                f"Отлично! Уведомления будут приходить за {hours} {hour_word} до начала занятия.",
                reply_markup=get_settings_keyboard()
            )
            await state.clear()
        else:
            await message.answer("Пожалуйста, введите число от 1 до 24.")
    except ValueError:
        await message.answer("Это не похоже на целое число. Пожалуйста, введите число от 1 до 24.")
