import json 
from appium import webdriver
from appium.options.android import UiAutomator2Options
import os



class StartAppium():
    def appium():
        current = os.getcwd()
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = "Emulator"
        with open(f'{current}/Config/config.json', 'r') as f:
            data = json.load(f)
            ip_address_entry = data['ip_address_entry']

        driver = webdriver.Remote(f'http://{ip_address_entry}:4723/wd/hub',options=options)
        return driver
   
if __name__ == '__main__':
    x = StartAppium()