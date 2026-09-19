from datetime import date, datetime
from app.core.time import utc_now

from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Date, DateTime, ForeignKey, Numeric, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models.lease import Lease
    from app.models.payment import Payment
    

class RentCharge(Base):
    __tablename__ = "rent_charges"
    
    __table_args__ = (
    UniqueConstraint(
        "lease_id",
        "rent_period",
        name="uq_rent_charge_lease_period",
    ),
)

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    lease_id: Mapped[int] = mapped_column(
        ForeignKey("leases.id"),
        nullable=False,
        index=True,
    )

    lease: Mapped["Lease"] = relationship(
    "Lease",
    back_populates="rent_charges",
    )

    payments: Mapped[list["Payment"]] = relationship(
    "Payment",
    back_populates="rent_charge",
    )

    rent_period: Mapped[str] = mapped_column(
        String(7),
        nullable=False,
    )

    amount_due: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    due_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        index=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
    )