from selenium.webdriver.common.action_chains import ActionChains
from webelements.browser import Browser
from webelements.UIElements import UIElement as Element
from selenium.webdriver.common.by import By

from webelements.dropdown import Dropdown
from webelements.actions import Actions
from selenium.webdriver.support.color import Color

# backround_color = new_registrant_btn.value_of_css_property("background-color")
# converted_background_color = Color.from_string(backround_color)
# assert converted_background_color.rgb == 'rgb(34, 154, 200)'


browser = Browser("https://cleveronly.com/practice/")
driver = browser.get_driver()

driver.maximize_window()



actions = Actions(browser)
double_click_box = Element(browser, By.ID, "card")
actions.double_click(double_click_box)

double_click_box_background_color = Color
assert double_click_box_background_color

keydown_click_box = Element(browser, By.ID, "key_practice")
actions.send_keys("enter")


