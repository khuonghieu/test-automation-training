import time
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options
from res.pages.CardPayment import CardPayment
from res.testdata import TestData
from res.locators import Locators


class TestPurchase(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.purchase = CardPayment(self.driver)

    def test_fail_transaction(self):
        self.purchase.fill_card_information(TestData.FAIL_TRANSACTION_CARD)
        self.purchase.click(Locators.PAY_BTN)
        assert self.purchase.is_enabled(Locators.PAYMENT_FAIL_MESSAGE)

    def test_success_transaction(self):
        self.purchase.fill_card_information(TestData.SUCCESSFUL_TRANSACTION_CARD)
        self.purchase.click(Locators.PAY_BTN)
        time.sleep(15)
        self.purchase.assert_element_text(Locators.SESSION_BALANCE, "unlimited")


if __name__ == '__main__':
    unittest.main()
