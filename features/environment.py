from behave import fixture
from behave.fixture import use_fixture
from chrome_driver import ChromeDriver


@fixture
def browser_chrome(context, **kwargs):
    context.browser = ChromeDriver().instantiate()
    yield context.browser
    context.browser.delete_all_cookies()
    context.browser.quit()

def before_tag(context, tag):
    if tag == 'browser.chrome':
        use_fixture(browser_chrome, context)
