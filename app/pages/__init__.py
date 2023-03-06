import os

from app.pages.base import BasePage
from utils import import_all_sub_classes

__all__ = import_all_sub_classes(os.path.dirname(__file__), BasePage)
