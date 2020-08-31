from selenium import webdriver
import unittest
from res.pages.LandingPage import LandingPage


class TestLandingPage(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="../../test-automation-training/drivers/chromedriver",
                                       options=chrome_options)
        self.landing_page = LandingPage(self.driver)

    def test_login_button_is_displayed(self):
        assert self.landing_page.is_enabled(LandingPage.LOGIN_MODAL_BTN)

    def test_login_modal_is_displayed(self):
        self.landing_page.click(LandingPage.LOGIN_MODAL_BTN)
        assert self.landing_page.is_enabled(LandingPage.LOGIN_MODAL)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
