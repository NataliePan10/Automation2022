from behave import given, when, then
from Internship.BotanikaBeautyTests.utils.config_reader import ConfigReader
from Internship.BotanikaBeautyTests.components.browser import Browser
from Internship.BotanikaBeautyTests.pages.home_page import HomePage
from Internship.BotanikaBeautyTests.components.navigation_bar import NavigationBar
from Internship.BotanikaBeautyTests.pages.new_product_page import NewProductsPage


URL = "https://botanikabeauty.com/"
configs = ConfigReader("Internship/BotanikaBeautyTests/steps/config.ini")


@when("user clicks 'Add to cart' button")
def click_add_to_cart_button(context):
    new_product_page = NewProductsPage(context.browser)
    new_product_page.add_to_cart("The Cleanser Hydrating Shampoo")




@then("new product is added to the cart")
def verify_new_product_added_to_the_cart(context):
    new_product_page = NewProductsPage(context.browser)
    assert new_product_page.get_cart_title() == "Item(s) added to the cart"


@then("correct amount of new products are added to the cart")
def verify_correct_amount_of_new_products(context):
    new_product_page = NewProductsPage(context.browser)
    assert new_product_page.get_cart_indicator() == "1"



@when("user types amount of new products")
def amount_of_new_product(context):
    new_product_page = NewProductsPage(context.browser)
    new_product_page.shampoo()
    new_product_page.quickshop()
    new_product_page.amount_of_new_product("5")


@when("user clicks quantity of new products")
def quantity_of_new_product(context):
    new_product_page = NewProductsPage(context.browser)
    new_product_page.shampoo()
    new_product_page.quickshop()
    new_product_page.increase_product_amount()
    assert new_product_page.get_cart_indicator() == "2"


# @when("user clicks 'Add to cart' button")
# def click_add_to_cart_button(context):
#     new_product_page = NewProductsPage(context.browser)
#     new_product_page.add_to_cart("The Cleanser Hydrating Shampoo")

















