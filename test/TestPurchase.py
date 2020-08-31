import time
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options
from res.pages.CardPayment import CardPayment
from res.testdata import TestData


class TestPurchase(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="../../test-automation-training/drivers/chromedriver",
                                       options=chrome_options)
        self.purchase = CardPayment(self.driver)

    def test_fail_transaction(self):
        self.purchase.fill_card_information(TestData.FAIL_TRANSACTION_CARD)
        self.purchase.click(CardPayment.PAY_BTN)
        assert self.purchase.is_enabled(CardPayment.PAYMENT_FAIL_MESSAGE)

    def test_success_transaction(self):
        self.purchase.fill_card_information(TestData.SUCCESSFUL_TRANSACTION_CARD)
        self.purchase.click(CardPayment.PAY_BTN)
        time.sleep(10)
        self.purchase.assert_element_text(CardPayment.SESSION_BALANCE, "unlimited")

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
