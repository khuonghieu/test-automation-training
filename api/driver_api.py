from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DriverAPI:
    """This class is the parent class for all the pom in our application."""
    """It contains all common elements and functionalities available to all pom."""

    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        self.find_element(by_locator).click()

    # this function switch to an iframe
    def switch_to_frame(self, by_locator):
        frame = self.find_element(by_locator)
        self.driver.switch_to.frame(frame)

    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        web_element = self.find_element(by_locator)
        assert web_element.text == element_text

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return self.find_element(by_locator).send_keys(text)

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_enabled(self, by_locator):
        return self.find_element(by_locator)

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self, by_locator):
        element = self.find_element(by_locator)
        return bool(element)

    def get_current_url(self):
        return self.driver.current_url
