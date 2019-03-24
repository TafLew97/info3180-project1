"""empty message

Revision ID: dc7ec82a6d2b
Revises: 0ac73d9ee66a
Create Date: 2019-03-23 08:46:01.381495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc7ec82a6d2b'
down_revision = '0ac73d9ee66a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('filename', sa.String(), nullable=True))
    op.drop_column('profiles', 'photo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('photo', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('profiles', 'filename')
    # ### end Alembic commands ###