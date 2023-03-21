import time

from Internship.BotanikaBeautyTests.components.browser import Browser
from Internship.BotanikaBeautyTests.components.UIElement import UIElement as Element
from Internship.BotanikaBeautyTests.components.actions import Actions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Internship.BotanikaBeautyTests.pages.new_product_page import NewProductsPage


browser = Browser("https://botanikabeauty.com/collections/new", "chrome")
got_btn = Element(browser, By.XPATH, "//button[@class='btn btn-theme js-btn-ok']")
got_btn.click()
new_product_page = NewProductsPage(browser)

time.sleep(5)





actions = Actions(browser)
spray = Element(browser, By.XPATH, "//a[contains(text(),'The Lifter Volumizer Spray')]")
actions.move_to_element(spray)
add_to_cart_under_shampoo = Element(browser, By.XPATH, "//span[@data-id='39670945120310']")
actions.move_to_element(add_to_cart_under_shampoo)
add_to_cart_under_shampoo.click()


cart_title = Element(browser, By.XPATH, "//div[@id='growls-default']")
                     #"//span[@class='js-cart-count site-header__cart-indicator']")
print(cart_title.get_text())


time.sleep(5)

browser.shutdown()
