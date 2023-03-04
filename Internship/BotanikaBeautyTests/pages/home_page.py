from Internship.BotanikaBeautyTests.components.navigation_bar import NavigationBar
from Internship.BotanikaBeautyTests.components.browser import Browser
from Internship.BotanikaBeautyTests.components.UIElement import UIElement as Element


class HomePage:
    def __init__(self, browser):
        self.navbar = NavigationBar(browser)


    def show_new_products(self):
        self.navbar.show_new_products()




