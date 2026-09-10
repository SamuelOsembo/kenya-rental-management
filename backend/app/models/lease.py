from datetime import date, datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Date, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models.tenant import Tenant
    from app.models.unit import Unit
    from app.models.rent_charge import RentCharge

class Lease(Base):
    __tablename__ = "leases"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    tenant_id: Mapped[int] = mapped_column(
        ForeignKey("tenants.id"),
        nullable=False,
        index=True,
    )

    tenant: Mapped["Tenant"] = relationship(
    "Tenant",
    back_populates="leases",
    )

    unit_id: Mapped[int] = mapped_column(
        ForeignKey("units.id"),
        nullable=False,
        index=True,
    )
    unit: Mapped["Unit"] = relationship(
    "Unit",
    back_populates="leases",
    )

    rent_charges: Mapped[list["RentCharge"]] = relationship(
    "RentCharge",
    back_populates="lease",
    )

    start_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    end_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    monthly_rent: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    security_deposit: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        default=0,
        nullable=False,
    )

    rent_due_day: Mapped[int] = mapped_column(
        nullable=False,
        default=5,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )