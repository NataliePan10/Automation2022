from Internship.BotanikaBeautyTests.components.navigation_bar import NavigationBar
from Internship.BotanikaBeautyTests.components.UIElement import UIElement as Element
from Internship.BotanikaBeautyTests.components.actions import Actions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Internship.BotanikaBeautyTests.components.browser import Browser


import time

class AddToCartBtnOnPopup:
    def __init__(self, browser):
        self.actions = Actions(browser)
        self.navbar = NavigationBar(browser)

        self.cart_btn_on_popup = Element(browser, By.XPATH, "//button[@class='btn btn-theme gradient-theme qv-add-button']")
        self.close_button = Element(browser, By.XPATH, "//div[@id='jsQuickview']/div/div/div/button/i")
        self.amount_of_product = Element(browser, By.XPATH, "//input[@class = 'qv-quantity']")

        self.increase_product_amount = Element(browser, By.XPATH, "//div[@class = 'quantity']")
        self.cart_indicator = Element(browser, By.XPATH, "//span[@title='Shopping Cart']")

        self.arrow_up = Element(browser, By.XPATH, "//input[@class='qv-quantity']")



    def add_cart_btn_on_popup(self):
        return self.cart_btn_on_popup.click()

    def close(self):
        return self.close_button.click()

    def enter_text(self, text):
        return self.amount_of_product.enter_text(text)

    # def amount_by_typing(self):
    #     self.actions.move_to_element(self.arrow_up)
    #     self.actions.send_keys("Backspace")

    def arrow(self):
        self.increase_product_amount.click()

    def get_cart_indicator(self):
        return self.cart_indicator.get_text()

