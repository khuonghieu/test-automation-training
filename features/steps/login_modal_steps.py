from pom.LoginModal import LoginModal
from behave import *
from res.testdata import TestData


@given('User is on Login Modal')
def user_loads_login_modal(context):
    context.login_modal = LoginModal(context.browser)


@when('User fills in valid username and password')
def user_fills_valid_account(context):
    context.login_modal.login(TestData.LOGIN_SUCCESS_ACCOUNT["USERNAME"], TestData.LOGIN_SUCCESS_ACCOUNT["PASSWORD"])


@when('User fills in invalid username and password')
def user_fills_invalid_account(context):
    context.login_modal.login(TestData.LOGIN_FAIL_ACCOUNT["USERNAME"], TestData.LOGIN_FAIL_ACCOUNT["PASSWORD"])


@then('User should see the account button on the navbar')
def successful_login(context):
    assert context.login_modal.is_enabled(LoginModal.NAVBAR_ACCOUNT)


@then('User should see log in error message')
def fail_login(context):
    assert context.login_modal.is_enabled(LoginModal.LOGIN_ERROR_MESSAGE)
