"""empty message

Revision ID: 804fbe48dec2
Revises: 395fc57941fa
Create Date: 2023-12-11 10:14:25.508592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '804fbe48dec2'
down_revision = '395fc57941fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('surname', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('copies', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    op.drop_table('author')
    # ### end Alembic commands ###
