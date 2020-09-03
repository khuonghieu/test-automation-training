from pom.login_modal import LoginModal
from res.testdata import TestData
from selenium.webdriver.common.by import By


class PricingPage(LoginModal):

    _expected_url = TestData.BASE_URL + "/pricing"

    INDIVIDUAL_SMALL_BUSINESS_BTN = (
        By.CSS_SELECTOR,
        "div.App div.gi-Landing.gi-Landing--Pricing:nth-child(2) div.gi-coverPricing div.container-fluid "
        "div.gi-coverPricing-Tab > button.gi-coverPricing-Tab-Item.is-active.test-invididuals-tab:nth-child(1)")
    SUBSCRIPTION_BTN = (By.CSS_SELECTOR,
                        "div.App div.gi-Landing.gi-Landing--Pricing:nth-child(2) div.gi-coverPricing "
                        "div.container-fluid div.gi-coverPricing-Inner.gi-coverPricing-Inner--Individuals div.row "
                        "div.col-12.col-md-4:nth-child(3) div.gi-pricingItem div.gi-pricingItem-Button > button.btn")

    def __init__(self, driver):
        super().__init__(driver)
        super().login(TestData.LOGIN_SUCCESS_ACCOUNT["USERNAME"], TestData.LOGIN_SUCCESS_ACCOUNT["PASSWORD"])
        self.driver.get_url(TestData.BASE_URL + "/pricing")
        super().click(self.PRICING_BTN)

    def is_present(self):
        return self._expect_url in self.driver.get_current_url()
