import re

from app.constants import AppConstants
from utils.gpt import ChatGPT


class KeyResultProvideFailedError(Exception):
    pass


class OKRChatGPT(ChatGPT):
    def __init__(self):
        super().__init__(
            key=AppConstants.GPT_API_KEY,
            model="gpt-3.5-turbo",
            concepts={
                "base_concept": "너는 OKR 모델을 기반으로 목표를 입력받아 Key Result 를 출력하는 개인 비서야.",
                "should_do": "나는 너에게 목표를 제시할것이고, 너는 Key Result 를 최소 3개까지 제시 해야만해.",
                "react_format": "반드시 이 모양으로만 대답해줘:\n\n- KR1: 첫번째 예시 데이터\n- KR2: 두번째 예시 데이터\n- KR3: 세번째 예시 데이터",
            },
        )

    def get_key_results(self, objective: str) -> list[str]:
        answer = self.query(content=f'"{objective}" 를 목표로 설정했을 때 Key Result 를 제시해줘')
        key_results = re.findall(r"- KR[\d*]: (.*)", answer)
        if len(key_results) == 0:
            raise KeyResultProvideFailedError(answer)

        return key_results
