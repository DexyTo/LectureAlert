from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int]
    full_name: Mapped[str]
    notification_time: Mapped[int] = mapped_column(default=24)
    is_active: Mapped[bool] = mapped_column(default=True)
    is_sending_photo: Mapped[bool] = mapped_column(default=True)

    lectures: Mapped[list["Lecture"]] = relationship(
        back_populates="student")


class Lecture(Base):
    __tablename__ = "lectures"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    type: Mapped[str]
    location: Mapped[str]
    teachers: Mapped[str]
    start_time: Mapped[datetime] = mapped_column(index=True)
    student_id: Mapped[int] = mapped_column(
        ForeignKey("students.id", ondelete="CASCADE"), index=True)
    is_sended: Mapped[bool] = mapped_column(default=False, index=True)

    student: Mapped["Student"] = relationship(back_populates="lectures")
