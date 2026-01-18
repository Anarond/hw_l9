import pytest
from selene import browser
import time


@pytest.fixture
def browser_set():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield
    time.sleep(3)
    browser.quit()