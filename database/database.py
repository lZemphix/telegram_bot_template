from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from .config import settings

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False
)
sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=False
)

class Base(DeclarativeBase):
    pass

async_session_factory = async_sessionmaker(async_engine)
session_factory = sessionmaker(sync_engine)

