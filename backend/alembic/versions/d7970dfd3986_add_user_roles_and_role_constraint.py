"""Add user roles and role constraint

Revision ID: d7970dfd3986
Revises: 27bbb21ac542
Create Date: 2026-09-19 20:26:25.046530

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d7970dfd3986"
down_revision: Union[str, Sequence[str], None] = "27bbb21ac542"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "role",
                sa.String(length=30),
                nullable=False,
                server_default="landlord",
            )
        )

        batch_op.create_check_constraint(
            "ck_user_role_valid",
            "role IN ('admin', 'landlord', 'property_manager', 'staff')",
        )

        batch_op.create_index(
            "ix_users_role",
            ["role"],
            unique=False,
        )


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.drop_index(
            "ix_users_role",
        )

        batch_op.drop_constraint(
            "ck_user_role_valid",
            type_="check",
        )

        batch_op.drop_column("role")