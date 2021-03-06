"""empty message

Revision ID: 83996de3318b
Revises: c6cc2a1a57d4
Create Date: 2021-01-20 22:27:13.943463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83996de3318b'
down_revision = 'c6cc2a1a57d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###
