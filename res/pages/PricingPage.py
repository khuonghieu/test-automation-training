from res.pages.LoginModal import LoginModal
from res.testdata import TestData
from res.locators import Locators


class PricingPage(LoginModal):
    def __init__(self, driver):
        super().__init__(driver)
        super().login(TestData.LOGIN_SUCCESS_ACCOUNT["USERNAME"], TestData.LOGIN_SUCCESS_ACCOUNT["PASSWORD"])
        self.driver.get(TestData.BASE_URL + "/pricing")
        super().click(Locators.PRICING_BTN)

