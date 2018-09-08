"""followers and following db setup

Revision ID: 94121c48c793
Revises: af7684373577
Create Date: 2018-09-09 04:49:42.265560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94121c48c793'
down_revision = 'af7684373577'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
