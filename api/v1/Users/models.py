from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import TINYINT
from api.v1.shared.base import Base


class User(Base):
    __tablename__ = "users_table"

    name: Mapped[str] = mapped_column(String(64), nullable=False, unique=True)
    number: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    saldo: Mapped[int] = mapped_column(Integer(), nullable=False, default=0)
    is_active: Mapped[bool] = mapped_column(TINYINT(), default=True, nullable=False)
