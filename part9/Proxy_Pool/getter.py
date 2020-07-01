import requests
from pyquery import PyQuery as pq
from mydb import RedisClient


POOL_UPPER_THRESHOLD = 10000

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"
}


# 元类
class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for key, value in attrs.items():
            if 'crawl_' in key:
                attrs['__CrawlFunc__'].append(key)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return super(ProxyMetaclass, cls).__new__(cls, name, bases, attrs)
        # return type.__new__(cls, name, bases, attrs)


def get_page(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.ConnectionError as e:
        print("Error", e.args)

class Crawler(object, metaclass=ProxyMetaclass):
    """docstring for Crawler"""
    def __init__(self):
        pass

    def get_proxies(self, callback):
        """
        获取批量代理
        return: 批量代理
        """
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            print("成功获取到代理", proxy)
            proxies.append(proxy)
        return proxies

    def crawl_daili66(self, page_count=4):
        """
        获取代理66
        param page_count: 页码
        return: 代理
        """
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print("Crawling", url)
            html = get_page(url)
            if html:
                doc = pq(html)
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])

    def crawl_proxy360(self):
        """
        获取Proxy360
        return: 代理
        """
        url = 'http://www.goubanjia.com'
        html = get_page(url)
        if html:
            doc = pq(html)
            tds = doc('td.ip').items()
            for td in tds:
                td.find('p').remove()
                yield td.text().replace('\n', '')


# if __name__ == '__main__':
#     crawler = Crawler()
#     # results = crawler.crawl_daili66()
#     results = crawler.crawl_proxy360()
#     for result in results:
#         print(result)


class Getter(object):
    """docstring for Getter"""
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()

    def is_over_threshold(self):
        """
        判断是否达到了代理池限制
        return: 判断结果
        """
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        print("获取器开始执行")
        if not self.is_over_threshold():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_label]
                proxies = self.crawler.get_proxies(callback)
                for proxy in proxies:
                    pass
                    self.redis.add(proxy)



if __name__ == '__main__':
    getter = Getter()
    getter.run()
