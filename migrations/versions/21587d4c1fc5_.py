"""empty message

Revision ID: 21587d4c1fc5
Revises: 
Create Date: 2018-11-18 21:03:32.871138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21587d4c1fc5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('apply_affiliation',
    sa.Column('seq', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('seq')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('apply_affiliation')
    # ### end Alembic commands ###
