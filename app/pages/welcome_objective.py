import typing

import pynecone

from app import Global
from app.components.container import Container
from app.pages.base import BasePage
from app.states.okr import OKRState


class WelcomeObjectiveState(Global.State):
    def prev(self):
        from app.pages.welcome import Welcome

        return pynecone.redirect(Welcome.route)

    def next(self):
        from app.pages.welcome_key_results import WelcomeKeyResults

        return pynecone.redirect(WelcomeKeyResults.route)


class WelcomeObjective(BasePage):
    route = "/welcome-objective"

    def get_component(self) -> pynecone.Component:
        return Container.with_cta(
            pynecone.vstack(
                pynecone.form_control(
                    pynecone.form_label("꼭 이루어 내고 싶은 목표가 있나요?"),
                    pynecone.text_area(
                        default_value=OKRState.objective,
                        on_blur=OKRState.set_objective,
                        variant="filled",
                    ),
                    pynecone.form_helper_text("ex) 올해에는 영어를 유창하게 쓸 수 있도록 공부하기"),
                ),
                align_items="flex-start",
            ),
            display="flex",
            flex_flow="column",
            justify_content="center",
            cta_left=pynecone.button(
                "이전", width="100%", on_click=WelcomeObjectiveState.prev
            ),
            cta_right=pynecone.button(
                "다음", width="100%", on_click=WelcomeObjectiveState.next
            ),
        )
