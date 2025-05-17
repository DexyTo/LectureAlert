import asyncio
from aiogram import Bot
from sqlalchemy.ext.asyncio import AsyncSession
from database.crud import get_active_students, update_student_schedule
from parserCode.parseSchedule import get_schedule
from database.config import async_session_factory  


async def send_schedule_change_notification(bot: Bot, chat_id: int):
    message = "📢 Ваше расписание на следующую неделю изменилось! Проверьте обновления."
    await bot.send_message(chat_id=chat_id, text=message)


async def retry_with_backoff(func, max_retries=3, initial_delay=5, *args, **kwargs):
    for attempt in range(max_retries):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
            delay = initial_delay * (2 ** attempt)
            print(f"Ошибка: {e}. Повторная попытка через {delay} сек...")
            await asyncio.sleep(delay)


async def update_student_schedule_with_retry(session: AsyncSession, chat_id: int, full_name: str, bot: Bot):
    new_schedule = await retry_with_backoff(
        get_schedule,
        full_name=full_name
    )

    has_changes = await retry_with_backoff(
        update_student_schedule,
        session=session,
        chat_id=chat_id,
        full_name=full_name,
        classes=new_schedule
    )

    if has_changes:
        await send_schedule_change_notification(bot, chat_id)


async def update_all_schedules(bot: Bot):
    async with async_session_factory() as session:
        students = await get_active_students(session)
        for student in students:
            try:
                await update_student_schedule_with_retry(
                    session,
                    student.chat_id,
                    student.full_name,
                    bot
                )
                print(f"Расписание студента {student.full_name} обновлено")
            except Exception as e:
                print(
                    f"Не удалось обновить расписание студента {student.full_name}")
                continue
