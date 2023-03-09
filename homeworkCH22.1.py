from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webelements.browser import Browser
from webelements.UIElements import UIElement as Element
from selenium.webdriver.common.keys import Keys
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
double_click_box_background_color = double_click_box.get_background_color()
assert double_click_box_background_color.rgb == 'rgb(255, 179, 128)'


actions = Actions(browser)
keydown_click_box = Element(browser, By.XPATH, "//input[@onkeydown='onEnter()']")
actions.send_keys_to_element(keydown_click_box, Keys.ENTER)
msg = Element(browser, By.ID, "hidden_text")
assert msg.get_text() == "You pressed the key!"


actions = Actions(browser)
context_menu_box = Element(browser, By.ID, "context_menu")
actions.right_click(context_menu_box)
change_color = Element(browser, By.XPATH, "//li[@onclick='changeColor()']")
change_color.click()
context_menu_box_background_color = context_menu_box.get_background_color()
assert context_menu_box_background_color.rgb == 'rgb(204, 255, 245)'


actions = Actions(browser)
context_menu_box = Element(browser, By.ID, "context_menu")
actions.right_click(context_menu_box)
change_font = Element(browser, By.XPATH, "//li[@onclick='changeFont()']")
change_font.click()
text_style = Element(browser, By.XPATH, "//div[@id='context_menu']/p")
context_menu_box_font_style = text_style.get_font_style()
print(context_menu_box_font_style)
assert context_menu_box_font_style == '"Source Sans Pro", Arial, Helvetica, sans-serif'


actions = Actions(browser)
context_menu_box = Element(browser, By.ID, "context_menu")
actions.right_click(context_menu_box)
open_cleveronly = Element(browser, By.XPATH, '//li[@class="menu-option"]/a')
original_window = browser.get_driver().current_window_handle
open_cleveronly.click()
browser.get_driver().switch_to.window(original_window)


actions = Actions(browser)
context_menu_box = Element(browser, By.ID, "context_menu")
actions.right_click(context_menu_box)
actions.send_keys(Keys.ESCAPE)
context_menu_close = Element(browser, By.XPATH, "//div[@class='menu']")
context_menu_close.wait_until_invisible()




#actions = Actions(browser)

#context_menu_box = Element(browser, By.XPATH, "//ul[@class='menu-option']")
#actions.right_click(context_menu_box).send_seys(Keys.ENTER).perform


