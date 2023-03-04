import time

from behave import given, when, then
from Internship.BotanikaBeautyTests.utils.config_reader import ConfigReader
from Internship.BotanikaBeautyTests.components.browser import Browser
from Internship.BotanikaBeautyTests.pages.home_page import HomePage
from Internship.BotanikaBeautyTests.components.navigation_bar import NavigationBar
from Internship.BotanikaBeautyTests.pages.new_product_page import NewProductsPage

URL = "https://botanikabeauty.com/"
configs = ConfigReader("Internship/BotanikaBeautyTests/steps/config.ini")


@given("Botanikabeauty home page is launched")
def launch_botanikabeauty_homepage(context):
    browser = Browser(URL, configs.get_browser())
    context.browser = browser

@when("the user selects New Products from Shop Menu")
def select_new_products(context):
    home_page = HomePage(context.browser)
    home_page.show_new_products()



@then("The available new products are displayed")
def verify_new_products_availability(context):
    time.sleep(3)
    new_product_page = NewProductsPage(context.browser)
    print(new_product_page.get_shampoo_title())
    assert new_product_page.get_shampoo_title() == "THE CLEANSER HYDRATING SHAMPOO"
    assert new_product_page.get_conditioner_title() == "THE MANAGER SILKENING CONDITIONER"
    print(new_product_page.get_trio_bundle_title())
    assert new_product_page.get_trio_bundle_title() == "TRIO BUNDLE: THE MANAGER, LIFTER & CLEANSER"
    assert new_product_page.get_spray_title() == "THE LIFTER VOLUMIZER SPRAY"

