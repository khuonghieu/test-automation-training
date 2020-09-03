from pom.pricing_page import PricingPage
from behave import *
from res.testdata import TestData


@given('User is already logged in')
def user_loads_pricing_page(context):
    context.pricing_page = PricingPage(context.browser)
    context.pricing_page.login(TestData.LOGIN_SUCCESS_ACCOUNT["USERNAME"], TestData.LOGIN_SUCCESS_ACCOUNT["PASSWORD"])


@given('User go to Pricing page')
def step_impl(context):
    context.pricing_page.go_to_pricing_page()
    assert context.pricing_page.is_present()


@then('User should see pricing button')
def pricing_btn_is_displayed(context):
    assert context.pricing_page.is_enabled(context.pricing_page.PRICING_BTN)


@then('User should see Individual and Small Business Button')
def individual_and_small_business_btn_is_chosen(context):
    assert context.pricing_page.is_enabled(PricingPage.INDIVIDUAL_SMALL_BUSINESS_BTN)


@then('User should see Subscription Button')
def subscription_btn_is_displayed(context):
    assert context.pricing_page.is_enabled(PricingPage.SUBSCRIPTION_BTN)
