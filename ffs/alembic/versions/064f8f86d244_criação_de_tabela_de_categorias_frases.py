"""Criação de tabela de categorias_frases

Revision ID: 064f8f86d244
Revises: 49ec18a5d6b3
Create Date: 2019-08-11 22:41:09.374428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '064f8f86d244'
down_revision = '49ec18a5d6b3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'categorias_frases',
        sa.Column('id_categoria', sa.Integer, sa.ForeignKey('categoria.id_categoria'), nullable=False),
        sa.Column('id_frase', sa.Integer, sa.ForeignKey('frase.id_frase'), nullable=False),
    )
    

def downgrade():
    op.drop_table('categorias_frases')
