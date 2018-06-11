"""id

Revision ID: 91da49a9be8f
Revises: bb92a633fb5f
Create Date: 2018-06-11 15:59:19.673506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91da49a9be8f'
down_revision = 'bb92a633fb5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'point_name', 'route', ['id_route'], ['id_route'])
    op.create_foreign_key(None, 'point_name', 'point', ['id_point'], ['id'])
    op.create_foreign_key(None, 'point_name', 'language', ['language'], ['id_language'])
    op.create_foreign_key(None, 'route_name', 'language', ['language'], ['id_language'])
    op.create_foreign_key(None, 'route_name', 'route', ['id_route'], ['id_route'])
    op.create_foreign_key(None, 'user', 'role', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_constraint(None, 'route_name', type_='foreignkey')
    op.drop_constraint(None, 'route_name', type_='foreignkey')
    op.drop_constraint(None, 'point_name', type_='foreignkey')
    op.drop_constraint(None, 'point_name', type_='foreignkey')
    op.drop_constraint(None, 'point_name', type_='foreignkey')
    # ### end Alembic commands ###