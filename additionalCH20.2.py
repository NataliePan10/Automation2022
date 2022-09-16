
from selenium import webdriver
from webelements.browser import Browser
from webelements.UIElements import UIElement as Element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from pyCharmProjects.dropdown import Dropdown
from webelements.checkbox import Checkbox
browser = Browser("https://cleveronly.com/brainbucket/index.php?route=account/register")
driver = browser.get_driver()

wd_wait = browser.get_wd_wait()
wd_wait.until

driver.maximize_window()

#firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
firstname_field = Element(browser, By.XPATH, '//fieldset/div[2]')


#firstname_input = driver.find_element_by_id("input-firstname")
firstname_input = Element(browser, By.ID, 'input-firstname')
firstname_input.enter_text("Natalia")

#lastname_field = driver.find_element_by_xpath("//fieldset/div[2]")
lastname_field = Element(browser, By. XPATH, '//fieldset/div[2]')
lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class

#lastname_input = driver.find_element_by_id("input-lastname")
lastname_input = Element(browser, By. ID, 'input-lastname')
lastname_input.enter_text("Pan")

#email_field = driver.find_element_by_xpath("//fieldset/div[2]")
email_field = Element(browser, By.XPATH, '//fieldset/div[2]')
email_field_class = email_field.get_attribute("class")
assert "required" in email_field_class
#email_input = driver.find_element_by_id("input-email")
email_input = Element(browser, By.ID, 'input-email')

email_input.enter_text("atulkanata@gmail.com")

#telephone_field = driver.find_element_by_xpath("//fieldset/div[2]")
telephone_field = Element(browser, By.XPATH, '//fieldset/div[2]')
telephone_field_class = telephone_field.get_attribute("class")
assert "required" in telephone_field_class
#telephone_input = driver.find_element_by_id("input-telephone")
telephone_input = Element(browser, By.ID, 'input-telephone')
telephone_input.enter_text("8502387503")


#address_1_field = driver.find_element_by_xpath("//fieldset/div[2]")
address_1_field = Element(browser, By.XPATH, '//fieldset/div[2]')
address_1_field_class = email_field.get_attribute("class")
assert "required" in address_1_field_class
#address_1_input = driver.find_element_by_id("input-address-1")
address_1_input = Element(browser, By. ID, 'input-address-1')
address_1_input.enter_text("8700 front beach road unit 1212")


#city_field = driver.find_element_by_xpath("//fieldset/div[2]")
city_field = Element(browser, By.XPATH, '//fieldset/div[2]')
city_field_class = city_field.get_attribute("class")
assert "required" in city_field_class
#city_input = driver.find_element_by_id("input-city")
city_input = Element(browser, By. ID, 'input-city')
city_input.enter_text("Panama City Beach")



#password_field = driver.find_element_by_xpath("//fieldset/div[2]")
password_field = Element(browser, By.XPATH, '//fieldset/div[2]')
password_field_class = password_field.get_attribute("class")
assert "required" in password_field_class
#password_input = driver.find_element_by_id("input-password")
password_input = Element(browser, By.ID, 'input-password')
password_input.enter_text("160486")


#password_confirm_field = driver.find_element_by_xpath("//fieldset/div[2]")
password_confirm_field = Element(browser, By.XPATH, '//fieldset/div[2]')
password_confirm_field_class = password_confirm_field.get_attribute("class")
assert "required" in password_confirm_field_class
#password_confirm_input = driver.find_element_by_id("input-confirm")
password_confirm_input = Element(browser, By.ID, 'input-confirm')
password_confirm_input.enter_text("160486")

time.sleep(2)


#select=Select(driver.find_element_by_id("input-zone"))
select = Dropdown(browser, By.ID, 'input-zone').select_by_text("Florida")

#navigate privacy policy

privacy_policy = driver.find_element_by_xpath("//input[@type='checkbox'and @ name='agree' and @value='1']")
privacy_policy.click()

#navigate to subscription


#subscribe_btn = driver.find_element_by_xpath("//input[@name='newsletter' and @value='0']")
subscribe_btn = Checkbox(browser, By.XPATH, "//input[@name='newsletter' and @value='0']").click()



time.sleep(5)

driver.quit()