from selenium import webdriver
from selenium.webdriver.support.color import Color

driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window
logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

new_registration_btn = driver.find_element_by_xpath("//a[contains(text(), 'Continue')]")

background_color = new_registration_btn.value_of_css_property("background-color")
converted_background_color = Color.from_string(background_color)
assert converted_background_color.rgb == 'rgb(34, 154, 200)'
new_registration_btn.click()


firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class

firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.clear()
firstname_input.send_keys("Nata")


driver.quit



#email_input = driver.find_element_by_id("input-email")