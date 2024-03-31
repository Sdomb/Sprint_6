import pytest
from selenium import webdriver
from total_info import Info


@pytest.fixture(scope='function')
def driver():
    firefox_options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=firefox_options)
    driver.set_window_size(1024, 768)
    driver.get(Info.scooter_page_url)
    yield driver
    driver.quit()


