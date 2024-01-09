"""Add properties_id column to propertiesImages

Revision ID: cac716da3f98
Revises: 2933fe2b2519
Create Date: 2024-01-09 23:10:19.661483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cac716da3f98'
down_revision = '2933fe2b2519'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('propertiesImages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('properties_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key('fk_properties_id', 'properties', ['properties_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('propertiesImages', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('properties_id')

    # ### end Alembic commands ###