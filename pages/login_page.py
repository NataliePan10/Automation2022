from components.header import Header
from components.right_menu import RightMenu
from webelements.UIElements import UIElement as Element
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self), browser):
        self.header = Header(browser)
        self.right_menu = RightMenu(browser)
        self.continue_btn = Element(browser, By.XPATH, "//a[contains(text(), 'Continue')]")

    def open_registration_from_menu(self):
        self.header.open_login_page()
        self.right_menu.click_registration()


    def open_registration_from_account_dropdown(self):
        self.header.open_registration_form()
    def click_continue_btn(self):
        self.header.open_login_page()
        self.continue_btn.click()

