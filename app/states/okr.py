import typing
from functools import partial

import pynecone
from pynecone import EventChain
from pynecone.event import EventHandler

from app import Global


class KeyResult(pynecone.Base):
    index: int
    value: str

    def json(self):
        return self.value


class OKRState(Global.State):
    objective: str = ""
    key_results: list[KeyResult] = []
    error_message: str = ""

    def set_key_result(self, index: int, v: str):
        print(index)

    @pynecone.var
    def has_key_results(self) -> bool:
        return len(list(self.key_results)) > 0
