from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import json, time
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By



class IdFind():
    def find_id(driver, id):
        time.sleep(1)
        return driver.find_element(by=AppiumBy.ID, value = id)
    def finds_id(driver, id):
        time.sleep(1)
        return driver.find_elements(by=AppiumBy.ID, value = id)
    
    def web_id_find(driver, id):
        time.sleep(1)
        return driver.find_element(By.ID, id)
    

    def web_id_finds(driver, id):
        time.sleep(1)
        return driver.find_elements(By.ID, id)
    
    
    
    # def finds_id_text(driver, id):
    #     time.sleep(1)
    #     yield driver.find_element(by=AppiumBy.ID, value = id).text
    
if __name__ == '__main__':
    x = IdFind()