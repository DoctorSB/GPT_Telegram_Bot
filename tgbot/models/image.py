import openai
from environs import Env
from json_reader import json_reader
from decoder import decoder

class ImageGPT:
    def __init__(self) -> None:
        env = Env()
        env.read_env()
        openai.api_key = env('GPT_API_KEY')

    def img_response(self, task):
        response = openai.Image.create(
            prompt=task,
            n=1,
            size='256x256',
            response_format='b64_json'
        )
        processed_response = json_reader(response)
        processed_response = decoder(processed_response)
        file_name = '_'.join(task.split()) + '.png'
        with open(file_name, 'wb') as file:
            file.write(processed_response)
        return processed_response
    
if __name__ == '__main__':
    gpt = ImageGPT()
    data = input('Введите задачу: ')
    print(gpt.img_response(data))
