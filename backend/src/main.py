from fastapi import FastAPI
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Путь до LectureAlert/
sys.path.append(str(BASE_DIR))

from database.crud import get_all_students
from database.models import StudentSchema

app = FastAPI()


@app.get("/api/students")
async def get_students() -> list[StudentSchema]:
    students = await get_all_students()
    return students
