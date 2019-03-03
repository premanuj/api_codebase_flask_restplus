"""empty message

Revision ID: 4678868d2814
Revises: 
Create Date: 2019-02-24 13:13:56.874303

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import uuid

# revision identifiers, used by Alembic.
revision = "4678868d2814"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sqlalchemy_utils.types.uuid.UUIDType(), default=uuid.uuid4, nullable=False),
        sa.Column("email", sqlalchemy_utils.types.email.EmailType(length=255), nullable=False),
        sa.Column("password", sqlalchemy_utils.types.PasswordType(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    # ### end Alembic commands ###
