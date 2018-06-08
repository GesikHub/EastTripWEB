"""route

Revision ID: 73147afad10e
Revises: 43355abbf8fb
Create Date: 2018-06-08 09:04:40.735441

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '73147afad10e'
down_revision = '43355abbf8fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('date_main_window',
    sa.Column('time_zone', sa.Integer(), nullable=False),
    sa.Column('weather', sa.Integer(), nullable=True),
    sa.Column('euro', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('time_zone')
    )
    op.create_table('language',
    sa.Column('id_language', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=5), nullable=True),
    sa.PrimaryKeyConstraint('id_language')
    )
    op.create_table('route',
    sa.Column('id_route', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('language', sa.Integer(), nullable=True),
    sa.Column('average_check', sa.Float(), nullable=True),
    sa.Column('time', sa.Float(), nullable=True),
    sa.Column('distance', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['language'], ['language.id_language'], ),
    sa.PrimaryKeyConstraint('id_route')
    )
    op.create_table('point',
    sa.Column('id_point', sa.Integer(), nullable=False),
    sa.Column('id', sa.String(length=10), nullable=True),
    sa.Column('latitude', sa.String(length=15), nullable=True),
    sa.Column('longitude', sa.String(length=15), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('subtitle', sa.String(length=100), nullable=True),
    sa.Column('illustration', sa.String(length=100), nullable=True),
    sa.Column('route', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['route'], ['route.id_route'], ),
    sa.PrimaryKeyConstraint('id_point')
    )
    op.drop_table('comfort_place')
    op.drop_table('time_table_day')
    op.drop_table('place_user')
    op.drop_table('translate')
    op.drop_table('comfort')
    op.drop_table('client')
    op.drop_table('payment_method_place')
    op.drop_table('photo')
    op.drop_table('place')
    op.drop_table('time_table')
    op.drop_table('payment_method')
    op.drop_table('category_place')
    op.drop_table('category')
    op.drop_table('finance')
    op.create_foreign_key(None, 'user', 'role', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.create_table('finance',
    sa.Column('id_finance', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('average_check', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('currency', mysql.ENUM('USD', 'UAH', 'EUR'), nullable=True),
    sa.Column('id_place', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id_finance'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_table('category',
    sa.Column('id_category', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=12), nullable=True),
    sa.Column('id_supergroup', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id_category'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_table('category_place',
    sa.Column('id_category_place', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_place', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('id_category', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id_category_place'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_table('payment_method',
    sa.Column('id_payment_method', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('type', mysql.ENUM('DebitCard', 'CreditCard', 'ElectronicPayment'), nullable=True),
    sa.PrimaryKeyConstraint('id_payment_method'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_table('time_table',
    sa.Column('id_timetable', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('open_time', mysql.TIME(), nullable=True),
    sa.Column('close_time', mysql.TIME(), nullable=True),
    sa.PrimaryKeyConstraint('id_timetable'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_table('place',
    sa.Column('id_place', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('description', mysql.VARCHAR(length=500), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=350), nullable=True),
    sa.Column('website', mysql.VARCHAR(length=70), nullable=True),
    sa.Column('country', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('city', mysql.VARCHAR(length=150), nullable=True),
    sa.Column('location', mysql.VARCHAR(length=40), nullable=True),
    sa.Column('address', mysql.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id_place'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_table('photo',
    sa.Column('id_photo', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('url', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('id_place', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id_photo'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_table('payment_method_place',
    sa.Column('id_payment_place', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_place', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('id_payment_method', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id_payment_place'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_table('client',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('token', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('id_user', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_table('comfort',
    sa.Column('id_comfort', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('type', mysql.ENUM('Socket', 'WelcomeTourists', 'ForChildren', 'AnimalAccess', 'RentBikes', 'Polygraph', 'Ramp', 'SpecialToilet', 'SpecialService'), nullable=True),
    sa.PrimaryKeyConstraint('id_comfort'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_table('translate',
    sa.Column('id_translate', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('language', mysql.ENUM('RUS', 'ENG'), nullable=True),
    sa.Column('name', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('description', mysql.VARCHAR(length=500), nullable=True),
    sa.Column('address', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('id_place', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id_translate'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_table('place_user',
    sa.Column('id_place_user', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_user', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('id_place', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id_place_user'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_table('time_table_day',
    sa.Column('id_timetable_day', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('day', mysql.ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'), nullable=True),
    sa.Column('id_place', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('id_timetable', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id_timetable_day'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.create_table('comfort_place',
    sa.Column('id_comfort_place', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('id_place', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('id_comfort', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id_comfort_place'),
    mysql_default_charset='utf8',
    mysql_engine='MyISAM'
    )
    op.drop_table('point')
    op.drop_table('route')
    op.drop_table('language')
    op.drop_table('date_main_window')
    # ### end Alembic commands ###
