
from webelements.UIElements import UIElement as Element
from selenium.webdriver.common.by import By


class RightMenu:
    def __init__(self, browser):
        self.login_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[1]")
        self.registration_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[2]")
        self.forgotten_password_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[3]")
        self.my_account_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[4]")

        self.address_book_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[5]")
        self.wishlist_btn = Element(browser, By.XPATH, "//*[@id='column-right']//a[6]")
        self.order_history_btn = Element("//*[@id='column-right']//a[7]")
        self.downloads_btn = Element("//*[@id='column-right']//a[8]")
        self.recurring_payments_btn = Element("//*[@id='column-right']//a[9]")
        self.reward_points_btn = Element("//*[@id='column-right']//a[10]")
        self.returns_btn = Element("//*[@id='column-right']//a[11]")
        self.transactions_btn = Element("//*[@id='column-right']//a[12]")
        self.newsletter_btn = Element("//*[@id='column-right']//a[13]")

    def click_login(self):
        self.login_btn.click()