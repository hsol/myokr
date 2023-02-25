import pynecone
from app import Global
from app.pages import get_route_pages, BasePage

app = pynecone.App(
    state=Global.State,
    stylesheets=Global.STYLE_SHEETS,
    style=Global.STYLE,
)
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
