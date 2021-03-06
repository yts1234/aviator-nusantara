"""Change some data type

Revision ID: a32cb528d162
Revises: b5df6fca8cf4
Create Date: 2020-08-23 22:45:21.049525

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a32cb528d162'
down_revision = 'b5df6fca8cf4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('flights', 'arrival_time',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('flights', 'departure_time',
               existing_type=mysql.DATETIME(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('flights', 'departure_time',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('flights', 'arrival_time',
               existing_type=mysql.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###
