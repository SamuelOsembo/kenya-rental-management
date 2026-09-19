from datetime import date, datetime
from app.core.time import utc_now
from decimal import Decimal
from typing import TYPE_CHECKING
from sqlalchemy import Boolean, CheckConstraint, Date, DateTime, ForeignKey, Index, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models.tenant import Tenant
    from app.models.unit import Unit
    from app.models.rent_charge import RentCharge

class Lease(Base):
    __tablename__ = "leases"

    __table_args__ = (
    CheckConstraint(
        "monthly_rent >= 0",
        name="ck_lease_monthly_rent_nonnegative",
    ),
    CheckConstraint(
        "security_deposit >= 0",
        name="ck_lease_security_deposit_nonnegative",
    ),
    CheckConstraint(
        "rent_due_day BETWEEN 1 AND 31",
        name="ck_lease_rent_due_day_valid",
    ),
    CheckConstraint(
        "end_date IS NULL OR end_date >= start_date",
        name="ck_lease_dates_valid",
    ),
)

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
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
    )


Index(
    "uq_lease_active_unit",
    Lease.unit_id,
    unique=True,
    sqlite_where=Lease.is_active.is_(True),
    postgresql_where=Lease.is_active.is_(True),
)