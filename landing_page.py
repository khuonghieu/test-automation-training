from selenium import webdriver
import unittest


class LandingPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.got-it.io/solutions/excel-chat")
        self.driver.implicitly_wait(10)

    def test_login_button(self):
        login_btn = self.driver.find_element_by_id("test-login-button")
        assert login_btn.is_displayed()

    def test_pressing_login_button(self):
        login_btn = self.driver.find_element_by_id("test-login-button")
        login_btn.click()
        login_modal = self.driver.find_element_by_xpath("//div[@class='modal-dialog']//div[@class='modal-content']")
        assert login_modal.is_displayed()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
