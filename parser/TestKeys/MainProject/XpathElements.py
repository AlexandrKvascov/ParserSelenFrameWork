from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import json, time
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By


class XpathFind():
    def find_content_view(driver, xpath):
        time.sleep(1)
        return driver.find_element(by=AppiumBy.XPATH, value = f'//android.view.View[contains(@content-desc, "{xpath}")]')
    def find_content_widget_button(driver, xpath):
        time.sleep(1)
        return driver.find_element(by=AppiumBy.XPATH, value = f'//android.widget.Button[contains(@content-desc, "{xpath}")]')
    def find_content_widget_image(driver, xpath):
        time.sleep(1)
        return driver.find_element(by=AppiumBy.XPATH, value = f'//android.widget.ImageView[contains(@content-desc, "{xpath}")]')
    def find_xpath_app(driver, xpath):
        time.sleep(1)
        return driver.find_element(by=AppiumBy.XPATH, value = xpath)
    def web_xpath(driver, xpath):
        time.sleep(1)
        return driver.find_element(By.XPATH,xpath)
    def web_xpaths(driver, xpaths):
        time.sleep(1)
        return driver.find_elements(By.XPATH, xpaths)
if __name__ == '__main__':
    x = XpathFind()