from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import json, time
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By

class TextFind():
    def TextWeb(driver, text):
        time.sleep(1)
        body = driver.find_element(By.TAG_NAME, 'body')
        bodys_in = body.find_elements(By.XPATH, '/*')
        print(len(bodys_in))
        for count in range(len(bodys_in)):
            print(bodys_in[count].text)
            if bodys_in[count].text == text:
                return bodys_in[count]
if __name__ == '__main__':
    x = TextFind()