import time
from behave import *
from pom.card_payment import CardPayment
from res.testdata import TestData


@given('User is logged in')
def step_impl(context):
    context.purchase = CardPayment(context.browser)
    context.purchase.login(TestData.LOGIN_SUCCESS_ACCOUNT["USERNAME"],
                           TestData.LOGIN_SUCCESS_ACCOUNT["PASSWORD"])


@given('User chose subscription option')
def step_impl(context):
    context.purchase.choose_subscription_option()


@given('User is on Card Form')
def step_impl(context):
    context.purchase.show_all_payment_methods()
    context.purchase.choose_card_option()


@when('User fills in an invalid card')
def step_impl(context):
    context.purchase.fill_card_information(TestData.FAIL_TRANSACTION_CARD)


@when('User fills in a valid card')
def step_impl(context):
    context.purchase.fill_card_information(TestData.SUCCESSFUL_TRANSACTION_CARD)


@then('User should see Transaction Success Modal')
def step_impl(context):
    assert context.purchase.is_enabled(CardPayment.TRANSACTION_SUCCESS_MODAL)


@when('User clicks Pay Now')
def step_impl(context):
    context.purchase.click(CardPayment.PAY_BTN)
    time.sleep(10)


@then('User should see a failure message')
def step_impl(context):
    assert context.purchase.is_enabled(CardPayment.PAYMENT_FAIL_MESSAGE)
