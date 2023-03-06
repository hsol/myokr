import pynecone

from app import Global
from app.components.container import Container
from app.components.logo import Logo
from app.pages.base import BasePage


class IndexState(Global.State):
    def redirect(self):
        from app.pages.welcome import Welcome

        return pynecone.redirect(Welcome.route)


class Index(BasePage):
    route = "/"

    def get_component(self) -> pynecone.Component:
        return Container.wrapper(
            pynecone.flex(
                pynecone.vstack(
                    pynecone.flex(Logo.big, height="20vh", align="center"),
                    pynecone.spacer(),
                    pynecone.button(
                        "시작하기",
                        bg=Global.Palette.MANTIS,
                        color="black",
                        size="lg",
                        on_click=IndexState.redirect,
                    ),
                ),
                direction="column",
                align="center",
                justify="center",
                height="100%",
            ),
            height="100vh",
        )
