from selenium import webdriver
import unittest


class LoginModal(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.got-it.io/solutions/excel-chat")
        self.driver.implicitly_wait(10)
        login_btn = self.driver.find_element_by_id("test-login-button")
        login_btn.click()
        self.login_modal = self.driver.find_element_by_xpath(
            "//div[@class='modal-dialog']//div[@class='modal-content']")
        self.email = self.driver.find_element_by_xpath("//input[@placeholder='Email']")
        self.password = self.driver.find_element_by_xpath("//input[@placeholder='Password']")
        self.login_confirm_btn = self.driver.find_element_by_xpath("//button[@id='login-button']")

    def test_login_modal_is_displayed(self):
        assert self.login_modal.is_displayed()

    def test_login_success(self):
        self.email.send_keys("khuongletrunghieu1@gmail.com")
        self.password.send_keys("Abc123!")
        self.login_confirm_btn.click()
        # If found a navbar with account button then login was successful
        navbar_account = self.driver.find_element_by_class_name("gi-navBar-Account")
        assert navbar_account.is_displayed()

    def test_login_fail(self):
        self.email.send_keys("khuongletrunghieu1@gmail.com")
        self.password.send_keys("Abc123@")
        self.login_confirm_btn.click()
        # If error message pop out then login was unsuccessful
        error_message = self.driver.find_element_by_xpath("//div[@class='alert alert-danger']")
        assert error_message.is_displayed()

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
