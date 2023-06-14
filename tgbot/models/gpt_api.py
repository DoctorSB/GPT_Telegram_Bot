import openai
from environs import Env
import backoff
import time

@backoff.on_exception(backoff.expo, openai.error.RateLimitError, max_time=30)
def completions_with_backoff(**kwargs):
    try:
        return openai.Completion.create(**kwargs)
    except Exception as e:
        print(f"Error details: {str(e)}")
        raise e

class GPT:
    def __init__(self) -> None:
        env = Env()
        env.read_env()
        openai.api_key = env.str('GPT_API_KEY', parse_mode='HTML')
        self.__message = []

    def request(self, task):
        self.__message.append({'role': 'user', 'content': task})
        print(f'{task}: запрос отправлен')
        try:
            start_time = time.time()
            answer = completions_with_backoff(model="gpt-3.5-turbo", prompt=task)
            end_time = time.time()
            print(f'Request completed in {end_time - start_time} seconds')
            self.__message.append(
                {'role': 'assistant', 'content': answer.choices[0].text})
            return answer.choices[0].text
        except Exception as e:
            print(f"Error encountered: {str(e)}")
            return None

    def clear(self):
        self.__message = []

if __name__ == '__main__':
    gpt = GPT()
    data = input('Введите задачу: ')
    print(gpt.request(data))
