import sqlalchemy as sa
from sqlalchemy.orm import Mapped
from datetime import datetime
from uuid import uuid4
from commons.db import Base



class Users(Base):
    __tablename__ = "user"

    id: Mapped[str] = sa.Column(sa.String, primary_key=True, default=lambda: str(uuid4()))  # type: ignore
    username: Mapped[str] = sa.Column(sa.String, nullable=False, unique=True)  # type: ignore
    email: Mapped[str] = sa.Column(sa.String, nullable=False)  # type: ignore
    password: Mapped[str] = sa.Column(sa.String, nullable=False)  # type: ignore
    first_name: Mapped[str] = sa.Column(sa.String, nullable=True)  # type: ignore
    last_name: Mapped[str] = sa.Column(sa.String, nullable=True)  # type: ignore
    bio: Mapped[str] = sa.Column(sa.String, nullable=True)  # type: ignore
    nationally: Mapped[str] = sa.Column(sa.String, nullable=True)  # type: ignore
