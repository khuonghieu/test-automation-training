import time

from selenium.webdriver.common.by import By

from pom.base_page import BasePage


class AdminUserProfile(BasePage):

    GOOGLE_AUTH_BTN = (By.CSS_SELECTOR, ".btn.btn-lg.btn-social.btn-google")
    TERMINATE_SUBSCRIPTION_BTN = (By.CSS_SELECTOR, "#terminateSubscriptionButton")
    STORAGE_KEY = '"accesstoken"'
    STORAGE_VALUE = 'JSON.stringify({"access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEwOCwiYXVkIjoiYWRtaW4iLCJpYXQiOjE1OTkyMDk1MzMsImV4cCI6MTYzMDc0NTUzMywibm9uY2UiOiJmMzdlOTdkYSJ9.K3F6c8ATs2A204Zgoc0w5ZJcjEt63dJjT1qYwzWWIc8","account_id":108,"account_name":"Hugh Khuong","account_type":"admin","auth_type":"google"})'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get_url("https://admin.got-it.io/")
        self.driver.execute_script("window.localStorage.setItem("+self.STORAGE_KEY+","+self.STORAGE_VALUE+")")
        self.driver.get_url("https://admin.got-it.io/user/students/17536")

    def terminate_subscription(self):
        if self.is_enabled(self.TERMINATE_SUBSCRIPTION_BTN):
            self.click(self.TERMINATE_SUBSCRIPTION_BTN)
