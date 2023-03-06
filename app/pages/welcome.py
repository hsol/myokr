import pynecone

from app import Global
from app.components.container import Container
from app.components.logo import Logo
from app.pages.base import BasePage


class WelcomeState(Global.State):
    def next(self):
        from app.pages.welcome_objective import WelcomeObjective

        return pynecone.redirect(WelcomeObjective.route)


class Welcome(BasePage):
    route = "/welcome"

    def get_component(self) -> pynecone.Component:
        return Container.with_cta(
            pynecone.vstack(
                Logo.inline,
                *([pynecone.spacer()] * 3),
                pynecone.markdown(
                    "OKR(Objectives and key results)은 **목표**와 결과를 **정의**하고 **추적**하기 위한 목표설정 모델입니다."
                ),
                pynecone.spacer(),
                pynecone.markdown(
                    "여러분의 **목표**에도 OKR 모델을 적용하여 내가 스스로 얼마나 잘 해내고 있는지 진척도를 체크해보세요!"
                ),
                align_items="flex-start",
            ),
            display="flex",
            flex_flow="column",
            justify_content="center",
            cta_right=pynecone.button("다음", width="100%", on_click=WelcomeState.next),
        )
