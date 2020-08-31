from res.pages.BasePage import BasePage
from res.testdata import TestData
from selenium.webdriver.common.by import By


class LandingPage(BasePage):
    LOGIN_MODAL_BTN = (By.ID, "test-login-button")
    LOGIN_MODAL = (By.CSS_SELECTOR, "body.modal-open:nth-child(2) div.fade.in.modal:nth-child(2) div.modal-dialog "
                                    "div.modal-content div.modal-body > div.gi-AccountModal")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
