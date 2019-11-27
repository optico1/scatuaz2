# -- FILE: features/environment.py
# CONTAINS: Browser fixture setup and teardown
from behave import fixture, use_fixture
<<<<<<< HEAD
from selenium.webdriver import Chrome

@fixture
def browser_chorome(context):
    # -- BEHAVE-FIXTURE: Similar to @contextlib.contextmanager
    context.driver = Chrome()
    yield context.driver
    # -- CLEANUP-FIXTURE PART:
    context.driver.quit()

def before_all(context):
    use_fixture(browser_chorome, context)
    # -- NOTE: CLEANUP-FIXTURE is called after after_all() hook.
=======
from selenium.webdriver import Firefox
from unittest import TestCase


@fixture
def browser_firefox(context):
    # -- BEHAVE-FIXTURE: Similar to @contextlib.contextmanager
    context.driver = Firefox()
    context.url = 'http://192.168.33.10:8000/'
    context.test = TestCase()
    yield context.driver
    # -- CLEANUP-FIXTURE PART:
    # context.driver.quit()


def before_all(context):
    use_fixture(browser_firefox, context)
    # -- NOTE: CLEANUP-FIXTURE is called after after_all() hook.
>>>>>>> origin/master
