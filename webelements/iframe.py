from webelements.browser import Browser
from webelements.UIElements import UIElement as Element
from selenium.webdriver.common.by import By
import time

URL = "http://cleveronly.com/practice/"

class Iframe(Element):
    def __init__(self, browser, by, locator):
        super.__init__(browser, by, locator)
        self.driver = browser.get_driver()
        self.iframe = self.driver.switch_to.frame(self.get_element())

    def switch_to_iframe(self):
        return self.iframe