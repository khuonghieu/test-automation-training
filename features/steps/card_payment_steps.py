import random

from pom.card_payment import CardPayment
from behave import *
from res.testdata import TestData


@given('User clicks on Card Option to open Card Form')
def user_chooses_card_option(context):
    context.card_payment = CardPayment(context.browser)


@then('User should see Card Form')
def card_payment_form_is_displayed(context):
    assert context.card_payment.is_enabled(CardPayment.CARD_FORM)


@when("User fills in valid card information")
def fill_valid_card(context):
    context.card_payment.fill_card_information(TestData.SUCCESSFUL_TRANSACTION_CARD)


@then('User should see no error message')
def card_is_valid(context):
    assert context.card_payment.card_info_is_valid()


@when('User fills in incomplete card number')
def fill_incomplete_card_num(context):
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


@then('User should see an error message')
def card_error_message_is_shown(context):
    assert not context.card_payment.card_info_is_valid()
