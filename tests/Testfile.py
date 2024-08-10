from base.BasePage import BaseClass
from base.DriverClass import WebDriverClass
import utils.CustomLogger as cl
import time

wd = WebDriverClass()

driver = wd.get_driver("chrome")
bp = BaseClass(driver)

bp.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html", "Selenium Template — DummyPoint")
bp.sendText("admin", "user_input", "id")

time.sleep(2)
driver.quit()