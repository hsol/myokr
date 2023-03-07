import inspect
import json
import typing
from functools import partial

import pynecone
from pynecone.event import EventHandler, EventChain
from pynecone.utils import call_event_fn
from pynecone.var import BaseVar

from app import Global
from app.components.container import Container
from app.okr_gpt import KeyResultProvideFailedError
from app.pages.base import BasePage
from app.states.okr import OKRState


class WelcomeKeyResultsState(OKRState):
    def on_load(self):
        if self.objective:
            self.error_message = ""
            try:
                key_result_strings = Global.GPT.get_key_results(self.objective)
            except KeyResultProvideFailedError as e:
                self.error_message = str(e)
                return

            self.set_key_results(key_result_strings)
        else:
            self.error_message = "목표가 설정되지 않았어요. 이전으로 돌아가서 다시 목표를 입력해주세요!"

    def prev(self):
        from app.pages.welcome_objective import WelcomeObjective

        return pynecone.redirect(WelcomeObjective.route)

    def next(self):
        from app.pages.welcome import Welcome

        return pynecone.redirect(Welcome.route)

    def partial_set_key_results(self, index):
        events = call_event_fn(self.set_key_result, index)
        # Return the event chain.
        return EventChain(events=events)


class WelcomeKeyResults(BasePage):
    route = "/welcome-key-results"

    def get_on_load_event_handler(self) -> typing.Callable[[], None] | None:
        return WelcomeKeyResultsState.on_load

    def get_component(self) -> pynecone.Component:
        def key_result_input(key_result: str, index: int):
            return pynecone.form_control(
                pynecone.form_label(f"Key Result {index}"),
                pynecone.text_area(
                    default_value=key_result,
                    on_blur=getattr(
                        WelcomeKeyResultsState, f"set_key_result_{index+1}"
                    ),
                ),
                width="100%",
            )

        return Container.with_cta(
            pynecone.vstack(
                pynecone.cond(
                    WelcomeKeyResultsState.has_key_results,
                    pynecone.vstack(
                        pynecone.code_block(
                            "목표: " + WelcomeKeyResultsState.objective,
                        ),
                        pynecone.text("위 목표에 대해 Key-Result 들을 생각해봤어요."),
                        pynecone.spacer(),
                        *(
                            [
                                key_result_input(key_result=key_result, index=0)
                                for key_result in WelcomeKeyResultsState.key_results
                            ]
                        ),
                        *([pynecone.spacer()] * 3),
                        pynecone.text("어때요? 제시된 Key-Result 들이 마음에 드시나요?"),
                        pynecone.text("마음에 들지 않는다면, 입맛에 맞도록 직접 수정 해보세요."),
                        align_items="flex-start",
                        width="100%",
                    ),
                    pynecone.cond(
                        WelcomeKeyResultsState.error_message,
                        pynecone.vstack(
                            pynecone.alert(
                                pynecone.alert_icon(),
                                pynecone.alert_title(
                                    WelcomeKeyResultsState.error_message
                                ),
                                status="error",
                            ),
                            width="100%",
                            align_items="center",
                        ),
                        pynecone.vstack(
                            pynecone.circular_progress(is_indeterminate=True),
                            pynecone.text("멋진 아이디어를 생각해내는 중이에요."),
                            width="100%",
                            align_items="center",
                        ),
                    ),
                ),
                align_items="flex-start",
            ),
            display="flex",
            flex_flow="column",
            justify_content="center",
            cta_left=pynecone.button(
                "목표 다시 설정", width="100%", on_click=WelcomeKeyResultsState.prev
            ),
            cta_right=pynecone.cond(
                WelcomeKeyResultsState.has_key_results
                and not WelcomeKeyResultsState.error_message,
                pynecone.button(
                    "저장", width="100%", on_click=WelcomeKeyResultsState.next
                ),
                pynecone.box(),
            ),
        )
