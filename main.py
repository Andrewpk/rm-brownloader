import os

import requests

if __name__ == '__main__':
    config_url = 'https://rm-brown-soudboard.s3.amazonaws.com/config.json'
    config = requests.get(config_url).json()

    base_mp3_url = 'https://rm-brown-soudboard.s3.amazonaws.com/'
    for sound in config:
        download_url = base_mp3_url + sound['name'] + '.mp3'
        filename = os.path.join(os.getcwd(), 'mp3s', sound['name'])
        filename = filename + '.mp3'
        with open(filename, 'wb') as file:
            file.write(requests.get(download_url).content)
        print(f'{sound["name"]} downloaded')
