from pom.base_page import BasePage
from res.testdata import TestData
from selenium.webdriver.common.by import By


class LandingPage(BasePage):
    LOGIN_MODAL_BTN = (By.ID, "test-login-button")
    LOGIN_MODAL = (By.CSS_SELECTOR, "body.modal-open:nth-child(2) div.fade.in.modal:nth-child(2) div.modal-dialog "
                                    "div.modal-content div.modal-body > div.gi-AccountModal")

    _expected_url = TestData.BASE_URL

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get_url(TestData.BASE_URL)

    def is_present(self):
        return self._expect_url in self.driver.get_current_url()
