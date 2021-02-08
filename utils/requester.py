import requests


def get_page_json(index):
        data = requests.get(f'https://cdn.hiyobi.me/json/{index}_list.json')
        resp = data.json()
        return resp


class Requester:

    def get_title(self, index):
        data = requests.get(f'https://api.hiyobi.me/gallery/{index}')
        resp = data.json()
        return resp['title']

    def get_page_list(self, index):
        resp = get_page_json(index)
        result = []
        for i in range(len(resp)):
            file = resp[i]['name']
            img = f'https://cdn.hiyobi.me/data/{index}/{file}'
            result.append(img)
        return result

    def get_list(self, page):
        data = requests.get(f'https://api.hiyobi.me/list/{page}')
        resp = data.json()
        return resp
