from res.pages.PaymentModal import PaymentModal
from res.locators import Locators


class CardPayment(PaymentModal):
    def __init__(self, driver):
        super().__init__(driver)
        super().show_all_payment_methods()
        self.click(Locators.CARD_OPTION)

    def fill_card_component_frame(self, frame_locator, input_locator, card_number):
        self.switch_to_frame(frame_locator)
        self.enter_text(input_locator, card_number)
        self.driver.switch_to.default_content()

    def fill_card_information(self, card_info_object):
        self.fill_card_component_frame(Locators.CARD_NUM_FRAME, Locators.CARD_NUMBER_INPUT, card_info_object["NUMBER"])
        self.fill_card_component_frame(Locators.EXP_DATE_FRAME, Locators.CARD_DATE_INPUT, card_info_object["DATE"])
        self.fill_card_component_frame(Locators.CVV_FRAME, Locators.CARD_CVV_INPUT, card_info_object["CVV"])
        self.fill_card_component_frame(Locators.POSTAL_FRAME, Locators.CARD_POSTAL_INPUT, card_info_object["POSTAL"])

    def card_info_is_valid(self):
        card_err_mess_list = self.driver.find_elements_by_class_name(Locators.CARD_ERROR_MESSAGE_LIST[1])
        valid = True
        for message in card_err_mess_list:
            if message.is_displayed():
                valid = False
        return valid
