from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import USER_PASSWORD, USER_EMAIL, WEBSITE_LOGIN_PAGE
from locators import TestLocators


class TestSignOut:
    def test_sign_out(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_SIGN_IN).send_keys(USER_EMAIL)
        driver.find_element(*TestLocators.PASSWORD_INPUT_SIGN_IN).send_keys(USER_PASSWORD)
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_TO_SIGN_IN).click()
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.SIGN_OUT_BUTTON))
        driver.find_element(*TestLocators.SIGN_OUT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.RESET_PASSWORD_BUTTON))
        assert driver.current_url == WEBSITE_LOGIN_PAGE
