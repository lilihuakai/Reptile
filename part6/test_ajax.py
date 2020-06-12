from urllib.parse import urlencode
from pyquery import PyQuery as pq
import requests

base_url = "https://m.weibo.cn/api/container/getIndex?"
headers = {
    'Host': "m.weibo.cn",
    'Referer': "https://m.weibo.cn/u/2830678474",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
    'X-Requested-With': "XMLHttpRequest"
}


def get_page(since_id):
    params = {
        'type': "uid",
        'value': "2830678474",
        'containerid': "1076032830678474",
        'since_id': since_id
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print("Error", e.args)

def get_since_id(json):
    if json:
        since_id = json.get('data').get('cardlistInfo').get('since_id')
        return since_id

def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        since_id = json.get('data').get('cardlistInfo').get('since_id')
        for item in items:
            mblog = item.get('mblog')
            weibo = {}
            weibo['id'] = mblog.get('id')
            weibo['text'] = pq(mblog.get('text')).text()
            weibo['created_at'] = mblog.get('created_at')
            weibo['pic_num'] = mblog.get('pic_num')
            weibo['source'] = mblog.get('source')
            yield weibo

if __name__ == '__main__':
    since_id = None
    for num in range(0, 3):
        json = get_page(since_id)
        since_id = get_since_id(json)
        print(since_id)
        results = parse_page(json)
        for result in results:
            print(result)
