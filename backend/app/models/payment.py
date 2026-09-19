from datetime import datetime
from app.core.time import utc_now

from decimal import Decimal

from decimal import Decimal

from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models.rent_charge import RentCharge
    from app.models.receipt import Receipt
    from app.models.mpesa_transaction import MpesaTransaction

class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    rent_charge_id: Mapped[int] = mapped_column(
        ForeignKey("rent_charges.id"),
        nullable=False,
        index=True,
    )

    rent_charge: Mapped["RentCharge"] = relationship(
    "RentCharge",
    back_populates="payments",
    )

    receipt: Mapped["Receipt"] = relationship(
    "Receipt",
    back_populates="payment",
    uselist=False,
    )

    mpesa_transaction: Mapped["MpesaTransaction"] = relationship(
    "MpesaTransaction",
    back_populates="payment",
    uselist=False,
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    payment_method: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    reference: Mapped[str | None] = mapped_column(
        String(100),
        unique=True,
        nullable=True,
    )

    payment_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="confirmed",
        nullable=False,
    )

    notes: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
    )