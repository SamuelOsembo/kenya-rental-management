from datetime import datetime
from app.core.time import utc_now

from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

if TYPE_CHECKING:
    from app.models.notification import Notification


class NotificationLog(Base):
    __tablename__ = "notification_logs"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    notification_id: Mapped[int] = mapped_column(
        ForeignKey("notifications.id"),
        nullable=False,
        index=True,
    )

    notification: Mapped["Notification"] = relationship(
    "Notification",
    back_populates="logs",
    )

    channel: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    provider_message_id: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    error_message: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    sent_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    delivered_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    read_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
    DateTime(timezone=True),
    default=utc_now,
    nullable=False,
)