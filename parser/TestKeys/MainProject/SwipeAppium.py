from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import json, time


class Swipe():
    def toElemntDown(driver, xpath):
        for i in range(1000):
            driver.swipe(650,2000,650,1800)
            try:
                time.sleep(1)
                element = driver.find_element(by=AppiumBy.XPATH, value = xpath)
                return print(element)
            except:
                continue
            
            
    def toElemntUp(driver, xpath):
        for i in range(1000):
            driver.swipe(650,1800,650,2000)
            try:
                time.sleep(1)
                element = driver.find_element(by=AppiumBy.XPATH, value = xpath)
                return print(element)
            except:
                continue
if __name__ == '__main__':
    x = Swipe()