import pytest
import unittest
from base.BasePage import BaseClass
from pages.LocatorsPage import LocatorsPage

@pytest.mark.usefixtures("setUpClass", "setUpMethod")
class TestLocatorsPage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def setUpClassObjects(self):
        self.lp = LocatorsPage(self.driver)
        self.bp = BaseClass(self.driver)
    
    @pytest.mark.run(order=3)
    def test_enterFormDetails(self):
        self.lp.enterText()
        self.lp.clickRadioButton()
        self.lp.clickChekBox()
        self.lp.clickMultiSelect()
        self.lp.clickSubmitButton()