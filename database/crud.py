from datetime import datetime, timedelta
from sqlalchemy import select, delete, and_
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Student, Lecture
from .config import async_session_factory


async def get_student(chat_id: int):
    async with async_session_factory() as session:
        result = await session.execute(select(Student).where(Student.chat_id == chat_id))
        return result.scalar_one_or_none()


async def get_active_students(session: AsyncSession) -> list[Student]:
    result = await session.execute(select(Student).where(Student.is_active == True))
    return list(result.scalars().all())


async def insert_student_and_schedule(chat_id: int, full_name: str, notification_time: int, classes: list):
    async with async_session_factory() as session:
        student = Student(chat_id=chat_id, full_name=full_name,
                          notification_time=notification_time, is_active=True)
        for cls in classes:
            student_class = Lecture(name=cls.name, type=cls.type, location=cls.location,
                                    teachers=cls.teachers, start_time=cls.start_time)
            student.lectures.append(student_class)
        session.add(student)
        await session.commit()


async def update_student_schedule(session, chat_id: int, classes: list) -> bool:
    result = await session.execute(
        select(Student)
        .options(selectinload(Student.lectures))
        .where(Student.chat_id == chat_id)
    )
    student = result.unique().scalar_one()

    old_lectures = sorted(
        [(l.name, l.type, l.location, l.teachers, l.start_time)
            for l in student.lectures],
        key=lambda x: x[4]
    )

    new_lectures = sorted(
        [(cls.name, cls.type, cls.location, cls.teachers, cls.start_time)
            for cls in classes],
        key=lambda x: x[4]
    )

    has_changes = old_lectures != new_lectures

    await session.execute(delete(Lecture).where(Lecture.student_id == student.id))

    for cls in classes:
        lecture = Lecture(
            name=cls.name,
            type=cls.type,
            location=cls.location,
            teachers=cls.teachers,
            start_time=cls.start_time
        )
        student.lectures.append(lecture)
    await session.commit()
    return has_changes


async def toggle_notification_status(chat_id: int) -> bool:
    async with async_session_factory() as session:
        result = await session.execute(select(Student).where(Student.chat_id == chat_id))
        student = result.scalar_one()
        new_status = not student.is_active
        student.is_active = new_status
        await session.commit()
        return new_status


async def update_notification_time(chat_id: int, new_time: int) -> None:
    async with async_session_factory() as session:
        result = await session.execute(select(Student).where(Student.chat_id == chat_id))
        student = result.scalar_one()
        student.notification_time = new_time
        await session.commit()


async def toggle_sending_photo_status(chat_id: int) -> bool:
    async with async_session_factory() as session:
        result = await session.execute(select(Student).where(Student.chat_id == chat_id))
        student = result.scalar_one()
        new_status = not student.is_sending_photo
        student.is_sending_photo = new_status
        await session.commit()
        return new_status


async def get_upcoming_lectures(session: AsyncSession, hours_ahead: int = 24) -> list[Lecture]:
    now = datetime.now()
    result = await session.execute(
        select(Lecture)
        .options(selectinload(Lecture.student))
        .where(
            and_(
                Lecture.is_sended == False,
                Lecture.start_time.between(now, now + timedelta(hours=hours_ahead))
            )
        )
        .execution_options(populate_existing=True)
    )
    return list(result.scalars().all())
