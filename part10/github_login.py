import requests
from lxml import etree

class Login(object):
    """docstring for Login"""
    def __init__(self):
        self.headers = {
            'Host': 'github.com',
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        }
        self.login_url = "https://github.com/login"
        self.post_url = "https://github.com/session"
        self.logined_url = "https://github.com/settings/profile"
        self.session = requests.Session()

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath("//input[@name='authenticity_token']/@value")
        return token

    def dynamics(self, html):
        selector = etree(html)


    def login(self, email, password):
        post_data = {
            # 'commit': 'Sign in',
            # 'utf8': '✓',
            'authenticity_token': self.token()[0],
            'login': email,
            'password': password
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            print("123")
        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            print("456")


if __name__ == '__main__':
    login = Login()
    login.login(email='lilihuakai', password='')
