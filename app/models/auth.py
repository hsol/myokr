import pynecone


class User(pynecone.Model, table=True):
    email: str
