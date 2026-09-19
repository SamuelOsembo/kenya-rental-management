from datetime import datetime
from app.core.time import utc_now

from sqlalchemy import Boolean, CheckConstraint, DateTime, String

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.database import Base
if TYPE_CHECKING:
    from app.models.property import Property
    from app.models.maintenance_request import MaintenanceRequest
    from app.models.notification import Notification


class User(Base):
    __tablename__ = "users"

    __table_args__ = (
        CheckConstraint(
            "role IN ('admin', 'landlord', 'property_manager', 'staff')",
            name="ck_user_role_valid",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    full_name: Mapped[str] = mapped_column(String(150), nullable=False)

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False,
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
        unique=True,
        nullable=True,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    role: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="landlord",
        index=True,
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

    properties: Mapped[list["Property"]] = relationship(
    "Property",
    back_populates="landlord",
    )

    assigned_maintenance_requests: Mapped[list["MaintenanceRequest"]] = relationship(
    "MaintenanceRequest",
    foreign_keys="MaintenanceRequest.assigned_to",
    back_populates="assigned_user",
    )

    notifications: Mapped[list["Notification"]] = relationship(
    "Notification",
    back_populates="user",
    )