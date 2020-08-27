from res.pages.PricingPage import PricingPage
from res.locators import Locators
from selenium.common.exceptions import TimeoutException


class PaymentModal(PricingPage):
    def __init__(self, driver):
        super().__init__(driver)
        super().click(Locators.SUBSCRIPTION_BTN)

    def show_all_payment_methods(self):
        try:
            if self.is_enabled(Locators.CHOOSE_ANOTHER_METHOD):
                self.click(Locators.CHOOSE_ANOTHER_METHOD)
            else:
                pass
        except TimeoutException:
            pass