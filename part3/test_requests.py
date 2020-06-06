import requests
import re
from requests import Request, Session
from requests.auth import HTTPBasicAuth


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebkit/5377.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}


# Prepared Request
url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)


# 身份验证
# r = requests.get('http://localhost:5000', auth=('username', 'password'))
# r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
# print(r.status_code)


# 超时
# r = requests.get('https://www.taobao.com', timeout=1)
# print(r.status_code)


# 代理
# proxies = {
#     'http': "http://10.10.1.10:3128",
#     'http': "http://user:password@10.10.1.10:3128",
#     'https': "socks5://user:password@host:port"
# }
# requests.get('https://www.taobao.com', proxies=proxies)


# SSL证书验证
# response = requests.get('https://www.12306.cn')
# print(response.status_code)


# 会话Session
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)


# Cookies
# r = requests.get('http://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
    # print(key + '=' + value)


# 文件上传
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)


# 响应
# r = requests.get('http://www.jianshu.com')
# print(type(r.status_code), r.status_code)
# print(type(r.headers), r.headers)
# print(type(r.cookies), r.cookies)
# print(type(r.url), r.url)
# print(type(r.history), r.history)


# POST
# data = {
#     'name': 'germey',
#     'age': 22
# }
# r = requests.post('http://httpbin.org/post', data=data)
# print(r.text)


# 图片
# r = requests.get('http://github.com/favicon.ico')
# print(r.text)
# print(r.content)
# with open('favicon.ico', 'wb') as f:
    # f.write(r.content)


# headers
# r = requests.get('http://www.zhihu.com/explore', headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# title = re.findall(pattern, r.text)
# print(title)


# params
# data = {
#     'name': 'germey',
#     'age': 22
# }
# r = requests.get('http://httpbin.org/get', params=data)
# print(r.text)


# get()
# r = requests.get('http://www.baidu.com')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)
