import pytest
import unittest
import time

from base.BasePage import BaseClass
from pages.LocatorsPage import LocatorsPage

@pytest.mark.usefixtures("setUpClass", "setUpMethod")
class FormPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setUpClassObjects(self):
        self.lp = LocatorsPage(self.driver)
        self.bp = BaseClass(self.driver)
    
    def test_enterFormDetails(self):
        self.lp.enterText()
        self.lp.clickRadioButton()
        self.lp.clickChekBox()
        self.lp.clickMultiSelect()
        self.lp.clickSubmitButton()