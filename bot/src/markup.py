from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)

def get_schedule_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(
                text="Загрузить расписание",
                callback_data="load_schedule"
            )
        ]]
    )

def get_settings_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="⚙️Настройки")]],
        resize_keyboard=True,
        one_time_keyboard=False
    )

def get_notification_settings_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="🔔Включить/🔕Выключить уведомления",
                callback_data="change_notification_status"
            )],
            [InlineKeyboardButton(
                text="✏️Изменить время уведомления",
                callback_data="change_notification_time"
            )],
            [InlineKeyboardButton(
                text="⛪️Отправлять/Не отправлять фото",
                callback_data="change_sending_photo_status"
            )]
        ]
    )