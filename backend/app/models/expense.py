from sqlalchemy import Date
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Time
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from decimal import Decimal
from datetime import date, time, datetime

from sqlalchemy import DateTime
from sqlalchemy import func

from app.db.database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    expense_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    expense_time: Mapped[time | None] = mapped_column(
        Time,
        nullable=True,
    )

    description: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        nullable=False,
    )