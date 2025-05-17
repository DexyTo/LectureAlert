from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    waiting_for_name = State()
    waiting_for_notification_time = State()
    setting_notifications = State()
    waiting_for_new_notification_time = State()
