from selenium import webdriver
import unittest
from res.testdata import TestData
from selenium.webdriver.chrome.options import Options
from pom import card_payment


class TestCardPayment(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path='../drivers/chromedriver',
                                       options=chrome_options)
        self.card_payment = card_payment(self.driver)

    def test_card_payment_form_is_displayed(self):
        assert self.card_payment.is_enabled(card_payment.CARD_FORM)

    def test_pay_btn_is_displayed(self):
        assert self.card_payment.is_enabled(card_payment.PAY_BTN)

    def test_valid_card(self):
        self.card_payment.fill_card_information(TestData.SUCCESSFUL_TRANSACTION_CARD)
        assert self.card_payment.card_info_is_valid()

    def test_incomplete_card_number(self):
        self.card_payment.fill_card_component_frame(card_payment.CARD_NUM_FRAME,
                                                    card_payment.CARD_NUMBER_INPUT,
                                                    TestData.INCOMPLETE_CARD_NUMBER)
        self.card_payment.fill_card_component_frame(card_payment.CVV_FRAME,
                                                    card_payment.CARD_CVV_INPUT,
                                                    "123")
        assert not self.card_payment.card_info_is_valid()

    def test_incomplete_card_date(self):
        self.card_payment.fill_card_component_frame(card_payment.EXP_DATE_FRAME,
                                                    card_payment.CARD_DATE_INPUT,
                                                    TestData.INCOMPLETE_CARD_DATE)
        assert not self.card_payment.card_info_is_valid()

    def test_incomplete_card_cvv(self):
        self.card_payment.fill_card_component_frame(card_payment.CVV_FRAME,
                                                    card_payment.CARD_CVV_INPUT,
                                                    TestData.INCOMPLETE_CARD_CVV)
        assert not self.card_payment.card_info_is_valid()

    def test_incomplete_card_postal(self):
        self.card_payment.fill_card_component_frame(card_payment.POSTAL_FRAME,
                                                    card_payment.CARD_POSTAL_INPUT,
                                                    TestData.INCOMPLETE_CARD_POSTAL)
        assert not self.card_payment.card_info_is_valid()

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
