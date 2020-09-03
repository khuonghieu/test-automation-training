from pom.pricing_page import PricingPage
from behave import *


@given('User is already logged in and on Pricing page')
def user_loads_pricing_page(context):
    context.pricing_page = PricingPage(context.browser)
    assert context.pricing_page.is_present()


@then('User should see pricing button')
def pricing_btn_is_displayed(context):
    assert context.pricing_page.is_enabled(PricingPage.PRICING_BTN)


@then('User should see Individual and Small Business Button')
def individual_and_small_business_btn_is_chosen(context):
    assert context.pricing_page.is_enabled(PricingPage.INDIVIDUAL_SMALL_BUSINESS_BTN)


@then('User should see Subscription Button')
def subscription_btn_is_displayed(context):
    assert context.pricing_page.is_enabled(PricingPage.SUBSCRIPTION_BTN)
