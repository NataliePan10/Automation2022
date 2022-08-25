
from selenium import webdriver

#imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(executable_path='drivers/chromedriver')

driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()

def select_from_dropdown(button_xpath, dropdown_xpath, option_xpath):
    dropdown_abc = driver.find_element_by_xpath(button_xpath)
    dropdown_abc.click()
    WebDriverWait(driver, 10)until(EC.visibility_of_element_located(
                                (By.XPATH, dropdown_xpath)))

    option = driver.find_element_by_xpath(option_xpath)
    option.click()



#logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

wd_wait = WebDriverWait(driver, 10)
logo = wd_wait.until(EC.visibility_of_element_located(
                                (By.XPATH, "//img[@title='Brainbucket']")))



select_from_dropdown("//span[contains(.,'My account')]", "//ul[@class=<ul class='dropdown-menu dropdown-menu-right']", "//a[contains(., 'Register')]")

#Register Account
#Personal Details
firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class

firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.clear()
firstname_input.send_keys("Natalia")

#select region/state
time.sleep(2)


select=Select(driver.find_element_by_id("input-zone"))
select.select_by_value('3630')

time.sleep(5)

driver.quit()