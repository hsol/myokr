import re
import typing

import pynecone

from app.components.container import Container
from app.models.okr import Objective, KeyResult
from app.pages.base import BasePage
from app.services.auth import auth_service
from app.states.okr import OKRState


class WelcomeNeedLoginState(OKRState):
    email: str

    def set_email(self, v: str):
        self.error_message = ""
        if not re.fullmatch(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', v
        ):
            self.error_message = "이메일을 정확히 입력해주세요."
        else:
            session_user = auth_service.get_session_user(v)
            self.session.user_id = session_user.id

        self.email = v

    def on_email_blur(self, v: str):
        if re.fullmatch(
            r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', v
        ):
            session_user = auth_service.get_session_user(v)
            self.session.user_id = session_user.id

    def on_load(self):
        if not self.objective:
            self.error_message = "목표가 설정되지 않았어요. 이전으로 돌아가서 다시 목표를 입력해주세요!"
            return

        if not self.key_results:
            self.error_message = "KR 이 입력되지 않았어요. 이전으로 돌아가서 다시 목표부터 입력해주세요!"
            return

    def go_to_set_objective(self):
        from app.pages.welcome_objective import WelcomeObjective

        return pynecone.redirect(WelcomeObjective.route)

    def login(self):
        from app.pages.welcome_save_complete import WelcomeSaveComplete

        return pynecone.redirect(WelcomeSaveComplete.route)


class WelcomeNeedLogin(BasePage):
    route = "/welcome-login"

    def get_on_load_event_handler(self) -> typing.Callable[[], None] | None:
        return WelcomeNeedLoginState.on_load

    def get_component(self) -> pynecone.Component:
        def key_result_componenet(key_result: str, order: int):
            return pynecone.text(str(order) + ". " + key_result)

        return Container.with_cta(
            pynecone.vstack(
                pynecone.cond(
                    WelcomeNeedLoginState.objective,
                    pynecone.vstack(
                        pynecone.heading(
                            '"' + WelcomeNeedLoginState.objective + '"', size="md"
                        ),
                        pynecone.divider(border_color="black"),
                        pynecone.cond(
                            WelcomeNeedLoginState.kr1,
                            key_result_componenet(WelcomeNeedLoginState.kr1, 1),
                            pynecone.box(),
                        ),
                        pynecone.cond(
                            WelcomeNeedLoginState.kr2,
                            key_result_componenet(WelcomeNeedLoginState.kr2, 2),
                            pynecone.box(),
                        ),
                        pynecone.cond(
                            WelcomeNeedLoginState.kr3,
                            key_result_componenet(WelcomeNeedLoginState.kr3, 3),
                            pynecone.box(),
                        ),
                        pynecone.cond(
                            WelcomeNeedLoginState.kr4,
                            key_result_componenet(WelcomeNeedLoginState.kr4, 4),
                            pynecone.box(),
                        ),
                        pynecone.cond(
                            WelcomeNeedLoginState.kr5,
                            key_result_componenet(WelcomeNeedLoginState.kr5, 5),
                            pynecone.box(),
                        ),
                        *([pynecone.spacer()] * 3),
                        pynecone.input(
                            placeholder="example@gmail.com",
                            value=WelcomeNeedLoginState.email,
                            on_change=WelcomeNeedLoginState.set_email,
                            on_blur=WelcomeNeedLoginState.on_email_blur,
                        ),
                        align_items="flex-start",
                        width="100%",
                    ),
                ),
                pynecone.alert(
                    pynecone.alert_icon(),
                    pynecone.alert_title(
                        pynecone.cond(
                            WelcomeNeedLoginState.error_message,
                            WelcomeNeedLoginState.error_message,
                            "거의 다 되었어요. 이메일로 로그인 후 확인 해보시겠어요?",
                        )
                    ),
                    status=pynecone.cond(
                        WelcomeNeedLoginState.error_message, "error", "info"
                    ),
                ),
                align_items="flex-start",
            ),
            display="flex",
            flex_flow="column",
            justify_content="center",
            cta_left=pynecone.cond(
                WelcomeNeedLoginState.error_message,
                pynecone.button(
                    "목표 설정하기",
                    width="100%",
                    on_click=WelcomeNeedLoginState.go_to_set_objective,
                ),
                pynecone.button(
                    "로그인", width="100%", on_click=WelcomeNeedLoginState.login
                ),
            ),
        )
