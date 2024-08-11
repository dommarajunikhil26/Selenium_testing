import pytest
import unittest
import time

from base.BasePage import BaseClass
from pages.FormPage import FormPage

@pytest.mark.usefixtures("setUpClass", "setUpMethod")
class TestFormPage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setUpClassObjects(self):
        self.fp = FormPage(self.driver)
        self.bp = BaseClass(self.driver)
    
    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        time.sleep(5)
        self.fp.enterName()
        self.fp.enterEmail()
        self.fp.clickRadioButton()
        self.fp.enterMessage()
        self.fp.enterTech()
        self.fp.enterCaptcha()
        self.fp.submitForm()

    @pytest.mark.run(order=1)
    def test_launchFormPage(self):
        self.fp.openFormPage()
        self.fp.verifyFormPage()
    