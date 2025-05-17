from os import getenv
from dataclasses import dataclass
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from .models import Base


@dataclass
class Settings():
    DB_HOST: str | None = getenv("DB_HOST")
    DB_PORT: str | None = getenv("DB_PORT")
    DB_USER: str | None = getenv("DB_USER")
    DB_PASS: str | None = getenv("DB_PASS")
    DB_NAME: str | None = getenv("DB_NAME")


settings = Settings()


def database_URL_asyncpg():
    return f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"


async_engine = create_async_engine(
    url=database_URL_asyncpg(),
    echo=False,
)

async_session_factory = async_sessionmaker(async_engine)


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all, checkfirst=False)
        await conn.run_sync(Base.metadata.create_all)
