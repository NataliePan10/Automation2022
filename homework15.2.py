from selenium import webdriver
from selenium.webdriver.support.color import Color

driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window
logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

new_registrant_btn = driver.find_element_by_xpath("//a[contains(text(),'Continue')]")

#getting the background color of the button
backround_color = new_registrant_btn.value_of_css_property("background-color")
converted_background_color = Color.from_string(backround_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'

new_registrant_btn.click()

firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class

firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.clear()
firstname_input.send_keys("Natalia")

lastname_field = driver.find_element_by_xpath("//fieldset/div[2]")
lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class

lastname_input = driver.find_element_by_id("input-lastname")
lastname_input.clear()
lastname_input.send_keys("Pan")

email_field = driver.find_element_by_xpath("//fieldset/div[2]")
email_field_class = email_field.get_attribute("class")
assert "required" in email_field_class
email_input = driver.find_element_by_id("input-email")
email_input.clear()
email_input.send_keys ("atulkanata@gmail.com")

telephone_field = driver.find_element_by_xpath("//fieldset/div[2]")
telephone_field_class = telephone_field.get_attribute("class")
assert "required" in telephone_field_class
telephone_input = driver.find_element_by_id("input-telephone")
telephone_input.clear()
telephone_input.send_keys("8502387503")


address_1_field = driver.find_element_by_xpath("//fieldset/div[2]")
address_1_field_class = email_field.get_attribute("class")
assert "required" in address_1_field_class
address_1_input = driver.find_element_by_id("input-address-1")
address_1_input.clear()
address_1_input.send_keys ("8700 front beach road unit 1212")


city_field = driver.find_element_by_xpath("//fieldset/div[2]")
city_field_class = city_field.get_attribute("class")
assert "required" in city_field_class
city_input = driver.find_element_by_id("input-city")
city_input.clear()
city_input.send_keys ("Panama City Beach")



password_field = driver.find_element_by_xpath("//fieldset/div[2]")
password_field_class = password_field.get_attribute("class")
assert "required" in password_field_class
password_input = driver.find_element_by_id("input-password")
password_input.clear()
password_input.send_keys ("160486")


password_confirm_field = driver.find_element_by_xpath("//fieldset/div[2]")
password_confirm_field_class = password_confirm_field.get_attribute("class")
assert "required" in password_confirm_field_class
password_confirm_input = driver.find_element_by_id("input-confirm")
password_confirm_input.clear()
password_confirm_input.send_keys ("160486")

driver.quit()





