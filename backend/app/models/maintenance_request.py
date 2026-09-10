from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import DateTime, ForeignKey, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models.property import Property
    from app.models.unit import Unit
    from app.models.tenant import Tenant
    from app.models.user import User

class MaintenanceRequest(Base):
    __tablename__ = "maintenance_requests"

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
    back_populates="maintenance_requests",
    )

    unit_id: Mapped[int | None] = mapped_column(
        ForeignKey("units.id"),
        nullable=True,
        index=True,
    )

    unit: Mapped["Unit | None"] = relationship(
    "Unit",
    back_populates="maintenance_requests",
    )

    tenant_id: Mapped[int | None] = mapped_column(
        ForeignKey("tenants.id"),
        nullable=True,
        index=True,
    )

    tenant: Mapped["Tenant | None"] = relationship(
    "Tenant",
    back_populates="maintenance_requests",
    )

    title: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    category: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    priority: Mapped[str] = mapped_column(
        String(20),
        default="medium",
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="reported",
        nullable=False,
    )

    assigned_to: Mapped[int | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True,
        index=True,
    )

    assigned_user: Mapped["User | None"] = relationship(
    "User",
    foreign_keys=[assigned_to],
    back_populates="assigned_maintenance_requests",
    )

    estimated_cost: Mapped[float | None] = mapped_column(
        Numeric(12, 2),
        nullable=True,
    )

    actual_cost: Mapped[float | None] = mapped_column(
        Numeric(12, 2),
        nullable=True,
    )

    resolution_notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    reported_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    resolved_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    closed_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )