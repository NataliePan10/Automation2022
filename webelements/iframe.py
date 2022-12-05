from webelements.browser import Browser
from webelements.UIElements import UIElement as Element
from selenium.webdriver.common.by import By
import time

URL = "http://cleveronly.com/practice/"

class Iframe:
    def __init__(self, browser):
        self.driver = browser.get_driver()
        self.iframe = self.driver.switch_to.frame(iframe.get_element())

    def switch_to_iframe(self):
        return self.switch_to_iframe()