from database.models import UsersOrm
from .database import async_engine, async_session_factory
from sqlalchemy import select
import logging

logging.basicConfig(level=logging.DEBUG, filename="logs/logs.log", format="%(asctime)s - %(levelname)s - %(message)s")
class TableActions:

    @staticmethod
    async def create_tables():
        async with async_engine.connect() as conn:
            await conn.run_sync(UsersOrm.metadata.create_all)
            logging.debug('[create_tables] tables created!')
            await conn.commit()

    @staticmethod
    async def drop_tables():
        async with async_engine.connect() as conn:
            await conn.run_sync(UsersOrm.metadata.drop_all)
            logging.debug('[drop_tables] tables dropped!')
            await conn.commit()

class UsersActions:

    @staticmethod
    async def add_user(username: str, uid: int):
        async with async_session_factory() as session:
            new_user = UsersOrm(username=username, uid=uid)
            session.add(new_user)
            logging.debug('[add_user] user added!')
            await session.commit()

    @staticmethod
    async def check_user(uid: int):
        async with async_engine.connect() as conn:
            logging.debug('[check_user] connecting to check_user')
            user = await conn.execute(select(UsersOrm).where(UsersOrm.uid == uid))
            return False if user.fetchmany() == [] else True
    
users_actions = UsersActions()
table_actions = TableActions()

    