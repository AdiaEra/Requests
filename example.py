# task1
import requests
from pprint import pprint

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
# pprint(response.json())


def the_smartest_hero(hero_list):
    hero_list = ['Hulk', 'Captain America', 'Thanos']
    hero_dict = {}
    for i in response.json():
        if i['name'] in hero_list:
            hero_dict.setdefault(i['name'], i['powerstats']['intelligence'])
    for key, value in hero_dict.items():
        break
    return f'Самый умный супергерой - {max(hero_dict, key=hero_dict.get)} со значением {max(hero_dict.values())}'


print(the_smartest_hero('Hulk, Captain America, Thanos'))

# task2
TOKEN = ''


class YaMyloader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': 'OAuth {}'.format(self.token)
                }

    def get_file_list(self):
        file_list_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(file_list_url, headers=headers)
        return response.json()

    def _link_load_file(self, disk_file_path):
        """получаем ссылку на загрузку файла"""
        link_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(link_url, headers=headers, params=params)
        return response.json()

    def load_file(self, disk_file_path, file_name):
        result = self._link_load_file(disk_file_path=disk_file_path)
        url = result.get('href')
        response = requests.put(url, data=open(file_name, 'rb'))
        response.raise_for_status()
        if response.raise_for_status() == 201:
            print('victory!!!')


if __name__ == '__main__':
    ya = YaMyloader(token=TOKEN)
    ya.load_file(disk_file_path='just7_test.txt', file_name='text_file.txt')
