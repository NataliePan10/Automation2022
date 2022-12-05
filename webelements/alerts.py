from webelements.browser import Browser
from webelements.UIElements import UIElement as Element
from selenium.webdriver.common.by import By
import time

URL = "http: //cleveronly.com/practice/"

class Alerts:
    def __init__(self, browser):
        self.driver = browser.get_driver()
        self.alert = self.driver.switch_to_alert()

    def switch_to_alert(self):
        return self.driver.switch_to_alert()

    def accept_alert(self):
        self.alert.accept()


    def cancel_alert(self):
        self.alert.dismiss()

    def enter_text(self, text):
        self.alert.send_keys(text)





