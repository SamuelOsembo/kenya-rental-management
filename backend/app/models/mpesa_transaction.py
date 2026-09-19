from datetime import datetime
from app.core.time import utc_now

from decimal import Decimal
from typing import TYPE_CHECKING
from sqlalchemy import DateTime, ForeignKey, JSON, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models.payment import Payment

class MpesaTransaction(Base):
    __tablename__ = "mpesa_transactions"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    payment_id: Mapped[int | None] = mapped_column(
        ForeignKey("payments.id"),
        nullable=True,
        index=True,
    )

    payment: Mapped["Payment"] = relationship(
    "Payment",
    back_populates="mpesa_transaction",
    )

    channel: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    phone_number: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    mpesa_receipt_number: Mapped[str | None] = mapped_column(
        String(50),
        unique=True,
        nullable=True,
    )

    account_reference: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    merchant_request_id: Mapped[str | None] = mapped_column(
        String(100),
        unique=True,
        nullable=True,
    )

    checkout_request_id: Mapped[str | None] = mapped_column(
        String(100),
        unique=True,
        nullable=True,
    )

    transaction_date: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="pending",
        nullable=False,
    )

    result_code: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    result_description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    raw_callback: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
    )