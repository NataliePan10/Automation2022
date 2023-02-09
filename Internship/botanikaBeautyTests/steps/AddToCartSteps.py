from behave import given, when, then

@given("a web browser is at the Botanikabeauty home page")
def launch_botanikabeauty_homepage(context):
  print("launch_botanikabeauty_homepage")


@when("user selects new product")
def select_new_product(context):
  print("select new product")


@when("user clicks 'Add to cart' button")
def click_add_to_cart_button(context):
  print("click 'Add to cart' button")


@then("new product is added to the cart")
def verify_new_product_added_to_the_cart(context):
  print("new product is added to the cart")








