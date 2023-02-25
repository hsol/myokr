import pynecone

from app import Global
from app.pages.base import BasePage


class Welcome(BasePage):
    def get_component(self) -> pynecone.Component:
        return pynecone.container(
            pynecone.vstack(
                pynecone.text("내 목표를 향해서"),
                pynecone.heading(
                    "my-o.kr",
                    size="4xl",
                    font_family=Global.FontFamily.LOGO,
                ),
                height="30vh",
                display="flex",
                flex_flow="column",
                align_items="center",
                justify_content="center",
            ),
            center_content=True,
            display="flex",
            flex_flow="column",
            align_items="center",
            justify_content="center",
            height="100vh",
        )
