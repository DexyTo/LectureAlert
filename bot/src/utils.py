from functools import lru_cache
from pathlib import Path
import re
from typing import Optional


@lru_cache()
def get_photo_path(location: str) -> Optional[Path]:
    location_map = {
        "Р": "rtf", "МТ": "inmit", "Х": "hti",
        "Г": "guk", "Э": "guk", "И": "guk", "М": "guk",
        "Т": "anin", "С": "isa", "СП": "isa", "У": "ugi"
    }

    if match := re.search(r'(Р|МТ|Х|Г|Э|И|М)(0|1[0-9]?|[2-9])\d{2}', location):
        building = location_map[match.group(1)]
        floor = match.group(2)
        return Path(__file__).parent.parent.parent / "location_images" / "schemas" / f"{building}{floor}.jpg"
    return None


def format_notification_text(lecture) -> str:
    return (
        f"🔔 Внимание, скоро лекция!\n"
        f"📚 {lecture.name}\n"
        f"{lecture.type}\n"
        f"👨‍🏫 {lecture.teachers}\n"
        f"🏫 {lecture.location}\n"
        f"🕰 {lecture.start_time.strftime('%H:%M')}"
    )
