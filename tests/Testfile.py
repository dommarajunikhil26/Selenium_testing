from base.BasePage import BaseClass
from base.DriverClass import WebDriverClass
from pages.FormPage import FormPage
import utils.CustomLogger as cl
import time

wd = WebDriverClass()

driver = wd.get_driver("chrome")
bp = BaseClass(driver)

fp = FormPage(driver)

bp.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html", "Selenium Template — DummyPoint")

fp.openFormPage()
time.sleep(2)
fp.verifyFormPage()
time.sleep(2)
fp.enterName()
fp.enterEmail()
fp.clickRadioButton()
fp.enterMessage()
fp.enterTech()
fp.enterCaptcha()
fp.submitForm()

time.sleep(3)
driver.quit()