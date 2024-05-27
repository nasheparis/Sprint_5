import random

import pytest
from selenium import webdriver

from data import WEBSITE


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--windows-size=1920,1080')
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(WEBSITE)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def generate_new_user():
    return 'nataliasibgatullina9' + str(random.randint(100, 999)) + random.choice(
        ["@mail.ru", "@gmail.com", "@ya.ru", "@rambler.ru", "@yahoo.com"])
