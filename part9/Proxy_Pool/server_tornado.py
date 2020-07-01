import json
import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler, Application
from mydb import RedisClient
from loguru import logger

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8055


class Server(RequestHandler):
    """docstring for Server"""
    def initialize(self, redis):
    # def __init__(self, arg):
        """
        初始化
        param redis:
        """
        self.redis = redis

    def get(self, api=''):
        """
        API列表
        param api: 接口类型
        return:
        """
        if not api:
            links = ['random', 'all', 'count']
            self.write('<h4>Welcome to Liuzm Proxy API</h4>')
            for link in links:
                self.write('<a href=' + link + '>' + link + '</a><br>')
        if api == 'random':
            result = self.redis.random()
            if result:
                self.write(result)
        if api == 'all':
            result = self.redis.all()
            if result:
                self.write(json.dumps(result))
        if api == 'count':
            result = self.redis.count()
            if result:
                self.write(str(result))



def server(redis=None, address=SERVER_HOST, port=SERVER_PORT):
    if not redis:
        redis = RedisClient()
    application = Application([
        (r'/', Server, dict(redis=redis)),
        (r'/(.*)', Server, dict(redis=redis))
        ])
    application.listen(port, address=address)
    logger.info(f'API listening on http://{address}:{port}')
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    server()
