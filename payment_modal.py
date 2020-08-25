import time

from selenium import webdriver
import unittest


class PaymentModal(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.got-it.io/solutions/excel-chat")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("test-login-button").click()
        self.driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("khuongletrunghieu1@gmail.com")
        self.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("Abc123!")
        self.driver.find_element_by_xpath("//button[@id='login-button']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@id='pricing-navlink-landing']").click()
        self.driver.find_element_by_xpath("//button[contains(text(),'TRY FOR FREE')]").click()
        self.payment_modal = self.driver.find_element_by_xpath("//div[@class='modal-content']")

    def test_payment_modal_is_displayed(self):
        assert self.payment_modal.is_displayed()

    def test_card_option_is_displayed(self):
        time.sleep(7)
        card_option = self.driver.find_element_by_xpath("//div[@class='braintree-option braintree-option__card']")
        assert card_option.is_displayed()

    def test_paypal_option_is_displayed(self):
        time.sleep(7)
        paypal_option = self.driver.find_element_by_xpath("//div[@class='braintree-option braintree-option__paypal']")
        assert paypal_option.is_displayed()

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
