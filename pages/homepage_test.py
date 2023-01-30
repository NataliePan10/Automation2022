from pages.home_page import HomePage
from webelements.browser import Browser
from webelements.UIElements import UIElement as Element
from selenium.webdriver.common.by import By

URL = "https://cleveronly.com/brainbucket"


def test_opening_all_desktops():
    browser = Browser(URL)
    home_page = HomePage(browser)
    home_page.show_all_desktops()

    section_title = Element(browser, By.XPATH, "//*[@id='content']/h2").get_text()

    assert section_title == "Desktops"

    browser.shutdown()

if __name__ == "__main__":
    test_opening_all_desktops()
    
