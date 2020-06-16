import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 无头模式
# options = webdriver.FirefoxOptions()
# options.add_argument('-headless')
# browser = webdriver.Firefox(firefox_options=options)
# Chrome_options = webdriver.ChromeOptions()
# Chrome_options.add_argument('-headless')
# browser = webdriver.Chrome(chrome_options=Chrome_options)
browser = webdriver.Firefox()
# browser = webdriver.Chrome()

# 选项卡
browser.get("https://www.baidu.com")
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get("https://www.taobao.com")
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get("https://www.taobao.com")

# Cookies
# url = "https://www.zhihu.com/explore"
# browser.get(url)
# print(browser.get_cookies())
# browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

# Back\Forward
# browser.get("https://www.baidu.com")
# browser.get("https://www.taobao.com")
# browser.get("https://www.python.org")
# browser.back()
# time.sleep(1)
# browser.forward()

# 显式等待
# wait = WebDriverWait(browser, 10)
# wait.until(EC.presence_of_element_located((By.ID, 'content_left')))

# 隐式等待
# browser.implicitly_wait(10)

# url = "https://www.zhihu.com/explore"
# browser.get(url)
# 获取ID、位置、标签名和大小
# login = browser.find_element_by_class_name('AppHeader-login')
# print(login.id)
# print(login.location)
# print(login.tag_name)
# print(login.size)

# 获取文本
# login = browser.find_element_by_class_name('AppHeader-login')
# print(login.text)

# 获取属性
# logo = browser.find_element_by_class_name('AppHeader-inner')
# print(logo)
# print(logo.get_attribute('class'))

# 执行JavaScript
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Buttom")')


# url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# 切换Frame
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('NO LOGO')
# except Exception as e:
#     print(e)
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)

# 动作链：鼠标拖拽、键盘按键
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

browser.close()
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[0])
browser.close()

# try:
#     browser.get("https://www.taobao.com")

    # 交互
    # input = browser.find_element_by_id('q')
    # input.send_keys('iPhone')
    # time.sleep(1)
    # input.clear()
    # input.send_keys('iPad')
    # button = browser.find_element_by_class_name('btn-search')
    # button.click()

    # lis = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')
    # lis = browser.find_elements_by_css_selector('.service-bd li')
    # print(lis)

    # input_first = browser.find_element(By.ID, 'q')
    # print(input_first)

    # input_first = browser.find_element_by_id('q')
    # input_second = browser.find_element_by_css_selector('#q')
    # input_third = browser.find_element_by_xpath('//*[@id="q"]')
    # print(input_first, input_second, input_third)

    # browser.get("https://www.baidu.com")
    # input = browser.find_element_by_id('kw')
    # input.send_keys('Python')
    # input.send_keys(Keys.ENTER)
    # wait = WebDriverWait(browser, 10)
    # input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    # button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
    # print(input, button)

    # wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    # print(browser.current_url)
    # print(browser.get_cookies())
    # print(browser.page_source)
# finally:
#     browser.close()
