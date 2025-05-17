from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from bot.src.states import Form
from bot.src.markup import get_settings_keyboard
from database.crud import insert_student_and_schedule
from parserCode.parseSchedule import get_schedule

router = Router()


@router.callback_query(lambda c: c.data == "load_schedule")
async def ask_for_name(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()  # reset кнопки
    await callback.message.delete()  # type: ignore
    await callback.message.answer(  # type: ignore
        "Введите ваше ФИО через пробел:"
    )
    await state.set_state(Form.waiting_for_name)


@router.message(Form.waiting_for_name)
async def process_name(message: types.Message, state: FSMContext):
    try:
        await message.answer(f"В поисках вашего расписания!")
        schedule = await get_schedule(message.text)  # type: ignore
        await state.update_data(
            schedule=schedule,
            full_name=message.text,
            chat_id=message.chat.id
        )
        await message.answer(
            "За сколько часов (От 1 до 24) до начала занятия тебе присылать уведомление?"
        )
        await state.set_state(Form.waiting_for_notification_time)
    except RuntimeError as re:
        await message.answer("Ведутся технические работы. Воспользуйтесь ботом позже")
    except ValueError as ve:
        await message.answer(
            "Неверное ФИО! Попробуйте еще раз:"
        )


@router.message(Form.waiting_for_notification_time)
async def process_notification_time(message: types.Message, state: FSMContext):
    try:
        hours = int(message.text)  # type: ignore
        if 1 <= hours <= 24:
            data = await state.get_data()
            await insert_student_and_schedule(
                data["chat_id"],
                data["full_name"],
                hours,
                data["schedule"]
            )
            hour_word = "час" if hours == 1 else "часа" if 1 < hours < 5 else "часов"
            await message.answer(
                f"Отлично! Уведомления будут приходить за {hours} {hour_word} до начала занятия.",
                reply_markup=get_settings_keyboard()
            )
            await state.clear()
        else:
            await message.answer("Пожалуйста, введите число от 1 до 24.")
    except ValueError:
        await message.answer("Это не похоже на целое число. Пожалуйста, введите число от 1 до 24.")
