from webelements.browser import Browser
from webelements.UIElements import UIElement as Element
from webelements.alerts import Alerts
from webelements.iframe import Iframe
from selenium.webdriver.common.by import By

import time


URL = "http://cleveronly.com/practice/"

def test_simple_alert():
    browser = Browser(URL)
    alert_btn = Element(browser, By.XPATH, "//button[@onclick='openAlert()']")
    alert_btn.click()

    alert = Alerts(browser)
    time.sleep(2)
    alert.accept_alert()
    time.sleep(2)

    browser.shutdown()

def test_confirmation_alert():
    browser = Browser(URL)
    confirm_btn = Element(browser, By.XPATH, "//button[@onclick='openConfirmationAlert()']")
    confirm_btn.click()

    alert = Alerts(browser)
    time.sleep(2)
    alert.cancel_alert()

    time.sleep(2)
    msg = Element(browser, By. ID, 'msg')
    print(msg.get_text())
    assert msg.get_text() == "You pressed CANCEL!"


    confirm_btn.click()
    alert.accept_alert()
    print(msg.get_text())

    assert msg.get_text() == "You pressed OK!"

    browser.shutdown()

def test_prompt_alert():
    browser = Browser(URL)
    prompt_btn = Element(browser, By.XPATH, "//button[@onclick='openPrompt()']")
    prompt_btn.click()

    alert = Alerts(browser)

    time.sleep(2)
    name = "Natalie"
    alert.enter_text(name)
    alert.accept_alert()

    msg = "Hello {}! How are you today?".format(name)
    prompt_msg = Element(browser, By. ID, 'demo')
    print(prompt_msg.get_text())
    assert prompt_msg.get_text() == msg

    browser.shutdown()


def test_iframe():
    browser = Browser(URL)
    iframe = Iframe(browser)
    iframe.switch_to_iframe(iframe.get_element())

    time.sleep(2)
    Element(browser, By. ID, "intro logo").wait_until_visible()

    browser.switch_to_default_content()
    browser.shutdown()







if __name__ == "__main__":
    test_simple_alert()
    test_confirmation_alert()
    test_prompt_alert()
    #test_iframe()

