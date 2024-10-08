from traceback import print_stack
import utils.CustomLogger as cl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver import ActionChains
import utils.CustomLogger as cl
import allure
from allure_commons.types import AttachmentType 

class BaseClass:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver
    
    def launchWebPage(self, url, title):
        try:
            self.driver.get(url)
            assert title in self.driver.title
            self.log.info("Webpage launched with url: "+ url)
        except:
            self.log.error(f"Web page with url: {url} failed to launch")
            print_stack()

        
    def getLocatorType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "partialLink":
            return By.PARTIAL_LINK_TEXT
        elif locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "xpath":
            return By.XPATH
        else:
            self.log.info(f"Locator Type: {locatorType} is not found")
            print_stack()
            self.takeScreenShot(locatorType)

    
    def getWebElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            element = self.driver.find_element(locatorByType, locatorValue)
            self.log.info(f"WebElement found with locatorValue: {locatorValue} and locatorType: {locatorType}")
        except:
            self.log.error(f"WebElement not found with locatorValue: {locatorValue} and locatorType: {locatorType}")
            print_stack()
            self.takeScreenShot(locatorType)
            assert False
        return element
    
    def getWebElements(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            element = self.driver.find_elements(locatorByType, locatorValue)
            self.log.info(f"WebElements found with locatorValue: {locatorValue} and locatorType: {locatorType}")
        except:
            self.log.error(f"WebElements not found with locatorValue: {locatorValue} and locatorType: {locatorType}")
            print_stack()
            self.takeScreenShot(locatorType)
            assert False
        return element

    def waitForElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            wait = WebDriverWait(self.driver, 25, 1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            element = wait.until(EC.presence_of_element_located((locatorByType, locatorValue)))
            self.log.info(f"WebElement found with locatorValue: {locatorValue} and locatorType: {locatorType}")
        except:
            self.log.error(f"WebElement not found with locatorValue: {locatorValue} and locatorType: {locatorType}")
            print_stack()
            self.takeScreenShot(locatorType)
            assert False
        return element
    
    def waitForElements(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            wait = WebDriverWait(self.driver, 25, 1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            element = wait.until(EC.presence_of_all_elements_located((locatorByType, locatorValue)))
            self.log.info(f"WebElement found with locatorValue: {locatorValue} and locatorType: {locatorType}")
        except:
            self.log.error(f"WebElement not found with locatorValue: {locatorValue} and locatorType: {locatorType}")
            print_stack()
            self.takeScreenShot(locatorType)
            assert False
        return element
    
    def clickElement(self, locatorValue, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.click()
            self.log.info(f"Clicked on WebElement with locatorValue: {locatorValue} and locatorType: {locatorType}")
        except:
            self.log.error(f"Unable to clikc on WebElement with locatorValue: {locatorValue} and locatorType: {locatorType}")
            print_stack()
            self.takeScreenShot(locatorType)
            assert False

    
    def sendText(self,text, locatorValue, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(f"Sent the text: {text} on WebElement with locatorValue: {locatorValue} and locatorType: {locatorType}")
        except:
            self.log.error(f"Unable to send the text: {text} on WebElement with locatorValue: {locatorValue} and locatorType: {locatorType}")
            self.takeScreenShot(locatorType)
            print_stack()
            assert False

    def getText(self, locatorValue, locatorType="id"):
        element_text = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            element_text = element.text
            self.log.info(f"Got the text {element_text} from WebElement with locatorValue: {locatorValue} and locatorType: {locatorType}")
        except:
            self.log.error(f"Unable to get the text {element_text} from WebElement with locatorValue: {locatorValue} and locatorType: {locatorType}")
            print_stack()
            assert False
        return element_text
    
    def isElementDisplayed(self, locatorValue, locatorType="id"):
        isDisplayed = False
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            isDisplayed = element.is_displayed
            self.log.info(f"WebElement with locatorValue: {locatorValue} and locatorType: {locatorType} is displayed: {isDisplayed}")
        except:
            self.log.error(f"WebElement with locatorValue: {locatorValue} and locatorType: {locatorType} is displayed: {isDisplayed}")
            self.takeScreenShot(locatorType)
            print_stack()
            assert False
        return isDisplayed
    
    def scrollTo(self, locatorValue, locatorType="id"):
        actions = ActionChains(self.driver)
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            actions.move_to_element(element).perform()
            self.log.info(f"Scrolled to WebElement with locatorValue: {locatorValue} and locatorType: {locatorType}")
        except:
            self.log.error(f"Unable to scroll to WebElement with locatorValue: {locatorValue} and locatorType: {locatorType}")
            self.takeScreenShot(locatorType)
            print_stack()
            assert False

    def takeScreenShot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    