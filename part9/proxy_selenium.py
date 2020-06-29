from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile




# ## 第一步：创建一个FirefoxProfile实例
profile = FirefoxProfile()


# # Firefox浏览器1
# ## 第二步：开启“手动设置代理”
# profile.set_preference('network.proxy.type', 1)
# ## 第三步：设置代理IP
# profile.set_preference('network.proxy.http', '39.108.4.66')
# ## 第四步：设置代理端口，注意端口是int类型，不是字符串
# profile.set_preference('network.proxy.http_port', 24000)
# ## 第五步：设置htpps协议也使用该代理
# profile.set_preference('network.proxy.ssl', '39.108.4.66')
# profile.set_preference('network.proxy.ssl_port', 24000)

# Firefox浏览器2
# 不使用代理的协议，注释掉对应的选项即可
settings = {
    'network.proxy.type': 1,  # 0: 不使用代理；1: 手动配置代理
    'network.proxy.http': '39.108.4.66',
    'network.proxy.http_port': 24000,
    'network.proxy.ssl': '39.108.4.66',  # https的网站,
    'network.proxy.ssl_port': 24000,
}
# 更新配置文件
for key, value in settings.items():
    profile.set_preference(key, value)

# chrome浏览器
# proxy = '39.108.4.66:24000'
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=http://' + proxy)
# chrome = webdriver.Chrome(chrome_options=chrome_options)
# chrome.get('http://httpbin.org/get')


# 无头模式
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
# browser = webdriver.Firefox(firefox_options=options)
browser = webdriver.Firefox(firefox_options=options, firefox_profile=profile)
# browser = webdriver.Firefox(profile)
browser.get('http://httpbin.org/get')
# browser.get('https://www.google.com/')
print(browser.page_source)
