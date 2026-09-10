from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, ForeignKey, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models.property import Property
    from app.models.lease import Lease
    from app.models.maintenance_request import MaintenanceRequest

class Unit(Base):
    __tablename__ = "units"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    property_id: Mapped[int] = mapped_column(
        ForeignKey("properties.id"),
        nullable=False,
        index=True,
    )

    property: Mapped["Property"] = relationship(
    "Property",
    back_populates="units",
    )  

    leases: Mapped[list["Lease"]] = relationship(
    "Lease",
    back_populates="unit",
    ) 

    maintenance_requests: Mapped[list["MaintenanceRequest"]] = relationship(
    "MaintenanceRequest",
    back_populates="unit",
    )          

    unit_number: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    monthly_rent: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    is_occupied: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )