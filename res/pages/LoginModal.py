from res.pages.BasePage import BasePage
from res.locators import Locators
from res.testdata import TestData


class LoginModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.implicitly_wait(10)
        self.driver.get(TestData.BASE_URL)
        self.click(Locators.LOGIN_MODAL_BTN)

    def login(self, username, password):
        self.enter_text(Locators.EMAIL_INPUT, username)
        self.enter_text(Locators.PASSWORD_INPUT, password)
        self.click(Locators.LOGIN_CONFIRM_BTN)