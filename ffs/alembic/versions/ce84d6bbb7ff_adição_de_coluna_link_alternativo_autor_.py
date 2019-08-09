"""Adição de coluna link_alternativo_autor na tabela autor

Revision ID: ce84d6bbb7ff
Revises: 33f36d115d9b
Create Date: 2019-08-08 21:33:03.403766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce84d6bbb7ff'
down_revision = '33f36d115d9b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('autor',
                  sa.Column('link_alternativo_autor', sa.String(),
                            nullable=True))
    


def downgrade():
    op.drop_column('autor', 'link_alternativo_autor')
    
