from base.DriverClass import WebDriverClass
import utils.CustomLogger as cl
import time

wd = WebDriverClass()

driver = wd.get_driver("Chrome")

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
log = cl.customLogger()
log.info("Web Page Launched")

time.sleep(2)
driver.quit()