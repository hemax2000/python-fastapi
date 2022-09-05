import sqlalchemy as sa
from sqlalchemy.orm import Mapped
from datetime import datetime
from uuid import uuid4
from commons.db import Base



class Books(Base):
    __tablename__ = "books"

    id: Mapped[str] = sa.Column(sa.String, primary_key=True, default=lambda: str(uuid4()))  # type: ignore
    created_at: Mapped[datetime] = sa.Column(sa.DateTime, nullable=False, default=datetime.now)  # type: ignore
    title: Mapped[str] = sa.Column(sa.String, nullable=False)  # type: ignore
    completed: Mapped[bool] = sa.Column(sa.Boolean, nullable=False, default=False)  # type: ignore
    page_num: Mapped[int] = sa.Column(sa.Integer, nullable=False, default=0) # type: ignore
    user_id: Mapped[str] = sa.Column(sa.String, nullable=False, index=True)  # type: ignore
