import pynecone
from pynecone.event import EventHandler


class BasePage:
    def get_component(self) -> pynecone.Component:
        raise NotImplementedError

    def get_add_page_options(self) -> dict:
        return {}

    def get_on_load_event_handler(self) -> EventHandler | None:
        return None
