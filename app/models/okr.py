import pynecone
from sqlalchemy import ForeignKey, Column, Integer


class Objective(pynecone.Model, table=True):
    __tablename__ = "objective"
    user_id: int = Column(Integer, ForeignKey('auth_user.id'))
    value: str
    order_idx: int


class KeyResult(pynecone.Model, table=True):
    __tablename__ = "key_result"
    objective_id: int = Column(Integer, ForeignKey('objective.id'))
    value: str
    order_idx: int

    archive_percent: float = 0
