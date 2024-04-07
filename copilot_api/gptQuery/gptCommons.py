from openai import OpenAI
from .license import OPENAI_TOKEN


class GPTQuery:
    OPENAI_API_KEY = OPENAI_TOKEN
    CLIENT = OpenAI(api_key=OPENAI_API_KEY)
    PROMPT = None

    def __init__(self, system_prompt, tokens=2000, temperature=1):
        self._system_prompt = system_prompt
        self._result = None
        self._max_tokens = tokens
        self._temperature = temperature

    def process(self, query):
        try:
            completion = self.CLIENT.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self._system_prompt},
                    {"role": "user", "content": query},
                ],
                max_tokens=self._max_tokens,
                temperature=self._temperature
            )
            self._result = completion.choices[0].message.content
        except Exception as e:
            raise Exception(f'GPTQuery Error: {str(e)}')

    def get_result(self):
        return self._result
