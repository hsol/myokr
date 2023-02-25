from app.pages.base import BasePage
from app.pages.index import Index
from app.pages.welcome import Welcome


def get_route_pages() -> list[str, type[BasePage]]:
    return {
        "/": Index,
        "/welcome": Welcome,
    }.items()
