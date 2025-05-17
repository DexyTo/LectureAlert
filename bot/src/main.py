import asyncio
import logging
from pathlib import Path
import sys
from os import getenv
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Путь до LectureAlert/
sys.path.append(str(BASE_DIR))

from handlers import routers
from services import update_all_schedules
from services import check_upcoming_lectures

from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from database.config import create_tables


async def on_startup(bot: Bot):
    await create_tables()  # type: ignore

    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        update_all_schedules,
        trigger="cron",
        day_of_week="sun",
        hour=0,
        args=[bot],
        timezone="Asia/Yekaterinburg"
    )

    scheduler.add_job(
        check_upcoming_lectures,
        'interval',
        minutes=5,
        args=[bot],
        timezone='Asia/Yekaterinburg'
    )
    scheduler.start()


async def main():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    load_dotenv()

    bot_token: str | None = getenv("BOT_TOKEN")
    if bot_token is None:
        raise KeyError("В файле .env не найден BOT_TOKEN")

    bot = Bot(token=bot_token)
    dp = Dispatcher()

    for router in routers:
        dp.include_router(router)

    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Путь до LectureAlert/
    sys.path.append(str(BASE_DIR))

    asyncio.run(main())
