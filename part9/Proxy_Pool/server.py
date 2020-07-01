from flask import Flask, g
from mydb import RedisClient

API_HOST = '127.0.0.1'
API_PORT = 5055
API_THREADED = True
app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis

@app.route('/')
def index():
    return '<h2>Welcome to Proxy System</h2>'

@app.route('/random')
def get_proxy():
    """
    获取随机可用代理
    return: 随机代理
    """
    conn = get_conn()
    return conn.random()

@app.route('/count')
def get_count():
    """
    获取代理池总量
    return: 代理池总量
    """
    conn = get_conn()
    return str(conn.count())


if __name__ == '__main__':
    app.run(host=API_HOST, port=API_PORT, threaded=API_THREADED)
