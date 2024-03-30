from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import json, time
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By

class Key():
    def Entercode(driver):
        time.sleep(1)
        return driver.press_keycode(66)
if __name__ == "__main__":
    x = Key()