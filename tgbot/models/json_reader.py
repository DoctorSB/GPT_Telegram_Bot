import json

def json_reader(response):
    with open('data.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

