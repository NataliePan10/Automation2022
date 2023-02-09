from behave import given, when, then

@given("a web browser is at the Botanikabeauty home page")
def launch_botanikabeauty_homepage(context):
    print("launch_botanikabeauty_homepage")


@when("user selects new product")
def select_new_product(context):
    print("select new product")


@when("user clicks 'Add to cart' button as many times as needed")
def click_add_to_cart_button(context):
    print("click 'Add to cart' button")


@then("correct amount of new products are added to the cart")
def verify_correct_amount_of_new_product(context):
    print("correct amount of new products are added to the cart")