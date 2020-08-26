import time

from selenium import webdriver
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


class PaymentModal(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.got-it.io/solutions/excel-chat")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("test-login-button").click()
        self.driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("khuongletrunghieu1@gmail.com")
        self.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("Abc123!")
        self.driver.find_element_by_xpath("//button[@id='login-button']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//a[@id='pricing-navlink-landing']").click()
        self.driver.find_element_by_xpath("//button[contains(text(),'TRY FOR FREE')]").click()
        self.payment_modal = self.driver.find_element_by_xpath("//div[@class='modal-content']")

    def test_payment_modal_is_displayed(self):
        assert self.payment_modal.is_displayed()

    def test_card_option_is_displayed(self):
        choose_another_method_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Choose another way to pay')]")))
        if choose_another_method_btn.is_displayed():
            choose_another_method_btn.click()
        card_option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='braintree-option braintree-option__card']")))
        assert card_option.is_displayed()

    def test_paypal_option_is_displayed(self):
        choose_another_method_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Choose another way to pay')]")))
        if choose_another_method_btn.is_displayed():
            choose_another_method_btn.click()
        paypal_option = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='braintree-option braintree-option__paypal']")))
        assert paypal_option.is_displayed()

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
