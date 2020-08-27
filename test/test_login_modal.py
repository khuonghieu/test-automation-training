from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options
from res.pages.LoginModal import LoginModal
from res.locators import Locators
from res.testdata import TestData

class TestLoginModal(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.login_modal = LoginModal(self.driver)

    def test_login_modal_is_displayed(self):
        assert self.login_modal.is_enabled(Locators.LOGIN_MODAL)

    def test_success_login(self):
        self.login_modal.login(TestData.LOGIN_SUCCESS_ACCOUNT["USERNAME"], TestData.LOGIN_SUCCESS_ACCOUNT["PASSWORD"])
        assert self.login_modal.is_enabled(Locators.NAVBAR_ACCOUNT)

    def test_fail_login(self):
        self.login_modal.login(TestData.LOGIN_FAIL_ACCOUNT["USERNAME"], TestData.LOGIN_FAIL_ACCOUNT["PASSWORD"])
        assert self.login_modal.is_enabled(Locators.LOGIN_ERROR_MESSAGE)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
