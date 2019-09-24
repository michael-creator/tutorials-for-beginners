"""Initial Migration

Revision ID: 0c493659ac26
Revises: 
Create Date: 2019-09-24 10:31:39.358073

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0c493659ac26'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('content', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('post')
    op.add_column('users', sa.Column('usersname', sa.String(length=255), nullable=True))
    op.drop_constraint('users_email_key', 'users', type_='unique')
    op.drop_constraint('users_username_key', 'users', type_='unique')
    op.drop_column('users', 'password')
    op.drop_column('users', 'image_file')
    op.drop_column('users', 'email')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.VARCHAR(length=20), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('image_file', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('password', sa.VARCHAR(length=60), autoincrement=False, nullable=False))
    op.create_unique_constraint('users_username_key', 'users', ['username'])
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    op.drop_column('users', 'usersname')
    op.create_table('post',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('data_posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('content', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='post_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='post_pkey')
    )
    op.drop_table('posts')
    # ### end Alembic commands ###