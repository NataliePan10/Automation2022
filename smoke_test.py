from selenium import webdriver
from selenium.webdriver.support.color import Color

driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window
logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

email_input = driver.find_element_by_id("input-email")