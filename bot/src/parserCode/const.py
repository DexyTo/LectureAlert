from os import getenv
from dotenv import load_dotenv

load_dotenv()

modeus_token: str | None = getenv("MODEUS_TOKEN")
if modeus_token is None:
    raise KeyError("В файле .env не найден MODEUS_TOKEN")

headers: dict[str, str] = {
    "authority": "urfu.modeus.org",
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ru-RU",
    "authorization": modeus_token,
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 YaBrowser/25.2.0.0 Safari/537.36"
}
get_people_url: str = "https://urfu.modeus.org/schedule-calendar-v2/api/people/persons/search"
get_schedule_url: str = "https://urfu.modeus.org/schedule-calendar-v2/api/calendar/events/search?tz=Asia/Yekaterinburg"
