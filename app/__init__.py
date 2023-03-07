import pynecone

from app.models.auth import AuthUser
from app.okr_gpt import OKRChatGPT


class Session(pynecone.Base):
    user_id: int | None
    token: str

    ip: str
    storage: dict = {}

    @pynecone.var
    def user(self):
        if self.user_id is None:
            return None

        with pynecone.session() as s:
            return (
                s.query(AuthUser).filter(AuthUser.id.__eq__(self.user_id)).one_or_none()
            )


class Global:
    class State(pynecone.State):
        session: Session | None

        def get_session_user(self, email: str):
            with pynecone.session() as s:
                session_user = (
                    s.query(AuthUser).filter(AuthUser.email.__eq__(email)).one_or_none()
                )
                if session_user is None:
                    session_user = AuthUser(email=email)
                    s.add(session_user)
                s.commit()

            return session_user

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
