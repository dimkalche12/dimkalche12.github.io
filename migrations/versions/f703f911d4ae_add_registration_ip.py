"""add registration IP

Revision ID: f703f911d4ae
Revises: f69d7fec88d6
Create Date: 2018-07-09 13:04:50.652781

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f703f911d4ae'
down_revision = 'f69d7fec88d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('registration_ip', sa.Binary(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'registration_ip')
    # ### end Alembic commands ###
