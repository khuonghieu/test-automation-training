from pom import PaymentModal
from behave import *


@given('User is already logged in and clicks on Subscription Button to open payment modal')
def user_opens_payment_modal(context):
    context.payment_modal = PaymentModal(context.browser)


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
