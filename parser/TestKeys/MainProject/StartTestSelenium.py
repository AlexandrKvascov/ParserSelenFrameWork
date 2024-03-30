import json    
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os 
    
class StartSelenium():
    def sellenium():
        current = os.getcwd()
        with open(f'{current}/Config/config.json', 'r') as f:
            data = json.load(f)
        chromedriver_path = data['chromedriver_path']
        service = Service(executable_path=chromedriver_path)
        options = Options()
        options.add_argument("--disable-extensions")
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        # options.capabilities('C:\\Users\\AlexandrKosov\\Desktop\\Test_Appium\\chromedriver-win64\\chromedriver.exe')
        driver = webdriver.Chrome(service=service,options=options)
        return driver
    
if __name__ == '__main__':
    
    x = StartSelenium()