from requests import Request
# My
from config import *


class WeiXinRequest(Request):
    """docstring for WeiXinRequest """
    def __init__(self, url, callback, method='GET', headers=None, need_proxy=False,
        fail_time=0, timeout=TIME_OUT):
        Request.__init__(self, method, url, headers)
        self.callback = callback
        self.need_proxy = need_proxy
        self.fail_time = fail_time
        self.timeout = timeout

