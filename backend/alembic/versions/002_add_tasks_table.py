"""add tasks table

Revision ID: 002
Revises: 001
Create Date: 2024-04-25 18:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002'
down_revision = '001'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create tasks table
    op.create_table(
        'tasks',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('due_date', sa.DateTime(), nullable=True),
        sa.Column('completed', sa.Boolean(), default=False),
        sa.Column('completed_at', sa.DateTime(), nullable=True),
        sa.Column('priority', sa.String(), nullable=True),
        sa.Column('category', sa.String(), nullable=True),
        sa.Column('asana_task_id', sa.String(), nullable=True),
        sa.Column('transaction_id', sa.Integer(), nullable=False),
        sa.Column('assigned_to_id', sa.Integer(), nullable=True),
        sa.Column('created_by_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), onupdate=sa.text('now()')),
        sa.ForeignKeyConstraint(['transaction_id'], ['transactions.id'], ),
        sa.ForeignKeyConstraint(['assigned_to_id'], ['users.id'], ),
        sa.ForeignKeyConstraint(['created_by_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tasks_id'), 'tasks', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_tasks_id'), table_name='tasks')
    op.drop_table('tasks') 