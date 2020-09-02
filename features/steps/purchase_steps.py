import time
from behave import *
from pom import CardPayment
from res.testdata import TestData


@given('User is on the Card Form')
def user_chooses_card_option(context):
    context.card_payment = CardPayment(context.browser)


@when('User fills in an invalid card')
def fill_invalid_card(context):
    context.purchase.fill_card_information(TestData.FAIL_TRANSACTION_CARD)


@when('User fills in a valid card')
def fill_valid_card(context):
    context.purchase.fill_card_information(TestData.SUCCESSFUL_TRANSACTION_CARD)


@when('User clicks Pay Now')
def click_pay_now_btn(context):
    context.purchase.click(CardPayment.PAY_BTN)


@then('User should see a failure message')
def fail_transaction(context):
    assert context.purchase.is_enabled(CardPayment.PAYMENT_FAIL_MESSAGE)


@then('User should see the session balance has been set to unlimited')
def successful_transaction(context):
    time.sleep(10)
    context.purchase.assert_element_text(CardPayment.SESSION_BALANCE, "unlimited")
