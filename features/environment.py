from behave import fixture
from behave.fixture import use_fixture
from pom.admin_user_profile import AdminUserProfile
from res.chrome_driver import ChromeDriver


@fixture
def browser_chrome(context, **kwargs):
    context.browser = ChromeDriver().instantiate()
    yield context.browser
    context.browser.delete_all_cookies()
    context.browser.quit()


def before_tag(context, tag):
    if tag == 'browser.chrome':
        use_fixture(browser_chrome, context)


# def after_tag(context, tag):
#     if tag == 'terminate_subscription':
#         context.admin_user_profile = AdminUserProfile(context.browser)
#         context.admin_user_profile.terminate_subscription()


def after_step(context, step):
    if step.status == 'failed':
        step_str = step.name
        context.browser.save_screenshot('screenshots/' + step_str + ".png")
