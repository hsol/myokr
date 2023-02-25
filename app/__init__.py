import pynecone


class Global:
    class State(pynecone.State):
        def on_load(self):
            print("why")

    class FontFamily:
        DEFAULT = "'Noto Sans KR', sans-serif;"
        LOGO = "'Overlock', cursive"

    STYLE_SHEETS = [
        "https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400&display=swap",
        "https://fonts.googleapis.com/css2?family=Overlock:ital,wght@1,900&display=swap",
    ]
    STYLE = {
        "font_family": FontFamily.DEFAULT,
    }
