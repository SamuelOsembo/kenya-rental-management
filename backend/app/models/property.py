from datetime import datetime
from app.core.time import utc_now
from typing import TYPE_CHECKING 

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.unit import Unit
    from app.models.maintenance_request import MaintenanceRequest


class Property(Base):
    __tablename__ = "properties"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    landlord_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    landlord: Mapped["User"] = relationship(
        "User",
        back_populates="properties",
    )

    units: Mapped[list["Unit"]] = relationship(
    "Unit",
    back_populates="property",  
    )

    maintenance_requests: Mapped[list["MaintenanceRequest"]] = relationship(
    "MaintenanceRequest",
    back_populates="property",
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    address: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    city: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
    )