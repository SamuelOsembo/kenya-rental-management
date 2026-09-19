from alembic import op


# revision identifiers, used by Alembic.
revision = "527dd28ccced"
down_revision = "0b83fb887ba3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Add lease business rule constraints."""
    with op.batch_alter_table("leases", schema=None) as batch_op:
        batch_op.create_check_constraint(
            "ck_lease_monthly_rent_nonnegative",
            "monthly_rent >= 0",
        )
        batch_op.create_check_constraint(
            "ck_lease_security_deposit_nonnegative",
            "security_deposit >= 0",
        )
        batch_op.create_check_constraint(
            "ck_lease_rent_due_day_valid",
            "rent_due_day BETWEEN 1 AND 31",
        )
        batch_op.create_check_constraint(
            "ck_lease_dates_valid",
            "end_date IS NULL OR end_date >= start_date",
        )


def downgrade() -> None:
    """Remove lease business rule constraints."""
    with op.batch_alter_table("leases", schema=None) as batch_op:
        batch_op.drop_constraint(
            "ck_lease_dates_valid",
            type_="check",
        )
        batch_op.drop_constraint(
            "ck_lease_rent_due_day_valid",
            type_="check",
        )
        batch_op.drop_constraint(
            "ck_lease_security_deposit_nonnegative",
            type_="check",
        )
        batch_op.drop_constraint(
            "ck_lease_monthly_rent_nonnegative",
            type_="check",
        )