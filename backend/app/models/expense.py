from datetime import datetime
from decimal import Decimal
from app.core.time import utc_now

from sqlalchemy import DateTime, ForeignKey, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    property_id: Mapped[int] = mapped_column(
        ForeignKey("properties.id"),
        nullable=False,
        index=True,
    )

    unit_id: Mapped[int | None] = mapped_column(
        ForeignKey("units.id"),
        nullable=True,
        index=True,
    )

    category: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    expense_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    payment_method: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    reference: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
    )