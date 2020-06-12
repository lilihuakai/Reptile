from urllib.parse import urlencode
from multiprocessing.pool import Pool
import requests
import time

GROUP_START = 1
GROUP_END = 5
base_url = "https://www.toutiao.com/api/search/content/?"
headers = {
    'Host': "www.toutiao.com",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
    'X-Requested-With': "XMLHttpRequest"
}

def get_page(offset):
    params = {
        'aid': 24,
        'app_name': 'web_search',
        'offset': 0,
        'format': 'json',
        'keyword': "街拍",
        'autoload': 'true',
        'count': 20,
        'en_qc': 1,
        'cur_tab': 1,
        'from': 'search_tab',
        'pd': 'synthesis',
        'timestamp': str(int(time.time()))
        # '_signature'
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except response.ConnectionError:
        return None

def get_images(json):
    print('123')
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            share_url = item.get('share_url')
            yield {
                'title': title,
                'share_url': share_url
            }

def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
