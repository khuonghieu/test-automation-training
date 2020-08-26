from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LandingPage(BasePage):
    login_btn = (By.ID, 'test-login-button')
    login_modal = (By.XPATH, "//div[@class='modal-dialog']//div[@class='modal-content']")

    def __init__(self, browser):
        super(self, browser, base_url="https://www.got-it.io/solutions/excel-chat/")