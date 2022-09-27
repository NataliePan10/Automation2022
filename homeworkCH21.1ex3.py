from webelements.UIElements import UIElement as Element
from selenium.webdriver.common.by import By


class Footer:
    def __init__(self, browser):
        self.about_us_btn = Element(browser, By.ID, "about-us")
        self.privacy_policy_btn = Element(browser, By.ID, "privacy-policy")
        self.contact_us_btn = Element(browser, By.XPATH, "//a[@title='Contact Us']")


    def check_about_us(self):
        self.about_us_btn.click()

    def check_privacy_policy(self):
        self.privacy_policy_btn.click()

    def contact_us_form(self):
        self.contact_us_btn.click()