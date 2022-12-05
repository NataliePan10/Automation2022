#Homework CH 21 ex.2
from selenium import webdriver
from webelements.browser import Browser
from webelements.UIElements import UIElement as Element
from selenium.webdriver.common.by import By
from pages.registration_page import RegistrationPage


browser = Browser("https://cleveronly.com/brainbucket/index.php?route=account/register")
configs = ConfigReader("config.json")
driver = browser.get_driver()

wd_wait = browser.get_wd_wait()
wd_wait.until

driver.maximize_window()

def test_registration_through_dropdown():
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
    login_page = LoginPage(browser)
    login_page.open_registration_from_account_dropdown()

    registration_page = RegistrationPage(browser)
    assert registration_form.get_form_title() == 'Register Account'

    registration_page.enter_first_name("Natalia")
    registration_page.enter_last_name("Pan")
    registration_page.enter_email("atulkanata@gmail.com")
    registration_page.enter_telephone("850 238 7503")
    registration_page.enter_first_line_address("8700 Front Baech Road")
    registration_page.enter_city("Panama City Beach")
    registration_page.enter_postcode("32407")
    registration_page.enter_password("160486nata")
    registration_page.confirm_password_input("confirm")




driver.quit()
if __name__ == "__main__":
    test_registration_through_dropdown()