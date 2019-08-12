"""Remoção de coluna id_categoria das frases

Revision ID: 49ec18a5d6b3
Revises: ce84d6bbb7ff
Create Date: 2019-08-11 22:38:22.720332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49ec18a5d6b3'
down_revision = 'ce84d6bbb7ff'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('frase', 'id_categoria')


def downgrade():
    op.add_column('frase',
        sa.Column('id_categoria', sa.Integer, sa.ForeignKey("categoria.id_categoria"),nullable=False),)
