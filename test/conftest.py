import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session", autouse=True)
def browser_management():
    browser.config.window_width = 1200
    browser.config.window_height = 1080
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form')
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element('footer').execute_script('element.remove()')

    yield

    browser.quit()
