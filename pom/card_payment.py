import time

from selenium.common.exceptions import TimeoutException

from pom.base_page import BasePage
from selenium.webdriver.common.by import By
from pom.login_modal import LoginModal
from pom.payment_modal import PaymentModal
from pom.pricing_page import PricingPage
from res.testdata import TestData


class CardPayment(BasePage):
    CARD_FORM = (By.CSS_SELECTOR, ".braintree-sheet__content.braintree-sheet__content--form")
    CARD_NUM_FRAME = (By.CSS_SELECTOR, "#braintree-hosted-field-number")
    EXP_DATE_FRAME = (By.CSS_SELECTOR, "#braintree-hosted-field-expirationDate")
    CVV_FRAME = (By.CSS_SELECTOR, "#braintree-hosted-field-cvv")
    POSTAL_FRAME = (By.CSS_SELECTOR, "#braintree-hosted-field-postalCode")
    CARD_NUMBER_INPUT = (By.CSS_SELECTOR, "#credit-card-number")
    CARD_DATE_INPUT = (By.CSS_SELECTOR, "#expiration")
    CARD_CVV_INPUT = (By.CSS_SELECTOR, "#cvv")
    CARD_POSTAL_INPUT = (By.CSS_SELECTOR, "#postal-code")
    CARD_ERROR_MESSAGE_LIST = (By.CLASS_NAME, "braintree-form__field-error")
    PAY_BTN = (By.CSS_SELECTOR, ".u-flex>.gi-Button.gi-Button--primary.u-width-100")
    TRANSACTION_SUCCESS_MODAL = (By.XPATH, "//div[@class='modal-content']")
    PAYMENT_FAIL_MESSAGE = (By.CSS_SELECTOR, ".braintree-sheet__error-text")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get_url(TestData.BASE_URL)

    def login(self, username, password):
        self.click(LoginModal.LOGIN_MODAL_BTN)
        self.enter_text(LoginModal.EMAIL_INPUT, username)
        self.enter_text(LoginModal.PASSWORD_INPUT, password)
        self.click(LoginModal.LOGIN_CONFIRM_BTN)

    def choose_subscription_option(self):
        self.driver.get_url(TestData.BASE_URL + 'pricing')
        self.driver.click(PricingPage.SUBSCRIPTION_BTN)

    def show_all_payment_methods(self):
        try:
            if self.is_visible(PaymentModal.CHOOSE_ANOTHER_METHOD):
                self.click(PaymentModal.CHOOSE_ANOTHER_METHOD)
                time.sleep(1)
            else:
                pass
        except TimeoutException:
            pass

    def choose_card_option(self):
        self.click(PaymentModal.CARD_OPTION)

    def fill_card_component_frame(self, frame_locator, input_locator, card_number):
        self.switch_to_frame(frame_locator)
        self.enter_text(input_locator, card_number)
        self.driver.switch_to_default()

    def fill_card_information(self, card_info_object):
        self.fill_card_component_frame(self.CARD_NUM_FRAME, self.CARD_NUMBER_INPUT, card_info_object["NUMBER"])
        self.fill_card_component_frame(self.EXP_DATE_FRAME, self.CARD_DATE_INPUT, card_info_object["DATE"])
        self.fill_card_component_frame(self.CVV_FRAME, self.CARD_CVV_INPUT, card_info_object["CVV"])
        self.fill_card_component_frame(self.POSTAL_FRAME, self.CARD_POSTAL_INPUT, card_info_object["POSTAL"])

    def card_info_is_valid(self):
        card_err_mess_list = self.driver.wrapped_driver.find_elements_by_class_name(self.CARD_ERROR_MESSAGE_LIST[1])
        valid = True
        for message in card_err_mess_list:
            if message.is_displayed():
                valid = False
        return valid
