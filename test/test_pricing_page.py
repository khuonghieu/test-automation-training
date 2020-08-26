import time

from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options


class PricingPage(unittest.TestCase):
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
        self.pricing_btn = self.driver.find_element_by_xpath("//a[@id='pricing-navlink-landing']")

    def test_pricing_btn_is_displayed(self):
        assert self.pricing_btn.is_displayed()

    def test_individual_and_small_business_btn_is_chosen(self):
        self.pricing_btn.click()
        individual_small_business_btn = self.driver.find_element_by_xpath(
            "//button[@class='gi-coverPricing-Tab-Item is-active test-invididuals-tab']")
        assert individual_small_business_btn.is_enabled()

    def test_subscription_btn_is_displayed(self):
        self.pricing_btn.click()
        subscription = self.driver.find_element_by_xpath("//button[contains(text(),'TRY FOR FREE')]")
        assert subscription.is_displayed()

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
