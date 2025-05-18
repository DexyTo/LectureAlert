# LectureAlert - Цифровой помощник для студентов 🚀

**Telegram-бот**, который напоминает о лекциях, показывает расположение аудиторий и отвечает на частые вопросы студентов.

## 🔥 Возможности

- ⏰ **Автоматические уведомления** о ближайших лекциях (за указанное время)
- 🏫 **Карта аудиторий** в одном сообщении
- ❓ **FAQ** с ответами на популярные вопросы
- ⚙️ **Гибкие настройки** времени напоминаний
- 🔄 **Синхронизация** с расписанием Modeus (раз в неделю)

## 🛠 Технологический стек

| Компонент       | Технологии                          |
|-----------------|-------------------------------------|
| **Frontend**    | JavaScript, React, Vite, DaisyUI    |
| **Backend**     | Python (FastAPI, aiogram)           |
| **База данных** | PostgreSQL                          |
| **Инфраструктура** | Docker                           |

## 🚀 Быстрый старт

### Предварительные требования
- Python 3.10+
- Node.js 16+
- Telegram-аккаунт

### Установка

```bash
# Клонируем репозиторий
git clone https://github.com/yourusername/LectureAlert.git

#Создаем виртуальное окружение и активируем его
python -m venv venv
venv\Sripts\activate

# Устанавливаем зависимости для бота и backend-части
pip install -r requirements.txt

#Создаем в корне проекта файл .env с переменными окружения
MODEUS_TOKEN=...
BOT_TOKEN=..

DB_HOST=...
DB_PORT=...
DB_USER=...
DB_PASS=...
DB_NAME=...

# Устанавливаем фронтенд (админ-панель)
- Устанавливаем Node.js и npm
- cd .\frontend\
- npm create vite@latest admin-panel -- --template react
- cd admin-panel
- npm install
- npm install react-router-dom axios @tanstack/react-query tailwindcss @tailwindcss/vite daisyui
- npm run dev

# Запуск 
python bot\src\main.py