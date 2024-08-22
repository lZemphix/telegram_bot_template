from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from .config import settings

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False
)
psyco_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=False
)

sqlite_engine = create_engine(
    url=settings.DATABASE_URL_sqlite,
    echo=False
)

class Base(DeclarativeBase):
    pass

async_session_factory = async_sessionmaker(async_engine)
psyco_session_factory = sessionmaker(psyco_engine)
sqlite_session_factory = sessionmaker(sqlite_engine)


