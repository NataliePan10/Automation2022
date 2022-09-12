from selenium import webdriver

#imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.supporfrom selenium import webdriver

driver = webdriver.Chrome(executable_path='drivers/chromedriver')
# to start Firefox use the line below
#driver = webdriver.Firefox(executable_path='drivers/geckodriver')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()

#logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

wd_wait = WebDriverWait(driver, 10)
logo = wd_wait.until(EC.visibility_of_element_located(
                                (By.XPATH, "//img[@title='Brainbucket']")))

new_registrant_btn = driver.find_element_by_xpath("//a[contains(text(), 'Continue')]")
new_registrant_btn.click()

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

#navigate privacy policy

privacy_policy = driver.find_element_by_xpath("//input[@type='checkbox'and @ name='agree' and @value='1']")
privacy_policy.click()

#navigate to subscription


subscribe_btn = driver.find_element_by_xpath("//input[@name='newsletter' and @value='0']")

subscribe_btn.click()






time.sleep(5)

driver.quit()