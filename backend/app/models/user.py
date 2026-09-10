from datetime import datetime

from sqlalchemy import Boolean, DateTime, String

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.database import Base
if TYPE_CHECKING:
    from app.models.property import Property
    from app.models.maintenance_request import MaintenanceRequest
    from app.models.notification import Notification


class User(Base):
    __tablename__ = "users"

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