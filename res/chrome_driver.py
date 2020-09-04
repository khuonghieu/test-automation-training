from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ChromeDriver:
    @staticmethod
    def instantiate():
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path="../drivers/chromedriver", options=chrome_options)
        return driver
