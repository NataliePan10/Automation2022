from behave import given, when, then
from Internship.BotanikaBeautyTests.utils.config_reader import ConfigReader
from Internship.BotanikaBeautyTests.components.browser import Browser
from Internship.BotanikaBeautyTests.pages.home_page import HomePage
from Internship.BotanikaBeautyTests.components.navigation_bar import NavigationBar
from Internship.BotanikaBeautyTests.pages.new_product_page import NewProductsPage
from Internship.BotanikaBeautyTests.components.UIElement import UIElement as Element
from Internship.BotanikaBeautyTests.pages.popup import AddToCartBtnOnPopup
from selenium.webdriver.common.keys import Keys
import time



URL = "https://botanikabeauty.com/"
configs = ConfigReader("Internship/BotanikaBeautyTests/steps/config.ini")


@when("user clicks 'Add to cart' button")
def click_add_to_cart_button(context):
    new_product_page = NewProductsPage(context.browser)
    new_product_page.add_to_cart("The Cleanser Hydrating Shampoo")




@then("product is added to the cart")
def verify_new_product_added_to_the_cart(context):
    new_product_page = NewProductsPage(context.browser)
    #print("ASSERTION GET_CART_TITLE")
    #assert new_product_page.get_cart_title() == "Item(s) added to cart.The Cleanser Hydrating Shampoo x 1"
    new_product_page.cart_indicator.click()
    print("PRODUCT_INDICATOR")
    assert new_product_page.get_product_indicator() == "The Cleanser Hydrating Shampoo"
    print(new_product_page.get_cart_indicator())
    assert context.amount in new_product_page.get_cart_indicator()



@then("correct amount of new products are added to the cart")
def verify_correct_amount_of_new_products(context):
    new_product_page = NewProductsPage(context.browser)
    print("ASSERTION GET_CART_INDICATOR")
    assert new_product_page.get_cart_indicator() == "1"



@when('user clicks "Quickshop" button')
def click_quickshop(context):
    new_product_page = NewProductsPage(context.browser)
    new_product_page.quickshop("The Cleanser Hydrating Shampoo")



@when('user clicks "Add to cart" btn on popup')
def click_add_to_cart_btn_on_popup(context):
    popup = AddToCartBtnOnPopup(context.browser)
    popup.add_cart_btn_on_popup()
    popup.close()
    # new_product_page = NewProductsPage(context.browser)
    # new_product_page.add_to_cart_btn_on_popup()
    # new_product_page.close_button()




@when("user types amount of new products")
def amt_of_new_product(context):
     popup = AddToCartBtnOnPopup(context.browser)
     #new_product_page = NewProductsPage(context.browser)

     popup.enter_text("5")
     context.amount = "5"
     # print("ASSERTION GET_CART_INDICATOR")
     # assert popup.get_cart_indicator() == "5"

     #new_product_page.amount_of_new_product("5")


@when("user increases quantity of new products")
def increase_of_new_product(context):
    popup = AddToCartBtnOnPopup(context.browser)
    popup.amount_by_typing()
    popup.arrow()
    #new_product_page = NewProductsPage(context.browser)
    #print("ASSERTION GET_CART_INDICATOR")
    #assert popup.get_cart_indicator() == "2"
    popup.close()

# @when("user clicks 'Add to cart' button")
# def click_add_to_cart_button(context):
#     new_product_page = NewProductsPage(context.browser)
#     new_product_page.add_to_cart("The Cleanser Hydrating Shampoo")

















