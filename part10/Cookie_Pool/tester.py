import requests
from my_db import RedisClient


class ValidTester(object):
    """docstring for ValidTester"""
    def __init__(self, website='default'):
        """
        初始化一些对象
        param website: 名称
        """
        self.website = website
        self.cookies_db = RedisClient('cookies', self.website)
        self.accounts_db = RedisClient('accounts', self.website)

    def test(self, username, cookies):
        """
        测试生成Cookies，子类需要重写
        param username: 用户名
        param password: 密码
        return:
        """
        raise NotImplementedError

    def run(self):
        cookies_groups = self.cookies_db.all()
        for username, cookies in cookies_groups.items():
            self.test(username, cookies)


class WeiboValidTester(ValidTester):
    """docstring for WeiboValidTester"""
    def __init__(self, website='weibo'):
        ValidTester.__init__(self, website)

    def test(self, username, cookies):
        print("正在测试Cookies", "用户名",username)
        try:
            cookies = json.loads(cookies)
        except TypeError:
            self.cookies_db.delete(username)
            print(e.args)
            return
        try:
            test_url = ""
            response = requests.get(test_url, cookies=cookies, timeout=5, allow_redirects=False)
            if response.status_code == 200:
                print("Cookies有效", username)
            else:
                print(response.status_code, response.headers)
                print("Cookies失效", username)
                self.cookies_db.delete(username)
                print("删除Cookies", username)
        except Exception as e:
            print(e.args)


if __name__ == '__main__':
    WeiboValidTester().run()
