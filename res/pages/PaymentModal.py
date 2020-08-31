import time

from res.pages.PricingPage import PricingPage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class PaymentModal(PricingPage):

    PAYMENT_MODAL = (By.CSS_SELECTOR,
                     "body.modal-open:nth-child(2) div.fade.in.modal:nth-child(2) div.modal-dialog div.modal-content "
                     "div.modal-body > div:nth-child(1)")
    CHOOSE_ANOTHER_METHOD = (By.CSS_SELECTOR,
                             "body.modal-open:nth-child(2) div.fade.in.modal:nth-child(2) div.modal-dialog "
                             "div.modal-content div.modal-body div:nth-child(2) div.braintree-show-methods "
                             "div.braintree-dropin.braintree-loaded:nth-child(2) "
                             "div.braintree-large-button.braintree-toggle:nth-child(7) > span:nth-child(1)")
    CARD_OPTION = (By.CSS_SELECTOR,
                   "body.modal-open:nth-child(2) div.fade.in.modal:nth-child(2) div.modal-dialog div.modal-content "
                   "div.modal-body div.braintree-show-methods.braintree-show-options "
                   "div.braintree-dropin.braintree-loaded:nth-child(2) "
                   "div.braintree-test-class.braintree-options:nth-child(6) "
                   "div.braintree-test-class.braintree-options.braintree-options-initial div.braintree-options-list > "
                   "div.braintree-option.braintree-option__card:nth-child(1)")
    PAYPAL_OPTION = (By.CSS_SELECTOR,
                     "body.modal-open:nth-child(2) div.fade.in.modal:nth-child(2) div.modal-dialog div.modal-content "
                     "div.modal-body div.braintree-show-methods.braintree-show-options "
                     "div.braintree-dropin.braintree-loaded:nth-child(2) "
                     "div.braintree-test-class.braintree-options:nth-child(6) "
                     "div.braintree-test-class.braintree-options.braintree-options-initial div.braintree-options-list "
                     "> div.braintree-option.braintree-option__paypal:nth-child(2)")

    def __init__(self, driver):
        super().__init__(driver)
        super().click(PricingPage.SUBSCRIPTION_BTN)

    def show_all_payment_methods(self):
        try:
            if self.is_visible(self.CHOOSE_ANOTHER_METHOD):
                self.click(self.CHOOSE_ANOTHER_METHOD)
            else:
                pass
            time.sleep(1)
        except TimeoutException:
            pass
