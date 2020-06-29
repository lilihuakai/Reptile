import requests
import socks
import socket


# socks5代理--全局
socks.set_default_proxy(socks.SOCKS5, '39.108.4.66', 24000)
socket.socket = socks.socksocket
# socks5代理
# proxy = '39.108.4.66:24000'
# proxies = {
#     'http': 'socks5://' + proxy,
#     'https': 'socks5://' + proxy
# }
# 需要认证的代理
# proxy = 'username:password@39.108.4.66:24000'
# proxy = '39.108.4.66:24000'
# proxies = {
#     'http': 'http://' + proxy,
#     'https': 'https://' + proxy
# }

try:
    # socks5
    response = requests.get('http://httpbin.org/get')
    # response = requests.get('http://httpbin.org/get', proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print("Error", e.args)
