from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


# Appium地址
server = "http://localhost:4723/wd/hub"
desired_caps = {
  "platformName": "Android",
  "deviceName": "NX549J",
  "appPackage": "com.tencent.mm",
  "appActivity": ".ui.LauncherUI"
}
driver = webdriver.Remote(server, desired_caps)
el =  driver.find_element_by_id('com.tencent.mm:id/........')