import time
from pom.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from pom.login_modal import LoginModal
from pom.pricing_page import PricingPage
from res.testdata import TestData


class PaymentModal(BasePage):

    PAYMENT_MODAL = (By.CSS_SELECTOR, "#modal-payment-subscription-engine")
    CHOOSE_ANOTHER_METHOD = (By.CSS_SELECTOR, ".braintree-large-button.braintree-toggle")
    CARD_OPTION = (By.CSS_SELECTOR, ".braintree-option.braintree-option__card")
    PAYPAL_OPTION = (By.CSS_SELECTOR, ".braintree-option.braintree-option__paypal")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get_url(TestData.BASE_URL)

    def login(self, username, password):
        self.click(LoginModal.LOGIN_MODAL_BTN)
        self.enter_text(LoginModal.EMAIL_INPUT, username)
        self.enter_text(LoginModal.PASSWORD_INPUT, password)
        self.click(LoginModal.LOGIN_CONFIRM_BTN)

    def choose_subscription_option(self):
        self.driver.get_url(TestData.BASE_URL + 'pricing')
        self.driver.click(PricingPage.SUBSCRIPTION_BTN)

    def show_all_payment_methods(self):
        try:
            if self.is_visible(self.CHOOSE_ANOTHER_METHOD):
                self.click(self.CHOOSE_ANOTHER_METHOD)
                time.sleep(1)
            else:
                pass
        except TimeoutException:
            pass
