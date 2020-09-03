from pom.base_page import BasePage
from res.testdata import TestData
from selenium.webdriver.common.by import By


class LoginModal(BasePage):

    LOGIN_MODAL = (By.CSS_SELECTOR, "#modal-login")
    EMAIL_INPUT = (By.CSS_SELECTOR, '.gi-FormGroup input[name="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '.gi-FormGroup input[name="password"]')
    LOGIN_CONFIRM_BTN = (By.CSS_SELECTOR, "#login-button")
    LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-danger")
    LOGIN_MODAL_BTN = (By.CSS_SELECTOR, "#test-login-button")
    NAVBAR_ACCOUNT = (By.CSS_SELECTOR, "#setting_menu")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get_url(TestData.BASE_URL)
        self.click(self.LOGIN_MODAL_BTN)

    def fill_username(self, username):
        self.enter_text(self.EMAIL_INPUT, username)

    def fill_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.click(self.LOGIN_CONFIRM_BTN)
