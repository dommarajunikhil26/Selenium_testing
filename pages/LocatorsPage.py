import utils.CustomLogger as cl
from base.BasePage import BaseClass
from selenium.webdriver.support.select import Select

class LocatorsPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    _enterText = "user_input" # id
    _radioBtn = "radio" # name
    _dropDown = "dropdown" # id
    _dropDownValue = "OptionFour" # value
    _multiSelect = "multiselect" # id
    _submitBtn = "submitbutton" # id
    _checkBox = "checkbox" # name

    def enterText(self):
        self.sendText("admin", self._enterText, "id")
        cl.allureLogs("Entered Text")
    
    def clickRadioButton(self):
        elements = self.getWebElements(self._radioBtn, "name")
        for element in elements:
            if element.get_attribute("value") == self._dropDownValue:
                element.click()
                cl.allureLogs("Clicked on radio button")
                break

    def clickDropDown(self):
        element = self.waitForElement(self._dropDown,"id")
        dropdownOptions = Select(element)
        dropdownValues = dropdownOptions.options

        for value in dropdownValues:
            if value.text == "mOptionThree" or value.text == "mOptionOne" or value.text == "mOptionFive":
                dropdownOptions.select_by_value(value.text)
    
    def clickChekBox(self):
        checkboxes = self.getWebElements(self._checkBox, "name")
        for box in checkboxes:
             if box.get_attribute("value") == "c2" or box.get_attribute("value") == "c3":
                box.click()

    def clickMultiSelect(self):
        element = self.waitForElement(self._multiSelect, "id")

        multiselectOptions = Select(element)
        multiselectValues = multiselectOptions.options

        for value in multiselectValues:
            if value.text == "mOptionTwo" or value.text == "mOptionFive" or value.text == "mOptionFour":
                multiselectOptions.select_by_value(value.text)
    
    def clickSubmitButton(self):
        self.clickElement(self._submitBtn, "id")
