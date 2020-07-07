# API地址和端口
API_HOST = '127.0.0.1'
API_PORT = 5000
# API接口服务
API_PROCESS = True

# 产生器和验证器循环周期
CYCLE = 120

GENERATOR_MAP = {
    'weibo': 'WeiboCookiesGenetator'
}
# 产生器开关，模拟登录添加Cookies
GENERATOR_PROCESS = False

REDIS_HOST = 'localhost'
REDIS_PASSWORD = None
REDIS_PORT = 6379

# 验证器开关，循环检测数据库中Cookies是否可用，不可用删除
VALID_PROCESS = False