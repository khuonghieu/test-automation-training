import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from pom.base_page import BasePage
from res.testdata import TestData


class PaymentModal(BasePage):

    PAYMENT_MODAL = (By.CSS_SELECTOR, "#modal-payment-subscription-engine")
    CHOOSE_ANOTHER_METHOD = (By.CSS_SELECTOR, ".braintree-large-button.braintree-toggle")
    CARD_OPTION = (By.CSS_SELECTOR, ".braintree-option.braintree-option__card")
    PAYPAL_OPTION = (By.CSS_SELECTOR, ".braintree-option.braintree-option__paypal")

    def __init__(self, driver):
        super().__init__(driver)

    def show_all_payment_methods(self):
        try:
            if self.is_visible(self.CHOOSE_ANOTHER_METHOD):
                self.click(self.CHOOSE_ANOTHER_METHOD)
                time.sleep(1)
            else:
                pass
        except TimeoutException:
            pass

    def choose_card_option(self):
        self.click(self.CARD_OPTION)
