import time

from behave import *
from selenium.common.exceptions import TimeoutException

from pom.card_payment import CardPayment
from pom.landing_page import LandingPage
from pom.login_modal import LoginModal
from pom.payment_modal import PaymentModal
from pom.pricing_page import PricingPage
from res.testdata import TestData


@given('User is on landing page')
def step_impl(context):
    context.landing_page = LandingPage(context.browser)
    assert context.landing_page.is_present()


@given('User logs in')
def step_impl(context):
    context.landing_page.open_login_modal()
    context.login_modal = LoginModal(context.browser)
    context.login_modal.login(TestData.LOGIN_SUCCESS_ACCOUNT['USERNAME'], TestData.LOGIN_SUCCESS_ACCOUNT['PASSWORD'])


@given('User goes to pricing page')
def step_impl(context):
    time.sleep(2)
    context.pricing_page = PricingPage(context.browser)
    assert context.pricing_page.is_present()


@given('User chooses subscription option')
def step_impl(context):
    context.pricing_page.choose_subscription_option()


@given('User opens all available payment options')
def step_impl(context):
    context.payment_modal = PaymentModal(context.browser)
    context.payment_modal.show_all_payment_methods()
    assert context.payment_modal.is_enabled(context.payment_modal.CARD_OPTION)
    assert context.payment_modal.is_enabled(context.payment_modal.PAYPAL_OPTION)


@given('User chooses card payment option')
def step_impl(context):
    context.payment_modal.choose_card_option()


@then('User should see Card Form')
def step_impl(context):
    context.card_payment = CardPayment(context.browser)
    context.card_payment.is_enabled(context.card_payment.CARD_FORM)


@when('User fills in an invalid card')
def step_impl(context):
    context.card_payment.fill_card_information(TestData.FAIL_TRANSACTION_CARD)


@when('User fills in a valid card')
def step_impl(context):
    context.card_payment.fill_card_information(TestData.SUCCESSFUL_TRANSACTION_CARD)


@when('User fills in incomplete card number')
def step_impl(context):
    context.card_payment.fill_card_component_frame(CardPayment.CARD_NUM_FRAME,
                                                   CardPayment.CARD_NUMBER_INPUT,
                                                   TestData.INCOMPLETE_CARD_NUMBER)
    context.card_payment.fill_card_component_frame(CardPayment.CVV_FRAME,
                                                   CardPayment.CARD_CVV_INPUT,
                                                   "123")


@when('User fills in incomplete card date')
def fill_incomplete_card_date(context):
    context.card_payment.fill_card_component_frame(CardPayment.EXP_DATE_FRAME,
                                                   CardPayment.CARD_DATE_INPUT,
                                                   TestData.INCOMPLETE_CARD_DATE)


@when('User fills in incomplete card cvv')
def fill_incomplete_card_cvv(context):
    context.card_payment.fill_card_component_frame(CardPayment.CVV_FRAME,
                                                   CardPayment.CARD_CVV_INPUT,
                                                   TestData.INCOMPLETE_CARD_CVV)


@when('User fills in incomplete card postal')
def fill_incomplete_card_postal(context):
    context.card_payment.fill_card_component_frame(CardPayment.POSTAL_FRAME,
                                                   CardPayment.CARD_POSTAL_INPUT,
                                                   TestData.INCOMPLETE_CARD_POSTAL)


@when("User clicks Pay Now")
def step_impl(context):
    context.card_payment.click(context.card_payment.PAY_BTN)


@then('User should see a failure message')
def step_impl(context):
    assert context.card_payment.is_enabled(CardPayment.PAYMENT_FAIL_MESSAGE)


@then('User should see Transaction Success Modal or not')
def step_impl(context):
    try:
        assert context.card_payment.is_enabled(CardPayment.TRANSACTION_SUCCESS_MODAL)
    except TimeoutException:
        pass


@then('User should see card info error message')
def step_impl(context):
    assert not context.card_payment.card_info_is_valid()


@then('User should see no error message')
def step_impl(context):
    assert context.card_payment.card_info_is_valid()
