# -- FILE: features/environment.py
# CONTAINS: Browser fixture setup and teardown
from behave import fixture, use_fixture
from selenium.webdriver import Firefox
from unittest import TestCase


@fixture
def browser_firefox(context):
    # -- BEHAVE-FIXTURE: Similar to @contextlib.contextmanager
    context.driver = Firefox()
    context.url = 'http://192.168.33.10:8080/'
    context.test = TestCase()
    yield context.driver
    # -- CLEANUP-FIXTURE PART:
    context.driver.quit()


def before_all(context):
    use_fixture(browser_firefox, context)
    # -- NOTE: CLEANUP-FIXTURE is called after after_all() hook.
