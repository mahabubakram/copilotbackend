from openai import OpenAI
from .license import OPENAI_TOKEN


class GPTQuery:
    OPENAI_API_KEY = OPENAI_TOKEN
    CLIENT = OpenAI(api_key=OPENAI_API_KEY)
    PROMPT = None

    def __init__(self, system_prompt, user_prompt):
        self._system_prompt = system_prompt
        self._user_prompt = user_prompt
        self._result = None
        self.generate()

    def generate(self):
        completion = self.CLIENT.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self._system_prompt},
                {"role": "user", "content": self._user_prompt},
            ],
        )
        self._result = completion.choices[0].message.content

    def get_result(self):
        return self._result
