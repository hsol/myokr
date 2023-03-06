import asyncio
import typing

from app.constants import AppConstants

if typing.TYPE_CHECKING:
    import openai


class ChatGPT:
    model_name: str
    model_system_concepts: dict = {}
    module: "openai"

    def __init__(self, key: str, model: str, concepts: dict[str, str] = None):
        import openai

        self.model_name = model
        for k, v in concepts.items():
            self.add_concept(k, v)
        self.module = openai
        self.module.api_key = key

    def add_concept(self, key: str, concept: str):
        self.model_system_concepts[key] = concept

    def remove_concept(self, key: str):
        try:
            del self.model_system_concepts[key]
        except KeyError:
            pass

    def get_concept_messages(self, concepts: typing.Iterable):
        return [{"role": "system", "content": concept} for concept in concepts]

    def get_assistants_messages(self, assistants: typing.Iterable):
        return [{"role": "assistant", "content": assistant} for assistant in assistants]

    def query(self, content: str, assistants: list[str] = None):
        messages = [
            *self.get_concept_messages(self.model_system_concepts.values()),
            *(self.get_assistants_messages(assistants) if assistants else []),
        ]
        response = self.module.ChatCompletion.create(
            model=self.model_name,
            messages=[*messages, {"role": "user", "content": content}],
        )

        return "\n".join(choice["message"]["content"] for choice in response["choices"])
