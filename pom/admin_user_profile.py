from selenium.webdriver.common.by import By

from pom.base_page import BasePage


class AdminUserProfile(BasePage):

    GOOGLE_AUTH_BTN = (By.CSS_SELECTOR, ".btn.btn-lg.btn-social.btn-google")
    TERMINATE_SUBSCRIPTION_BTN = (By.CSS_SELECTOR, "#terminateSubscriptionButton")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get_url("https://admin.got-it.io/user/students/17536")

    def google_log_in(self):
        self.click(self.GOOGLE_AUTH_BTN)

    def terminate_subscription(self):
        if self.is_visible(self.TERMINATE_SUBSCRIPTION_BTN):
            self.click(self.TERMINATE_SUBSCRIPTION_BTN)
