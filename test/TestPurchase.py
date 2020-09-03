import time
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options
from pom import card_payment
from res.testdata import TestData


class TestPurchase(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="../../test-automation-training/drivers/chromedriver",
                                       options=chrome_options)
        self.purchase = card_payment(self.driver)

    def test_fail_transaction(self):
        self.purchase.fill_card_information(TestData.FAIL_TRANSACTION_CARD)
        self.purchase.click(card_payment.PAY_BTN)
        assert self.purchase.is_enabled(card_payment.PAYMENT_FAIL_MESSAGE)

    def test_success_transaction(self):
        self.purchase.fill_card_information(TestData.SUCCESSFUL_TRANSACTION_CARD)
        self.purchase.click(card_payment.PAY_BTN)
        time.sleep(10)
        self.purchase.assert_element_text(card_payment.SESSION_BALANCE, "unlimited")

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
