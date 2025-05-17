from .start import router as start_router
from .settings import router as settings_router
from .schedule import router as schedule_router
from .notifications import router as notifications_router

routers = [
    start_router,
    settings_router,
    schedule_router,
    notifications_router
]

__all__ = ['routers']