import pynecone
from app.pages.base import BasePage

class State(pynecone.State):
    def on_load(self):
        print("fuck")

class Index(BasePage):
    def get_component(self) -> pynecone.Component:
        return pynecone.container()

    def get_on_load_event_handler(self) -> callable:
        return State.on_load
