import aiohttp
from parserCode.const import headers, get_people_url


async def get_student_id(fullname: str) -> str:
    edited_fullname: str = " ".join([i.capitalize() for i in fullname.split()])
    payload: dict[str, str] = {
        "fullName": edited_fullname,
        "page": "0",
        "size": "1",
        "sort": "+fullName"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(get_people_url, headers=headers, json=payload) as response:
            if response.status == 200:
                students = await response.json()
                if students["_embedded"].get("persons"):
                    if students["_embedded"]["persons"][0]["fullName"] != edited_fullname:
                        raise ValueError("Студент не найден")
                    return students["_embedded"]["persons"][0]["id"]
                raise ValueError("Студент не найден")
            elif response.status == 401:
                raise RuntimeError(f"ошибка {response.status}. {response.text}")
            raise ValueError(
                f"Не удалось отправить POST запрос для получения студента с именем {fullname}: ошибка {response.status}. {response.text}")
