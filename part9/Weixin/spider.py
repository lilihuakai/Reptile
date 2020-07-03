import requests
from pyquery import PyQuery as pq
from requests import ReadTimeout, ConnectionError
from requests import Session
from urllib.parse import urlencode
# My
from config import *
from my_request import WeiXinRequest
from mydb import RedisQueue


class Spider(object):
    """docstring for Spider"""
    base_url = 'http://weixin.sogou.com/weixin'
    keyword = 'NBA'
    headers = {
        'Host': 'weixin.sogou.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'X-Requested-With': 'XMLHttpRequest',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'http://weixin.sogou.com/weixin?query=NBA&type=2',
        'Cookie': 'ABTEST=0|1593654502|v1; IPLOC=CN4403; SUID=8D4D8D3D771A910A000000005EFD3CE6; SUID=8D4D8D3D2F20910A000000005EFD3CE7; weixinIndexVisited=1; SUV=003B13D03D8D4D8D5EFD3CE85ACCE549; sct=3; SNUID=E23DFD526F6AD903BB1F479170BA626F; JSESSIONID=aaaUKqg7p6RlKeuAm-imx; PHPSESSID=pi9rlinmetrj5tl5qksqvjokg3'
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        # 'Accept-Encoding': 'gzip, deflate',
        # 'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,mt;q=0.2',
        # 'Cache-Control': 'max-age=0',
        # 'Connection': 'keep-alive',
        # 'Cookie': 'IPLOC=CN1100; SUID=6FEDCF3C541C940A000000005968CF55; SUV=1500041046435211; ABTEST=0|1500041048|v1; SNUID=CEA85AE02A2F7E6EAFF9C1FE2ABEBE6F; weixinIndexVisited=1; JSESSIONID=aaar_m7LEIW-jg_gikPZv; ld=Wkllllllll2BzGMVlllllVOo8cUlllll5G@HbZllll9lllllRklll5@@@@@@@@@@; LSTMV=212%2C350; LCLKINT=4650; ppinf=5|1500042908|1501252508|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo1NDolRTUlQjQlOTQlRTUlQkElODYlRTYlODklOEQlRTQlQjglQTglRTklOUQlOTklRTglQTclODV8Y3J0OjEwOjE1MDAwNDI5MDh8cmVmbmljazo1NDolRTUlQjQlOTQlRTUlQkElODYlRTYlODklOEQlRTQlQjglQTglRTklOUQlOTklRTglQTclODV8dXNlcmlkOjQ0Om85dDJsdUJfZWVYOGRqSjRKN0xhNlBta0RJODRAd2VpeGluLnNvaHUuY29tfA; pprdig=ppyIobo4mP_ZElYXXmRTeo2q9iFgeoQ87PshihQfB2nvgsCz4FdOf-kirUuntLHKTQbgRuXdwQWT6qW-CY_ax5VDgDEdeZR7I2eIDprve43ou5ZvR0tDBlqrPNJvC0yGhQ2dZI3RqOQ3y1VialHsFnmTiHTv7TWxjliTSZJI_Bc; sgid=27-27790591-AVlo1pzPiad6EVQdGDbmwnvM; PHPSESSID=mkp3erf0uqe9ugjg8os7v1e957; SUIR=CEA85AE02A2F7E6EAFF9C1FE2ABEBE6F; sct=11; ppmdig=1500046378000000b7527c423df68abb627d67a0666fdcee; successCount=1|Fri, 14 Jul 2017 15:38:07 GMT',
        # 'Host': 'weixin.sogou.com',
        # 'Upgrade-Insecure-Requests': '1',
        # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
    session = Session()
    queue = RedisQueue()
    # mysql = MySQL()
    # def __init__(self):
    #     self.base_url = "http://weixin.sogou.com/weixin"
    #     self.keyword = "NBA"
    #     self.queue = RedisQueue()
    #     self.session = Session()
    #     self.headers = {
    #         'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"
    #     }

    def get_proxy(self):
        """
        从代理池获取代理
        return: 代理
        """
        try:
            response = requests.get(PROXY_POOL_URL)
            if response.status_code == 200:
                print("Get Proxy", response.text)
                return response.text
            return None
        except Exception as e:
            print(e.args)
            return None

    def parse_detail(self, response):
        """
        解析详情页
        param response: 响应
        return: 微信公众号文章
        """
        doc = pq(response.text)
        data = {
            'title': doc('.rich_media_title').text(),
            'content': doc('.rich_media_content').text(),
            'date': doc('#post-date').text(),
            'nickname': doc('#js_profile_qrcode > div > strong').text(),
            'wechat': doc('#js_profile_qrcode > div > p:nth-child(3) > span').text(),
        }
        yield data

    def parse_index(self, response):
        """
        解析索引页
        param response: 响应
        return: 新的响应
        """
        doc = pq(response.text)
        items = doc('.news-box .news-list li .txt-box h3 a').items()
        for item in items:
            url = "http://weixin.sogou.com" + item.attr('href')
            weixin_request = WeiXinRequest(url=url, callback=self.parse_detail)
            yield weixin_request
        next_page = doc('#sogou_next').attr('href')
        if next_page:
            url = self.base_url + str(next_page)
            weixin_request = WeiXinRequest(url=url, callback=self.parse_index, need_proxy=True)
            yield weixin_request

    def start(self):
        """
        初始化工作
        """
        # 全局更新headers
        self.session.headers.update(self.headers)
        start_url = self.base_url + '?' + urlencode({'query': self.keyword, 'type': 2})
        weixin_request = WeiXinRequest(url=start_url, callback=self.parse_index, need_proxy=True)
        # 调度第一个请求
        self.queue.add(weixin_request)

    def my_request(self, weixin_request):
        """
        执行请求
        param weixin_request: 请求
        return: 响应
        """
        try:
            if weixin_request.need_proxy:
                proxy = self.get_proxy()
                if proxy:
                    proxies = {
                        'http': "http://" + proxy,
                        'https': "https://" + proxy
                    }
                    return self.session.send(weixin_request.prepare(), timeout=weixin_request.timeout, allow_redirects=False,
                        proxies=proxies)
            print(weixin_request)
            return self.session.send(weixin_request.prepare(), timeout=weixin_request.timeout, allow_redirects=False)
        except (ReadTimeout, ConnectionError) as e:
            print(e.args)
            return False

    def error(self, weixin_request):
        """
        错误处理
        param weixin_request:
        return:
        """
        weixin_request.fail_time = weixin_request.fail_time + 1
        print("Request Failed", weixin_request.fail_time, "Times", weixin_request.url)
        if weixin_request.fail_time < MAX_FAILED_TIME:
            self.queue.add(weixin_request)

    def schedule(self):
        """
        调度请求
        return:
        """
        while not self.queue.isEmpty():
            weixin_request = self.queue.pop()
            callback = weixin_request.callback
            print("Schedule", weixin_request.url)
            response = self.my_request(weixin_request)
            if response and response.status_code in VALID_STATUSES:
                results = list(callback(response))
                if results:
                    for result in results:
                        print("New Result", type(result))
                        if isinstance(result, WeiXinRequest):
                            self.queue.add(result)
                        else:
                            self.mysql.insert('articles', result)
                else:
                    self.error(weixin_request)
            else:
                self.error(weixin_request)

    def run(self):
        """
        入口
        return:
        """
        self.start()
        self.schedule()

if __name__ == '__main__':
    spider = Spider()
    # proxy = spider.get_proxy()
    # print(proxy)
    spider.run()
