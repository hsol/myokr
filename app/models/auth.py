from datetime import datetime

import pynecone
from sqlalchemy import Column, Integer, ForeignKey


class AuthUser(pynecone.Model, table=True):
    __tablename__ = "auth_user"
    email: str


class AuthUserAccessLog(pynecone.Model, table=True):
    user_id: int = Column(Integer, ForeignKey('auth_user.id'))
    token: str
    ip: str

    reg_datetime: datetime
