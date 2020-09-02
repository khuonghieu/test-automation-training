from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options
from pom import PricingPage


class TestPricingPage(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="../../test-automation-training/drivers/chromedriver",
                                       options=chrome_options)
        self.pricing_page = PricingPage(self.driver)

    def test_pricing_btn_is_displayed(self):
        assert self.pricing_page.is_enabled(PricingPage.PRICING_BTN)

    def test_individual_and_small_business_btn_is_chosen(self):
        assert self.pricing_page.is_enabled(PricingPage.INDIVIDUAL_SMALL_BUSINESS_BTN)

    def test_subscription_btn_is_displayed(self):
        assert self.pricing_page.is_enabled(PricingPage.SUBSCRIPTION_BTN)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
