from datetime import datetime
from app.core.time import utc_now

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models.lease import Lease
    from app.models.maintenance_request import MaintenanceRequest
    from app.models.notification import Notification

class Tenant(Base):
    __tablename__ = "tenants"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    leases: Mapped[list["Lease"]] = relationship(
    "Lease",
    back_populates="tenant",
    )

    maintenance_requests: Mapped[list["MaintenanceRequest"]] = relationship(
    "MaintenanceRequest",
    back_populates="tenant",
    )

    notifications: Mapped[list["Notification"]] = relationship(
    "Notification",
    back_populates="tenant",
    )

    full_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    phone: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        index=True,
    )

    email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    id_number: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    emergency_contact_name: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    emergency_contact_phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
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