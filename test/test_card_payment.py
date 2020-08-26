import time

from selenium import webdriver
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


class CardPayment(unittest.TestCase):
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
        time.sleep(2)
        self.driver.find_element_by_xpath("//a[@id='pricing-navlink-landing']").click()
        self.driver.find_element_by_xpath("//button[contains(text(),'TRY FOR FREE')]").click()
        self.payment_modal = self.driver.find_element_by_xpath("//div[@class='modal-content']")

        choose_another_method_btn = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Choose another way to pay')]")))
        if choose_another_method_btn.is_displayed():
            choose_another_method_btn.click()
        card_option = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='braintree-option braintree-option__card']")))
        card_option.click()

        self.card_form = self.driver.find_element_by_xpath("//div[@class='braintree-card braintree-form "
                                                           "braintree-sheet']")
        self.card_num_frame = self.driver.find_element_by_xpath("//iframe[@id='braintree-hosted-field-number']")
        self.exp_date_frame = self.driver.find_element_by_xpath("//iframe[@id='braintree-hosted-field-expirationDate']")
        self.cvv_frame = self.driver.find_element_by_xpath("//iframe[@id='braintree-hosted-field-cvv']")
        self.postal_frame = self.driver.find_element_by_xpath("//iframe[@id='braintree-hosted-field-postalCode']")
        self.pay_btn = self.driver.find_element_by_xpath("//button[@class='gi-Button gi-Button--primary u-width-100']")
        self.error_message_list = self.driver.find_elements_by_class_name("braintree-form__field-error")

    def fill_card_number(self, card_number):
        self.driver.switch_to.frame(self.card_num_frame)
        self.driver.find_element_by_id("credit-card-number").send_keys(card_number)
        self.driver.switch_to.default_content()

    def fill_card_date(self, card_date):
        self.driver.switch_to.frame(self.exp_date_frame)
        self.driver.find_element_by_id("expiration").send_keys(card_date)
        self.driver.switch_to.default_content()

    def fill_card_cvv(self, card_cvv):
        self.driver.switch_to.frame(self.cvv_frame)
        self.driver.find_element_by_id("cvv").send_keys(card_cvv)
        self.driver.switch_to.default_content()

    def fill_card_postal(self, card_postal):
        self.driver.switch_to.frame(self.postal_frame)
        self.driver.find_element_by_id("postal-code").send_keys(card_postal)
        self.driver.switch_to.default_content()

    def test_card_payment_form_is_displayed(self):
        assert self.card_form.is_displayed()

    def test_pay_btn_is_displayed(self):
        assert self.pay_btn.is_displayed()

    def test_valid_card(self):
        self.fill_card_number("4009348888881881")
        self.fill_card_date("0522")
        self.fill_card_cvv("123")
        self.fill_card_postal("19123")
        # If all error fields are not displayed then the card was valid
        valid = True
        for message in self.error_message_list:
            valid = valid and (not message.is_displayed())
        assert valid

    def test_incomplete_card_number(self):
        self.fill_card_number("400934888888188")
        self.fill_card_date("0522")
        assert self.error_message_list[0].is_displayed()

    def test_incomplete_card_date(self):
        self.fill_card_date("5")
        self.fill_card_number("4009348888881881")
        assert self.error_message_list[1].is_displayed()

    def test_incomplete_card_cvv(self):
        self.fill_card_cvv("12")
        self.fill_card_date("0522")
        assert self.error_message_list[2].is_displayed()

    def test_incomplete_card_postal(self):
        self.fill_card_postal("")
        self.fill_card_cvv("123")
        assert self.error_message_list[3].is_displayed()

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
