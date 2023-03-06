import pynecone

from app.okr_gpt import OKRChatGPT


class Global:
    class State(pynecone.State):
        def on_load(self):
            print("why")

    class FontFamily:
        DEFAULT = "'Noto Sans KR', sans-serif;"
        LOGO = "'Tilt Neon', cursive"

    class Palette:
        WHITE = "#FFFFFF"
        CINDER = "#030305"
        BIRCH = "#F2F4EF"
        RONCHI = "#EFB730"
        CLEARDAY = "#CEE3F4"
        VERMILLON = "#C94F44"
        RAISIN = "#261326"
        MANTIS = "#ABBF4E"

    STYLE_SHEETS = [
        "/base.css",
        "https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400&display=swap",
        "https://fonts.googleapis.com/css2?family=Tilt+Neon&display=swap",
    ]
    STYLE = {
        "font_family": FontFamily.DEFAULT,
        "color": Palette.CINDER,
        "box_sizing": "border-box",
    }
    GPT = OKRChatGPT()
