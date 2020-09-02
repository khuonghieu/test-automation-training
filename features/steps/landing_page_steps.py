from behave import *
from pom.LandingPage import LandingPage



@given('User is on Landing Page')
def user_loads_landing_page(context):
    context.landing_page = LandingPage(context.browser)
    assert context.landing_page.is_present()


@when('User clicks on LogIn Modal Button')
def user_clicks_login_modal_btn(context):
    context.landing_page.click(LandingPage.LOGIN_MODAL_BTN)


@then('User should see LogIn Modal Button')
def login_button_is_displayed(context):
    assert context.landing_page.is_enabled(LandingPage.LOGIN_MODAL_BTN)


@then('User should see LogIn Modal')
def login_modal_is_displayed(context):
    assert context.landing_page.is_enabled(LandingPage.LOGIN_MODAL)