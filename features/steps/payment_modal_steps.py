from pom.payment_modal import PaymentModal
from behave import *
from res.testdata import TestData


@given('User is logged in and clicks on Subscription Button')
def user_opens_payment_modal(context):
    context.payment_modal = PaymentModal(context.browser)
    context.payment_modal.login(TestData.LOGIN_SUCCESS_ACCOUNT["USERNAME"],
                                TestData.LOGIN_SUCCESS_ACCOUNT["PASSWORD"])
    context.payment_modal.choose_subscription_option()


@then('User should see payment modal')
def payment_modal_is_displayed(context):
    assert context.payment_modal.is_enabled(PaymentModal.PAYMENT_MODAL)


@then('User should see card payment option')
def card_option_is_displayed(context):
    context.payment_modal.show_all_payment_methods()
    assert context.payment_modal.is_enabled(PaymentModal.CARD_OPTION)


@then('User should see Paypal payment option')
def paypal_option_is_displayed(context):
    assert context.payment_modal.is_enabled(PaymentModal.PAYPAL_OPTION)
