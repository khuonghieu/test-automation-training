from selenium import webdriver
import unittest
from res.locators import Locators
from res.pages.LandingPage import LandingPage


class TestLandingPage(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=chrome_options)
        self.landing_page = LandingPage(self.driver)

    def test_login_button_is_displayed(self):
        assert self.landing_page.is_enabled(Locators.LOGIN_MODAL_BTN)

    def test_login_modal_is_displayed(self):
        self.landing_page.click(Locators.LOGIN_MODAL_BTN)
        assert self.landing_page.is_enabled(Locators.LOGIN_MODAL)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
