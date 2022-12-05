from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pages.home_page import HomePage
from components.navigation_bar import NavigationBar
from webelements.browser import Browser
from webelements.UIElements import UIElement as Element
from selenium.webdriver.common.by import By

URL = "https://cleveronly.com/brainbucket"

def test_case_opening_PCs():
    browser = Browser("https://cleveronly.com/brainbucket")
    driver = browser.get_driver()

    driver.maximize_window()

    home_page = HomePage(browser)
    open_PCs = Element(browser, By.XPATH, "//a[contains(text(),'- PC (1)')]")
    home_page.show_pcs()
    Samsung = Element(browser, By.XPATH, "//a[contains(text(),'Samsung SyncMaster 941BW')]")
    assert Samsung.get_text() == "Samsung SyncMaster 941 BW available for sale"


if __name__ == "__main__":
    test_case_opening_PCs()

