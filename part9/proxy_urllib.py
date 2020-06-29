import socks
import socket
from urllib import request
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

# socks5代理
socks.set_default_proxy(socks.SOCKS5, '39.108.4.66', 24000)
socket.socket = socks.socksocket
# 需要认证的代理
# proxy = 'username:password@39.108.4.66:24000'
# proxy = '39.108.4.66:24000'
# proxy_handler = ProxyHandler({
#     'http': 'http://' + proxy,
#     'https': 'https://' + proxy
#     })
# opener = build_opener(proxy_handler)

try:
    # socks5
    response = request.urlopen('http://httpbin.org/get')
    # response = opener.open('http://httpbin.org/get')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
except Exception as e:
    raise e