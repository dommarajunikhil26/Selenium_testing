from base.BasePage import BaseClass
import utils.CustomLogger as cl

class FormPage(BaseClass):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _formPage = "Form" # Link Text
    _checkFormPage = "h2" # Tag Name
    _enterName = "name" # id
    _enterEmail = "email" # id
    _radioButtons = "g" # id
    _enterTech = "tech" # id
    _enterMessage = "message" # id
    _captchaImage = "captcha_image" # id
    _enterCaptcha = "captcha" # id
    _clickSubmit = "btnContactUs" # id

    def openFormPage(self):
        self.clickElement(self._formPage, "link")
        cl.allureLogs("Opened Form Page")
    
    def verifyFormPage(self):
        element = self.getWebElement(self._checkFormPage, "tag")
        assert "Form 1" == element.text
    
    def enterName(self):
        self.sendText("admin", self._enterName, "id")
    
    def enterEmail(self):
        self.sendText("admin@gmail.com", self._enterEmail, "id")
    
    def clickRadioButton(self):
        elements = self.getWebElements(self._radioButtons, "id")
        for element in elements:
            if element.get_attribute("value") == "male":
                element.click()
                break
    def enterTech(self):
        self.sendText("admin full stack technology", self._enterTech, "id")
    
    def enterMessage(self):
        self.sendText("Demo app", self._enterMessage, "id")
    
    def getCaptcha(self):
        captcha = self.getText(self._captchaImage, "id")
        return captcha
    
    def enterCaptcha(self):
        self.sendText(self.getCaptcha(), self._enterCaptcha, "id")
    
    def submitForm(self):
        self.scrollTo(self._clickSubmit, "id")
        self.clickElement(self._clickSubmit, "id")