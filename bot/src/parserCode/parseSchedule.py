from dataclasses import dataclass
from datetime import datetime, timedelta
import aiohttp
from parserCode.const import headers, get_schedule_url
from parserCode.parseStudents import get_student_id


@dataclass
class Lesson:
    name: str
    type: str
    start_time: datetime
    end_time: datetime
    location: str
    teachers: str


async def get_sunday_dates() -> dict[str, str]:
    today: datetime = datetime.now()
    current_weekday: int = today.weekday()
    current_sunday: datetime = today + \
        timedelta(days=7 - (current_weekday + 1)
                  if current_weekday != 6 else 0)
    last_sunday: datetime = current_sunday - timedelta(weeks=1)
    time_min: str = last_sunday.replace(
        hour=19, minute=0, second=0, microsecond=0).isoformat() + "Z"
    time_max: str = current_sunday.replace(
        hour=19, minute=0, second=0, microsecond=0).isoformat() + "Z"

    return {"timeMin": time_min, "timeMax": time_max}


async def parse_schedule(student_name: str):
    student_id = await get_student_id(student_name)
    dates = await get_sunday_dates()
    payload = {
        "attendeePersonId": [student_id],
        "size": 500,
        "timeMin": dates["timeMin"],
        "timeMax": dates["timeMax"]
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(get_schedule_url, headers=headers, json=payload) as response:
            if response.status == 200:
                schedule = await response.json()
                return schedule
            raise ValueError(
                f"Не удалось отправить POST запрос для получения расписания студента: ошибка {response.status}. {response.text}")


async def get_schedule(fullname: str) -> list[Lesson]:
    data = await parse_schedule(fullname)

    events = data["_embedded"]["events"]
    course_units = {unit["id"]: unit["name"]
                    for unit in data["_embedded"]["course-unit-realizations"]}
    teachers = {person["id"]: person["fullName"]
                for person in data["_embedded"]["persons"]}

    locations = {}
    for loc in data["_embedded"]["event-locations"]:
        event_id = loc["eventId"]
        if loc.get("customLocation"):
            locations[event_id] = loc["customLocation"]

    rooms = {room["id"]: f"{room['name']} ({room['building']['nameShort']})"
             for room in data["_embedded"]["rooms"]}

    event_rooms = {}
    for er in data["_embedded"]["event-rooms"]:
        event_id = er["_links"]["event"]["href"].split("/")[-1]
        room_id = er["_links"]["room"]["href"].split("/")[-1]
        event_rooms[event_id] = rooms.get(room_id, "Неизвестная аудитория")

    event_teachers = {}
    for attendee in data["_embedded"]["event-attendees"]:
        event_id = attendee["_links"]["event"]["href"].split("/")[-1]
        teacher_id = attendee["_links"]["person"]["href"].split("/")[-1]
        if event_id not in event_teachers:
            event_teachers[event_id] = []
        event_teachers[event_id].append(teachers.get(teacher_id, "Неизвестно"))

    schedule: list[Lesson] = []
    for event in events:
        event_id = event["id"]
        course_id = event["_links"]["course-unit-realization"]["href"].split(
            "/")[-1]
        location = event_rooms.get(event_id) or locations.get(
            event_id) or "не определено"
        course = course_units.get(course_id, "Неизвестный курс")
        teachers = ", ".join(event_teachers.get(event_id, ["Нет данных"]))

        schedule.append(Lesson(course, event["name"], datetime.fromisoformat(event["start"]).replace(
            tzinfo=None), datetime.fromisoformat(event["end"]).replace(tzinfo=None), location, teachers))

    return schedule
