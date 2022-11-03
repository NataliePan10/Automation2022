from webelements.browser import Browser
from webelements.UIElements import UIElement as Element
from selenium.webdriver.common.by import By
import time

URL = "http://cleveronly.com/practice/"

def test_simple_alert():
    browser = Browser(URL)
    alert_btn = Element(browser, By.XPATH, "//button[@onclick='openAlert()]")
    alert_btn.click()

    alert = browser.get_driver().swith_to.alert
    time.sleep(2)
    alert.accept()
    time.sleep(2)

    browser.shutdown()

def test_confirmation_alert():
    browser = Browser(URL)
    confirmation_btn = Element(browser, By.XPATH, "//button[@onclick='openConfirmationAlert()]")
    confirmation_btn.click()

    alert = browser.get_driver().swith_to.alert
    time.sleep(2)
    alert.dismiss()

    time.sleep(2)
    msg = Element(browser, By.ID, 'msg')
    assert msg.get_text() == "You pressed CANCEL!"

    confirmation_btn.click()
    alert.accept()

    assert msg.get_text() == "You pressed OK!"

    browser.shutdown()


def test_prompt_alert():
    browser = Browser(URL)
    prompt_btn = Element(browser, By.XPATH, "//button[@onclick='openPrompt()]")

    prompt_btn.click()

    alert = browser.get_driver().switch_to_alert()

    time.sleep(2)
    name = "Natalia"
    alert.send_keys(name)
    alert.accept()

    msg = "Hello{}! How are you today?".format(name)
    prompt_msg = Element(browser, By.ID, "demo")
    assert prompt_msg.get_text() == msg

    browser.shutdown()


def test_iframe():
    browser = Browser(URL)
    iframe = Element(browser, By.TAG_NAME, 'iframe')
    browser.get_driver().switch_to.frame(iframe.get_element())

    time.sleep(2)
    Element(browser, By.ID, "intro_logo").wait_until_visible()

    browser.get_driver().switch_to.default_content()
    browser.shutdown()


if __name__ == "__main__":
    test_simple_alert()
    test_confirmation_alert()
    test_confirmation_alert()
    test_iframe()


