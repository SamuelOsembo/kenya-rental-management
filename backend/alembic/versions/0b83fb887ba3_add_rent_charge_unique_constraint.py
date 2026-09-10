"""add rent charge unique constraint

Revision ID: 0b83fb887ba3
Revises: 
Create Date: 2026-09-10 19:47:26.240460

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0b83fb887ba3'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    with op.batch_alter_table("rent_charges", schema=None) as batch_op:
        batch_op.create_unique_constraint(
            "uq_rent_charge_lease_period",
            ["lease_id", "rent_period"],
        )


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table("rent_charges", schema=None) as batch_op:
        batch_op.drop_constraint(
            "uq_rent_charge_lease_period",
            type_="unique",
        )