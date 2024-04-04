from models.database import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Users(db.Model):
    __tablename__ = "users"
    seq: Mapped[int] = mapped_column(primary_key=True)
    batch: Mapped[int] = mapped_column(nullable=False)
    id: Mapped[int] = mapped_column(unique=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    password: Mapped[str] = mapped_column(String(150), default=0)
