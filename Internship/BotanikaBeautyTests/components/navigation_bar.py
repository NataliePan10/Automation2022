from Internship.BotanikaBeautyTests.components.UIElement import UIElement as Element
from selenium.webdriver.common.by import By
from Internship.BotanikaBeautyTests.components.actions import Actions
from Internship.BotanikaBeautyTests.components.dropdown import Dropdown


class NavigationBar:
    def __init__(self, browser):
        self.actions = Actions(browser)

        self.shop = Element(browser, By.XPATH, "//ul[@class='site-nav']/li[1]")
        self.new_product_dropdown = Element(browser, By.XPATH, "//div[@class='menu-title']/a[@href='/collections/new']")


    def show_new_products(self):
        self.actions.move_to_element(self.shop)
        self.new_product_dropdown.click()


