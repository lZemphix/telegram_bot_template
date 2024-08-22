from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import MetaData, BigInteger
from .database import Base

metadata = MetaData()

class UsersOrm(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    uid: Mapped[int] = mapped_column(BigInteger)
    username: Mapped[str] = mapped_column(nullable=True, default='wo_nickname')
    