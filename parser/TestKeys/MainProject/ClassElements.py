from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import json, time
from appium_flutter_finder.flutter_finder import FlutterElement, FlutterFinder
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By

class ClassFind():
    def findAllClassNames(driver, className):
        time.sleep(1)
        class_name = driver.find_elements(by=AppiumBy.CLASS_NAME, value = className) 
        return class_name
    def webfindClasses(driver, className):
        time.sleep(1)
        return driver.find_elements(By.CLASS_NAME,className)
    def webfindClass(driver, className):
        time.sleep(1)
        return driver.find_element(By.CLASS_NAME,className)
    
    def webCssSelectr(driver, className):
        return driver.find_element(By.CSS_SELECTOR,className)
    def webCssSelectors(driver, className):
        return driver.find_elements(By.CSS_SELECTOR,className)
    
    def Attribute(driver, tag):
        time.sleep(1)
        return driver.get_attribute(tag)
        
if __name__ == "__main__":
    x = ClassFind()