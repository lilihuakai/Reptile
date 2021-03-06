import redis
from random import choice


INITIAL_SCORE = 10
MAX_SCORE = 100
MIN_SCORE = 0
REDIS_HOST = 'localhost'
REDIS_KEY = 'proxies'
REDIS_PASSWORD = None
REDIS_PORT = 6379


class PoolEmptyException(Exception):
    def __str__(self):
        """
        proxypool is used out
        :return:
        """
        return repr('no proxy in proxypool')

class RedisClient(object):
    """docstring for RedisClient"""
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        初始化
        param host: redis 地址
        param port: redis 端口
        param password: redis 密码
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password, decode_responses=True)

    def add(self, proxy, score=INITIAL_SCORE):
        """
        添加代理，设置分数最高
        param proxy: 代理
        param score: 分数
        return: 添加结果
        """
        if not self.db.zscore(REDIS_KEY, proxy):
            mapping = {proxy: score}
            return self.db.zadd(REDIS_KEY, mapping)
            # return self.db.zadd(REDIS_KEY, score, proxy)

    def random(self):
        """
        随机获取有效代理，首先尝试获取最高分数代理，如果最高分数不存在，则按照排名获取，否则异常
        return: 随机代理
        """
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):
                return choice(result)
            else:
                raise PoolEmptyException
                # raise PoolEmptyError

    def decrease(self, proxy):
        """
        代理值减一分，分数小于最低值，则代理删除
        param proxy: 代理
        return: 修改后的代理分数
        """
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print("代理", proxy, "当前分数", score, "减一")
            return self.db.zincrby(REDIS_KEY, -1, proxy)
        else:
            print("代理", proxy, "当前分数", score, "移除")
            return self.db.zrem(REDIS_KEY, proxy)

    def exists(self, proxy):
        """
        判断是否存在
        param proxy: 代理
        return: 是否存在
        """
        return not self.db.zscore(REDIS_KEY, proxy) == None

    def max(self, proxy):
        """
        将代理设置为最大值MAX_SCORE
        param proxy: 代理
        return: 设置结果
        """
        print("代理", proxy, "可以，设置为", MAX_SCORE)
        return self.db.zadd(REDIS_KEY, {proxy: MAX_SCORE})

    def count(self):
        """
        获取数量
        return: 数量
        """
        return self.db.zcard(REDIS_KEY)

    def all(self):
        """
        获取全部代理
        return: 全部代理列表
        """
        return self.db.zrevrangebyscore(REDIS_KEY, MAX_SCORE, MIN_SCORE)


if __name__ == '__main__':
    conn = RedisClient()
    result = conn.random()
    print(result)
