from base.BasePage import BaseClass

class FormPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _FormPage = "Form" # Link Text
    _checkPage = "Form 1" # Tag Name
    _enterName = "name" # id
    _enterEmail = "email" # id
    