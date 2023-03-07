import typing

import pynecone

from app.components.container import Container
from app.pages.base import BasePage
from app.states.okr import OKRState


class WelcomeSaveCompleteState(OKRState):
    def on_load(self):
        if not self.objective:
            self.error_message = "목표가 설정되지 않았어요. 이전으로 돌아가서 다시 목표를 입력해주세요!"

        if not self.key_results:
            self.error_message = "KR 이 입력되지 않았어요. 이전으로 돌아가서 다시 목표부터 입력해주세요!"

    def go_to_set_objective(self):
        from app.pages.welcome_objective import WelcomeObjective

        return pynecone.redirect(WelcomeObjective.route)

    def go_home(self):
        from app.pages.welcome_objective import WelcomeObjective

        return pynecone.redirect(WelcomeObjective.route)


class WelcomeSaveComplete(BasePage):
    route = "/welcome-done"

    def get_on_load_event_handler(self) -> typing.Callable[[], None] | None:
        return WelcomeSaveCompleteState.on_load

    def get_component(self) -> pynecone.Component:
        def key_result_componenet(key_result: str, order: int):
            return pynecone.text(str(order) + ". " + key_result)

        return Container.with_cta(
            pynecone.vstack(
                pynecone.cond(
                    WelcomeSaveCompleteState.error_message,
                    pynecone.vstack(
                        pynecone.alert(
                            pynecone.alert_icon(),
                            pynecone.alert_title(
                                WelcomeSaveCompleteState.error_message
                            ),
                            status="error",
                        ),
                        width="100%",
                        align_items="center",
                    ),
                    pynecone.vstack(
                        pynecone.text("OKR 을 저장했어요!"),
                        *([pynecone.spacer()] * 3),
                        pynecone.heading('"' + WelcomeSaveCompleteState.objective + '"', size="md"),
                        pynecone.divider(border_color="black"),
                        pynecone.cond(
                            WelcomeSaveCompleteState.kr1,
                            key_result_componenet(WelcomeSaveCompleteState.kr1, 1),
                            pynecone.box(),
                        ),
                        pynecone.cond(
                            WelcomeSaveCompleteState.kr2,
                            key_result_componenet(WelcomeSaveCompleteState.kr2, 2),
                            pynecone.box(),
                        ),
                        pynecone.cond(
                            WelcomeSaveCompleteState.kr3,
                            key_result_componenet(WelcomeSaveCompleteState.kr3, 3),
                            pynecone.box(),
                        ),
                        pynecone.cond(
                            WelcomeSaveCompleteState.kr4,
                            key_result_componenet(WelcomeSaveCompleteState.kr4, 4),
                            pynecone.box(),
                        ),
                        pynecone.cond(
                            WelcomeSaveCompleteState.kr5,
                            key_result_componenet(WelcomeSaveCompleteState.kr5, 5),
                            pynecone.box(),
                        ),
                        *([pynecone.spacer()] * 3),
                        pynecone.text("이제 저장한 OKR 을 언제든 재방문하고, 얼마나 진행되고 있는지 체크하면서 차근차근 목표를 향해 달려봐요!"),
                        align_items="flex-start",
                        width="100%",
                    ),
                ),
                align_items="flex-start",
            ),
            display="flex",
            flex_flow="column",
            justify_content="center",
            cta_left=pynecone.cond(
                WelcomeSaveCompleteState.error_message,
                pynecone.button(
                    "목표 다시 설정", width="100%", on_click=WelcomeSaveCompleteState.go_to_set_objective
                ),
                pynecone.button(
                    "시작하기", width="100%", on_click=WelcomeSaveCompleteState.go_home
                ),
            ),
        )
