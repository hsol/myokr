import pynecone
from app import Global
from app.pages.base import BasePage
from app.pages.index import Index
from app.pages.welcome import Welcome

app = pynecone.App(
    state=Global.State,
    stylesheets=Global.STYLE_SHEETS,
    style=Global.STYLE,
)


def get_route_pages() -> list[str, type[BasePage]]:
    pages = [Index, Welcome]
    return {
        page.route: page
        for page in pages
    }.items()

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
