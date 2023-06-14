from base64 import b64decode

def decoder(response):
    image = b64decode(response['data'][0]['b64_json'])
    return image