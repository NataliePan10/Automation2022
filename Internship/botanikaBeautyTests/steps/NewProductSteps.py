from behave import given, when, then

@given("a web browser is at the Botanikabeauty home page")
def launch_botanikabeauty_homepage(context):
    print("launch_botanikabeauty_homepage")


@when("user selects New Products from Shop Menu")
def select_new_products(context):
    print("select_new_products")


@then("available new products are displayed")
def verify_new_products_availability(context):
    print("verify_new_products_availability")