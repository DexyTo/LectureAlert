from datetime import datetime, timedelta
import logging
import aiofiles.os
from aiogram import Bot
from aiogram.types import FSInputFile
from database.crud import get_upcoming_lectures
from bot.src.utils import get_photo_path, format_notification_text
from database.config import async_session_factory  

async def check_upcoming_lectures(bot: Bot):
    async with async_session_factory() as session:  
        try:
            lectures = await get_upcoming_lectures(session)
            sent_lectures = []
        
            for lecture in lectures:
                try:
                    student = lecture.student
                    if not student.is_active:
                        continue
                        
                    notification_time = lecture.start_time - timedelta(hours=student.notification_time)
                    if datetime.now() >= notification_time:
                        message_text = format_notification_text(lecture)
                        photo_path = get_photo_path(lecture.location)
                        print(photo_path)
                        photo_exists = await aiofiles.os.path.exists(photo_path) if photo_path else False

                        if photo_path and photo_exists and student.is_sending_photo:
                            await bot.send_photo(
                                chat_id=student.chat_id,
                                photo=FSInputFile(photo_path),
                                caption=message_text
                            )
                        else:
                            await bot.send_message(
                                chat_id=student.chat_id,
                                text=message_text
                            )
                        lecture.is_sended = True
                        sent_lectures.append(lecture)
                except Exception as e:
                    logging.error(f"Ошибка в лекции {lecture.id}: {str(e)}")
                    await session.rollback()
            
            if sent_lectures:
                await session.commit()
                logging.info(f"Успешно обработано {len(sent_lectures)} уведомлений")
        
        except Exception as e:
            logging.error(f"Критическая ошибка: {str(e)}")
            await session.rollback()

            