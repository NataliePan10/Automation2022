from selenium import webdriver
from selenium.webdriver.support.color import Color

driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window
logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

email_input = driver.find_element_by_id("input-email")
email_input.clear()
email_input.send_keys ("atulkanata@gmail.com")

password_input = driver.find_element_by_id("input-password")
password_input.clear()
password_input.send_keys ("160486")

login_btn = driver.find_element_by_xpath("//a[contains(text(),'Login')]")
login_btn.click()
driver.quit()