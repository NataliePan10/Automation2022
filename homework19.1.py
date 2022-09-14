from selenium import webdriver

#imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path='drivers/chromedriver')

driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()

#logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

wd_wait = WebDriverWait(driver, 10)
logo = wd_wait.until(EC. element_to_be_clickable(
                                (By.XPATH, "//img[@title='Brainbucket']")))

new_registrant_btn = driver.find_element_by_xpath("//a[contains(text(), 'Continue')]")
new_registrant_btn.click()

time.sleep(5)

#Register Account
#Personal Details
#firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
#firstname_field_class = firstname_field.get_attribute("class")
#assert "required" in firstname_field_class

#firstname_input = driver.find_element_by_id("input-firstname")
#firstname_input.clear()
#firstname_input.send_keys("Lana")

driver.quit()