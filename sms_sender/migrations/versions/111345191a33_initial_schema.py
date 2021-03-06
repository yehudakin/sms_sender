"""empty message

Revision ID: 111345191a33
Revises: 
Create Date: 2019-03-11 23:32:12.518462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '111345191a33'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('currency_balance', sa.Float(), nullable=True),
    sa.Column('is_sms_verified', sa.Boolean(), nullable=True),
    sa.Column('sms_verification_code', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sms_events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('recipient_phone_number', sa.String(), nullable=True),
    sa.Column('account_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sms_events')
    op.drop_table('accounts')
    # ### end Alembic commands ###
