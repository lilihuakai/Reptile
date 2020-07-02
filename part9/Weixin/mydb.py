from pickle import dumps, loads
from redis import StrictRedis
# My
from config import *
from my_request import WeiXinRequest


class RedisQueue(object):
    """docstring for RedisQueue"""
    def __init__(self):
        """
        初始化Redis
        """
        self.db = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)

    def add(self, request):
        """
        向队列添加序列化后的Request
        param request: 请求对象
        return: 添加结果
        """
        if isinstance(request, WeiXinRequest):
            return self.db.rpush(REDIS_KEY, dumps(request))
        return False

    def pop(self):
        """
        取出下一个Request并反序列化
        return: Request对象 或者 None
        """
        if self.db.llen(REDIS_KEY):
            return loads(self.db.lpop(REDIS_KEY))
        else:
            return False

    def isEmpty(self):
        """
        判断队列是否为空
        """
        return self.db.llen(REDIS_KEY) == 0


if __name__ == '__main__':
    db = RedisQueue()
    url = "http://weixin.sogou.com"
    weixinRequest = WeiXinRequest(url=url, callback='hello', need_proxy=True)
    print(weixinRequest)
    db.add(weixinRequest)
    request = db.pop()
    print(request)
