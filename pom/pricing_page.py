from pom.base_page import BasePage
from res.testdata import TestData
from selenium.webdriver.common.by import By
from pom.login_modal import LoginModal


class PricingPage(BasePage):
    _expected_url = TestData.BASE_URL + "/pricing"

    INDIVIDUAL_SMALL_BUSINESS_BTN = (By.CSS_SELECTOR, ".gi-coverPricing-Tab-Item.is-active.test-invididuals-tab")
    SUBSCRIPTION_BTN = (By.XPATH, "//button[contains(text(),'TRY FOR FREE')]")
    PRICING_BTN = (By.CSS_SELECTOR, "#pricing-navlink-landing")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get_url(TestData.BASE_URL)

    def is_present(self):
        return self._expect_url in self.driver.get_current_url()

    def login(self, username, password):
        self.click(LoginModal.LOGIN_MODAL_BTN)
        self.enter_text(LoginModal.EMAIL_INPUT, username)
        self.enter_text(LoginModal.PASSWORD_INPUT, password)
        self.click(LoginModal.LOGIN_CONFIRM_BTN)

    def go_to_pricing_page(self):
        self.driver.get_url(TestData.BASE_URL + 'pricing')
