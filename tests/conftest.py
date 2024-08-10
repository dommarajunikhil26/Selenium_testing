import pytest
from base.BasePage import BaseClass
from base.DriverClass import WebDriverClass
import time

@pytest.fixture(scope="class")
def setUpClass(request):
    print("Before Class")
    driver_instance = WebDriverClass()
    driver = driver_instance.get_driver("chrome")
    bp = BaseClass(driver)
    bp.launchWebPage("http://www.dummypoint.com/seleniumtemplate.html", "Selenium Template — DummyPoint")
    if request.cls is not None: # we are changing driver objet into class level object so that
        # it is available for all classes at test folder
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print("After Class")

@pytest.fixture()
def setUpMethod():
    print("Before Method")
    yield
    print("After Method")