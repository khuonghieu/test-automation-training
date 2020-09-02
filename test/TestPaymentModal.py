from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options
from pom import PaymentModal


class TestPaymentModal(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="../../test-automation-training/drivers/chromedriver",
                                       options=chrome_options)
        self.payment_modal = PaymentModal(self.driver)

    def test_payment_modal_is_displayed(self):
        assert self.payment_modal.is_enabled(PaymentModal.PAYMENT_MODAL)

    def test_card_option_is_displayed(self):
        self.payment_modal.show_all_payment_methods()
        assert self.payment_modal.is_enabled(PaymentModal.CARD_OPTION)

    def test_paypal_option_is_displayed(self):
        self.payment_modal.show_all_payment_methods()
        assert self.payment_modal.is_enabled(PaymentModal.PAYPAL_OPTION)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
