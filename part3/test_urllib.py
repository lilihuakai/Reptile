import socket
import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar
from urllib import request, parse, error
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.request import ProxyHandler
from urllib.error import URLError
from urllib.parse import urlparse, urlunparse
from urllib.parse import urlsplit, urlunsplit
from urllib.parse import urljoin
from urllib.parse import urlencode, parse_qs, parse_qsl
from urllib.parse import quote, unquote
from urllib.robotparser import RobotFileParser

# RobotFileParser
rp = RobotFileParser('http://www.jianshu.com/robot.txt')
# rp = RobotFileParser()
# rp.set_url('http://www.jianshu.com/robot.txt')
rp.read()
print(rp.can_fetch('*', 'http://www.jianshu.com/p'))
print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))

# quote
# keyword = '壁纸'
# url = 'http://www.baidu.com?wd=' + quote(keyword)
# print(url)
# print(unquote(url))

# urlencode
# params = {
#     'name': 'germey',
#     'age': 21
# }
# query = 'age=21&name=germey'
# base_url = 'http://www.baidu.com?'
# url = base_url + urlencode(params)
# print(url)
# print(parse_qs(query))
# print(parse_qsl(query))


# urljoin
# print(urljoin('http://www.baidu.com', 'FAQ.html'))
# print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
# print(urljoin('http://www.baidu.com?wd=adb', 'https://cuiqingcai.com/index.html'))
# print(urljoin('http://www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com#comment', '?category=2'))

# urlunsplit
# data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
# print(urlunsplit(data))

# urlsplit
# result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
# print(result)
# print(result.scheme, result[0])

# urlunparse
# data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
# print(urlunparse(data))

# urlparse
# result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment', scheme='https')
# result = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print(result.scheme, result[0], result.netloc, result[1])
# print(type(result), result)

# LWPCookieJar
# filename = 'cookie2.txt'
# # cookie = http.cookiejar.LWPCookieJar(filename)
# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookie2.txt', ignore_discard=True, ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = build_opener(handler)
# response = opener.open('https://www.baidu.com')
# # cookie.save(ignore_discard=True, ignore_expires=True)
# print(response.read().decode('utf-8'))

# 保存Cookie成文件
# filename = 'cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = build_opener(handler)
# response = opener.open('https://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# Cookies
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = build_opener(handler)
# response = opener.open('https://www.baidu.com')
# for item in cookie:
#     print(item.name + "=" + item.value)

# 代理
# proxy_handler = ProxyHandler({
#     'http': 'http://127.0.0.1:9743',
#     'https': 'https://127.0.0.1:9743'
#     })
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('https://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

# 验证
# username = 'username'
# password = 'password'
# url = 'http://localhost:5000/'

# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)

# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)


# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
# response = urllib.request.urlopen('https://www.python.org')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# print(response.read().decode('utf-8'))
# print(response.read())
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))

# 超时设置
# try:
#     response = request.urlopen('http://httpbin.org/get123')
#     # response = request.urlopen('http://httpbin.org/get', timeout=0.1)
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')
# request = urllib.request.Request('http://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# 请求头header
# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org'
# }
# dict = {
#     'name': 'Germey'
# }
# data = bytes(parse.urlencode(dict), encoding='utf-8')
# req = request.Request(url, data=data, headers=headers, method='POST')
# req = request.Request(url, data=data, method='POST')
# req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))

