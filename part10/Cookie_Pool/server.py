from config import *
from flask import Flask, g
from my_db import RedisClient


__all__ = ['app']

app = Flask(__name__)

@app.route('/')
def index():
    return "<h2>Welcome to Cookie Pool System</h2>"

def get_conn():
    """
    获取连接
    return:
    """
    for website in GENERATOR_MAP:
        print(website)
        if not hasattr(g, website):
            setattr(g, website + '_cookies', eval('RedisClient' + '("cookies", "' + website + '")'))
            setattr(g, website + '_accounts', eval('RedisClient' + '("cookies", "' + website + '")'))
    return g


@app.route('/<website>/random')
def random(website):
    """
    获取随机的Cookie, 访问地址如 /weibo/random
    return: 随机Cookie
    """
    g = get_conn()
    cookies = getattr(g, website + '_cookies').random()
    return cookies


if __name__ == '__main__':
    app.run(host='127.0.0.1')
