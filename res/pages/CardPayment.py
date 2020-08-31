import time

from res.pages.PaymentModal import PaymentModal
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class CardPayment(PaymentModal):

    CARD_FORM = (By.CSS_SELECTOR, "body.modal-open:nth-child(2) div.fade.in.modal:nth-child(2) div.modal-dialog "
                                  "div.modal-content div.modal-body div.braintree-show-card "
                                  "div.braintree-dropin.braintree-loaded:nth-child(2) "
                                  "div.braintree-upper-container:nth-child(5) "
                                  "div.braintree-sheet__container.braintree-sheet--active > "
                                  "div.braintree-card.braintree-form.braintree-sheet")
    CARD_NUM_FRAME = (By.ID, "braintree-hosted-field-number")
    EXP_DATE_FRAME = (By.ID, "braintree-hosted-field-expirationDate")
    CVV_FRAME = (By.ID, "braintree-hosted-field-cvv")
    POSTAL_FRAME = (By.ID, "braintree-hosted-field-postalCode")
    CARD_NUMBER_INPUT = (By.ID, "credit-card-number")
    CARD_DATE_INPUT = (By.ID, "expiration")
    CARD_CVV_INPUT = (By.ID, "cvv")
    CARD_POSTAL_INPUT = (By.ID, "postal-code")
    CARD_ERROR_MESSAGE_LIST = (By.CLASS_NAME, "braintree-form__field-error")
    PAY_BTN = (By.CSS_SELECTOR, "body.modal-open:nth-child(2) div.fade.in.modal:nth-child(2) div.modal-dialog "
                                "div.modal-content div.modal-footer div.u-flex.u-flexGrow-1.u-flexColumn > "
                                "button.gi-Button.gi-Button--primary.u-width-100")
    TRANSACTION_SUCCESS_MODAL = (By.CSS_SELECTOR, "body.modal-open:nth-child(2) div:nth-child(20) "
                                                  "div.fade.in.modal:nth-child(2) div.modal-dialog > "
                                                  "div.modal-content")
    PAYMENT_FAIL_MESSAGE = (By.CSS_SELECTOR, "body.modal-open:nth-child(2) div.fade.in.modal:nth-child(2) "
                                             "div.modal-dialog div.modal-content div.modal-body "
                                             "div.braintree-show-card "
                                             "div.braintree-dropin.braintree-loaded.braintree-sheet--has-error:nth"
                                             "-child(2) div.braintree-upper-container:nth-child(5) "
                                             "div.braintree-sheet__container.braintree-sheet--active "
                                             "div.braintree-sheet__error > div.braintree-sheet__error-text")
    SESSION_BALANCE = (By.CSS_SELECTOR, "div.App div.gi-Landing.gi-Landing--Pricing div.gi-navBar div.container "
                                        "div.gi-navBar-Inner div.gi-navBar-Items "
                                        "button.gi-navBar-Button.gi-navBar-Button--sessionBalance > "
                                        "strong.u-marginLeft-1.u-marginRight-2:nth-child(2)")

    def __init__(self, driver):
        super().__init__(driver)
        super().show_all_payment_methods()
        time.sleep(2)
        self.click(self.CARD_OPTION)

    def fill_card_component_frame(self, frame_locator, input_locator, card_number):
        self.switch_to_frame(frame_locator)
        self.enter_text(input_locator, card_number)
        self.driver.switch_to.default_content()

    def fill_card_information(self, card_info_object):
        self.fill_card_component_frame(self.CARD_NUM_FRAME, self.CARD_NUMBER_INPUT, card_info_object["NUMBER"])
        self.fill_card_component_frame(self.EXP_DATE_FRAME, self.CARD_DATE_INPUT, card_info_object["DATE"])
        self.fill_card_component_frame(self.CVV_FRAME, self.CARD_CVV_INPUT, card_info_object["CVV"])
        self.fill_card_component_frame(self.POSTAL_FRAME, self.CARD_POSTAL_INPUT, card_info_object["POSTAL"])

    def card_info_is_valid(self):
        card_err_mess_list = self.driver.find_elements_by_class_name(self.CARD_ERROR_MESSAGE_LIST[1])
        valid = True
        for message in card_err_mess_list:
            if message.is_displayed():
                valid = False
        return valid
