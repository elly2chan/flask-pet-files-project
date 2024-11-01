"""Add users, pets, products and orders tables

Revision ID: 0e3d212cebc7
Revises: 
Create Date: 2024-10-31 21:43:07.267273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e3d212cebc7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.Enum('pending', 'approved', 'rejected', name='state'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('gender', sa.Enum('female', 'male', name='gender'), nullable=False),
    sa.Column('date_of_birth', sa.DateTime(), nullable=True),
    sa.Column('breed', sa.String(length=255), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('owner_email', sa.String(length=255), nullable=False),
    sa.Column('pet_type', sa.Enum('dog', 'cat', name='pettype'), nullable=False),
    sa.Column('is_stray', sa.Boolean(), nullable=True),
    sa.Column('european_passport', sa.Boolean(), nullable=True),
    sa.Column('microchip', sa.Boolean(), nullable=True),
    sa.Column('microchip_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('added_on', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('photo_url', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('role', sa.Enum('user', 'admin', name='roletype'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('products')
    op.drop_table('pets')
    op.drop_table('orders')
    # ### end Alembic commands ###
