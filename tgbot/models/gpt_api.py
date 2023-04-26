import openai
from environs import Env


class GPT:
    def __init__(self) -> None:
        env = Env()
        env.read_env()
        openai.api_key = env.str('GPT_API_KEY', parse_mode='HTML')
        self.__message = []

    def request(self, task):
        self.__message.append({'role': 'user', 'content': task})
        print(f'{task}: запрос отправлен')
        answer = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=self.__message
        )
        self.__message.append(
            {'role': 'bot', 'content': answer.choices[0].message.content})
        return answer.choices[0].message.content


if __name__ == '__main__':
    gpt = GPT()
    data = input('Введите задачу: ')
    print(gpt.request(data))