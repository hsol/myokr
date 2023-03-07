import pynecone

from app import Global, Session


class SessionMiddleware(pynecone.Middleware):
    def preprocess(self, app: pynecone.App, state: Global.State, event):
        if state.session is None:
            state.session = Session(
                token=event.router_data["token"], ip=event.router_data["ip"]
            )

    def postprocess(self, app: pynecone.App, state: Global.State, event, delta):
        pass
        # print(f"Delta {delta}")
