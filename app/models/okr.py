import pynecone


class Objective(pynecone.Model, table=True):
    user_id: int
    value: str
    order_idx: int


class KeyResult(pynecone.Model, table=True):
    objective_id: int
    value: str
    order_idx: int

    archive_percent: float
