import os

import pynecone
from app import Global
from app.middlewares.session import SessionMiddleware
from app.pages.base import BasePage
from app import pages

app = pynecone.App(
    state=Global.State,
    stylesheets=Global.STYLE_SHEETS,
    style=Global.STYLE,
    middleware=[SessionMiddleware()],
    api_url=os.environ.get("API_URL"),
)


def get_route_pages() -> list[str, type[BasePage]]:
    return {page.route: page for page in pages.__all__}.items()


for route, page in get_route_pages():
    instance: BasePage = page()
    app.add_page(
        instance.get_component(),
        **{
            **instance.get_add_page_options(),
            "route": route,
            "on_load": instance.get_on_load_event_handler(),
        },
    )

app.compile()
