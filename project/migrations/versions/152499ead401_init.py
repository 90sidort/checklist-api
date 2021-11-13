"""init

Revision ID: 152499ead401
Revises: 
Create Date: 2021-11-13 00:04:49.780476

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '152499ead401'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('album',
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('creator', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('genre', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_album_creator'), 'album', ['creator'], unique=False)
    op.create_index(op.f('ix_album_genre'), 'album', ['genre'], unique=False)
    op.create_index(op.f('ix_album_id'), 'album', ['id'], unique=False)
    op.create_index(op.f('ix_album_title'), 'album', ['title'], unique=False)
    op.create_table('book',
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('creator', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('genre', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_creator'), 'book', ['creator'], unique=False)
    op.create_index(op.f('ix_book_genre'), 'book', ['genre'], unique=False)
    op.create_index(op.f('ix_book_id'), 'book', ['id'], unique=False)
    op.create_index(op.f('ix_book_title'), 'book', ['title'], unique=False)
    op.create_table('movie',
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('creator', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('genre', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_movie_creator'), 'movie', ['creator'], unique=False)
    op.create_index(op.f('ix_movie_genre'), 'movie', ['genre'], unique=False)
    op.create_index(op.f('ix_movie_id'), 'movie', ['id'], unique=False)
    op.create_index(op.f('ix_movie_title'), 'movie', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_movie_title'), table_name='movie')
    op.drop_index(op.f('ix_movie_id'), table_name='movie')
    op.drop_index(op.f('ix_movie_genre'), table_name='movie')
    op.drop_index(op.f('ix_movie_creator'), table_name='movie')
    op.drop_table('movie')
    op.drop_index(op.f('ix_book_title'), table_name='book')
    op.drop_index(op.f('ix_book_id'), table_name='book')
    op.drop_index(op.f('ix_book_genre'), table_name='book')
    op.drop_index(op.f('ix_book_creator'), table_name='book')
    op.drop_table('book')
    op.drop_index(op.f('ix_album_title'), table_name='album')
    op.drop_index(op.f('ix_album_id'), table_name='album')
    op.drop_index(op.f('ix_album_genre'), table_name='album')
    op.drop_index(op.f('ix_album_creator'), table_name='album')
    op.drop_table('album')
    # ### end Alembic commands ###