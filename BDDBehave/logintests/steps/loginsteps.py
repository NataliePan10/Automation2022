from behave import given, when, then

""" 
    Given User launched login page
    Given User is not logged in
    When user enters email and password
    And user clicks Login button
    Then The user's profile page will be launched
    """

@given("user launch login page")
def launch_login_page(context):
    print("launch login page")

@given("user is not logged in")
def verify_user_not_logged_in(context):
    print("verify_user_not_logged_in")

@when("user enters email and password")
def enter_email_and_password(context):
    print("enter_email_and_password")

@when("user clicks Login button")
def click_login_button(context):
    print("click_login_button")

@then("The user's profile page will be launched")
def verify_user_profile_view(context):
    print("verify_user_profile_view")

