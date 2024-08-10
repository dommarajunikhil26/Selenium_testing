from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import utils.CustomLogger as cl

chrome_options = Options()
chrome_options.add_argument('--start-maximized')

chrome_service = Service('/opt/homebrew/bin/chromedriver')

class WebDriverClass:
    log = cl.customLogger()

    def get_driver(self, browserName):
        driver = None
        if browserName.lower() == "chrome":
            driver = webdriver.Chrome(options=chrome_options, service=chrome_service)
            self.log.info("Initializing Chrome Driver")
        elif browserName.lower() == "safari":
            driver = webdriver.Safari() 
            self.log.info("Initializing Safari Driver")
        return driver
            