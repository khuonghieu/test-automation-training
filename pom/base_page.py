from api.driver_api import DriverAPI


class BasePage:
    """This class is the parent class for all the pom in our application."""
    """It contains all common elements and functionalities available to all pom."""
    _expect_url = ""

    def is_present(self):
        pass

    def get_expect_url(self):
        return self._expect_url

    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver = DriverAPI(driver)

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        self.driver.click(by_locator)

    # this function switch to an iframe
    def switch_to_frame(self, by_locator):
        self.driver.switch_to_frame(by_locator)

    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        self.driver.assert_element_text(by_locator, element_text)

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return self.driver.enter_text(by_locator, text)

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_enabled(self, by_locator):
        return self.driver.is_enabled(by_locator)

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self, by_locator):
        return self.driver.is_visible(by_locator)
