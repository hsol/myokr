from datetime import datetime

import pynecone

from app import Global, Session
from app.models.auth import AuthUserAccessLog, AuthUser


class SessionMiddleware(pynecone.Middleware):
    def preprocess(self, app: pynecone.App, state: Global.State, event):
        if state.session is None:
            state.session = Session(
                token=event.router_data["token"], ip=event.router_data["ip"]
            )

        with pynecone.session() as s:
            if state.session.user_id is None:
                if (
                    token_user_log := s.query(AuthUserAccessLog)
                    .filter(AuthUserAccessLog.token.__eq__(state.session.token))
                    .one_or_none()
                ):
                    state.session.user_id = token_user_log.user_id

            if state.session.user_id is not None:
                s.add(
                    AuthUserAccessLog(
                        user_id=state.session.user_id,
                        token=state.session.token,
                        ip=state.session.ip,
                        reg_datetime=datetime.now(),
                    )
                )

            s.commit()

    def postprocess(self, app: pynecone.App, state: Global.State, event, delta):
        pass
        # print(f"Delta {delta}")
