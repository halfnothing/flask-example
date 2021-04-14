import datetime
import sqlalchemy
from sqlalchemy import sql
from .db_session import SqlAchemyBase
from sqlalchemy_serializer import SerializerMixin


class Work(SqlAchemyBase, SerializerMixin):
    __tablename__ = 'works'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True,
                           autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
