from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import json, time


class TapElement():
    def tapLocation(driver, element):
        return driver.tap([(int(element.location['x'])+10, int(element.location['y'])+10)])
        
if __name__ == '__main__':
    x = TapElement()