from behave import given, when, then

from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


#URL = "https://techskillacademy.net/brainbucket/index.php?route=account/login"
#configs = ConfigReader("BrainBucketTests/BDDBehave/logintests/steps/config.ini")

@given("User launched login page")
def launch_login_page(context):
    browser = Browser(URL, configs.get_browser(), configs.get_wait_time())
    context.browser = browser

@given("User is not logged in")
def verify_user_not_logged_in(context):
    login_page = LoginPage(context.browser)
    assert login_page.get_new_customer_title() == "New Customer"
    assert login_page.get_returning_customer_title() == "Returning Customer"
    context.login_page = login_page


@when("user enters email and password")
def enter_email_and_password(context):
    # login_page = context.login_page
    # configs = context.configs
    # login_page.enter_email(configs.get_user1_email())
    # login_page.enter_password(configs.get_user1_password())
    context.execute_steps(
        """
        When user enters email
        When user enters password
        """
    )


@when('user clicks Login button')
def click_login_button(context):
    login_page = context.login_page
    login_page.click_login_button()


@then("The user\'s profile page will be launched")
def verify_user_profile_view(context):
    profile_page = ProfilePage(context.browser)
    assert profile_page.get_my_account_title() == "My Account"
    assert profile_page.get_my_orders_title() == "My Orders"
    assert profile_page.get_newsletter_title() == "Newsletter"


@when("user enters email")
def enter_email(context):
    login_page = context.login_page
    login_page.enter_email(context.configs.get_user_email())


@when("user enters password")
def enter_passowrd(context):
    login_page = context.login_page
    login_page.enter_password(context.configs.get_user_password())


@then("warning is shown No match for E-Mail Address and/or Password")
def verify_warning(context):
    print("verify_warning")