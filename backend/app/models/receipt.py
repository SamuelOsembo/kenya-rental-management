from datetime import datetime
from app.core.time import utc_now

from decimal import Decimal

from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models.payment import Payment

class Receipt(Base):
    __tablename__ = "receipts"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    payment_id: Mapped[int] = mapped_column(
        ForeignKey("payments.id"),
        nullable=False,
        unique=True,
        index=True,
    )

    payment: Mapped["Payment"] = relationship(
    "Payment",
    back_populates="receipt",
    )

    receipt_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    issued_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
    )

    pdf_path: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    whatsapp_status: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    email_status: Mapped[str | None] = mapped_column(
        String(20),
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