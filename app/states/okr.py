import pynecone

from app import Global


class TooManyKeyResultsError(Exception):
    def __str__(self):
        return "최대 5개까지 Key Result 를 생성할 수 있습니다."


class OKRState(Global.State):
    objective: str = ""
    error_message: str = ""

    kr1: str | None = None
    kr2: str | None = None
    kr3: str | None = None
    kr4: str | None = None
    kr5: str | None = None

    def set_key_result_1(self, v: str):
        self.kr1 = v

    def set_key_result_2(self, v: str):
        self.kr2 = v

    def set_key_result_3(self, v: str):
        self.kr3 = v

    def set_key_result_4(self, v: str):
        self.kr4 = v

    def set_key_result_5(self, v: str):
        self.kr5 = v

    @pynecone.var
    def key_results(self) -> list[str]:
        return list(
            filter(
                lambda i: i is not None,
                [
                    self.kr1,
                    self.kr2,
                    self.kr3,
                    self.kr4,
                    self.kr5,
                ],
            )
        )

    def clear_key_results(self):
        [
            self.kr1,
            self.kr2,
            self.kr3,
            self.kr4,
            self.kr5,
        ] = [None] * 5

    @pynecone.var
    def has_key_results(self) -> bool:
        return len(list(self.key_results)) > 0
