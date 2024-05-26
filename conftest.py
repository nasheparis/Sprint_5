import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--windows-size=1920,1080')
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()
