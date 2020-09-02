from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options
from pom.LoginModal import LoginModal
from res.testdata import TestData


class TestLoginModal(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="../../test-automation-training/drivers/chromedriver",
                                       options=chrome_options)
        self.login_modal = LoginModal(self.driver)

    def test_login_modal_is_displayed(self):
        assert self.login_modal.is_enabled(LoginModal.LOGIN_MODAL)

    def test_success_login(self):
        self.login_modal.login(TestData.LOGIN_SUCCESS_ACCOUNT["USERNAME"], TestData.LOGIN_SUCCESS_ACCOUNT["PASSWORD"])
        assert self.login_modal.is_enabled(LoginModal.NAVBAR_ACCOUNT)

    def test_fail_login(self):
        self.login_modal.login(TestData.LOGIN_FAIL_ACCOUNT["USERNAME"], TestData.LOGIN_FAIL_ACCOUNT["PASSWORD"])
        assert self.login_modal.is_enabled(LoginModal.LOGIN_ERROR_MESSAGE)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
