from pom.base_page import BasePage
from res.testdata import TestData
from selenium.webdriver.common.by import By


class LoginModal(BasePage):
    LOGIN_MODAL = (By.CSS_SELECTOR, "body.modal-open:nth-child(2) div.fade.in.modal:nth-child(2) div.modal-dialog "
                                    "div.modal-content div.modal-body > div.gi-AccountModal")

    EMAIL_INPUT = (By.CSS_SELECTOR, "body.modal-open:nth-child(2) div.fade.in.modal:nth-child(2) div.modal-dialog "
                                    "div.modal-content div.modal-body div.gi-AccountModal div.gi-FormGroup:nth-child("
                                    "3) > input.gi-Input:nth-child(2)")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "body.modal-open:nth-child(2) div.fade.in.modal:nth-child(2) div.modal-dialog "
                                       "div.modal-content div.modal-body div.gi-AccountModal "
                                       "div.gi-FormGroup:nth-child(4) > input.gi-Input:nth-child(2)")
    LOGIN_CONFIRM_BTN = (By.ID, "login-button")
    LOGIN_ERROR_MESSAGE = (
        By.CSS_SELECTOR, "body.modal-open:nth-child(2) div.fade.in.modal:nth-child(2) div.modal-dialog "
                         "div.modal-content div.modal-body div.gi-AccountModal > "
                         "div.alert.alert-danger:nth-child(1)")
    LOGIN_MODAL_BTN = (By.ID, "test-login-button")
    NAVBAR_ACCOUNT = (By.CSS_SELECTOR, "div.App div.gi-Landing:nth-child(2) div.gi-navBar div.container "
                                       "div.gi-navBar-Inner div.gi-navBar-Items > div.gi-navBar-Account")
    PRICING_BTN = (By.ID, "pricing-navlink-landing")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get_url(TestData.BASE_URL)
        self.click(self.LOGIN_MODAL_BTN)

    def fill_username(self, username):
        self.enter_text(self.EMAIL_INPUT, username)

    def fill_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def press_login_button(self):
        self.click(self.LOGIN_CONFIRM_BTN)

    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.click(self.LOGIN_CONFIRM_BTN)
