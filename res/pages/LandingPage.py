from res.pages.BasePage import BasePage
from res.testdata import TestData


class LandingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.implicitly_wait(10)
        self.driver.get(TestData.BASE_URL)
