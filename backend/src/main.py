import os
import shutil
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from auth import router as auth_router
from pathlib import Path
import sys

# Путь до LectureAlert/
BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(BASE_DIR))

from database.models import StudentSchema
from database.crud import get_all_students


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

IMAGES_DIR = BASE_DIR / "location_images/floors"


@app.get("/api/students")
async def get_students() -> list[StudentSchema]:
    students = await get_all_students()
    return students


@app.post("/api/update-floor-image")
async def update_floor_image(file: UploadFile = File(...),
                             file_name: str = Form(...)):
    
    for existing_file in os.listdir(IMAGES_DIR):
        file_path = os.path.join(IMAGES_DIR, existing_file)
        if existing_file.startswith(file_name):
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
    
    return {"success": True}

app.include_router(auth_router)