from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import USER_PASSWORD, USER_EMAIL
from locators import TestLocators


class TestSignIn:
    def test_sign_in_main(self, driver):
        driver.find_element(*TestLocators.SIGN_IN_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_SIGN_IN).send_keys(USER_EMAIL)
        driver.find_element(*TestLocators.PASSWORD_INPUT_SIGN_IN).send_keys(USER_PASSWORD)
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_TO_SIGN_IN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.PLACE_ORDER_BUTTON))
        success = driver.find_element(*TestLocators.PLACE_ORDER_BUTTON)
        assert success.text == "Оформить заказ"

    def test_sign_in_personal_account(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_SIGN_IN).send_keys(USER_EMAIL)
        driver.find_element(*TestLocators.PASSWORD_INPUT_SIGN_IN).send_keys(USER_PASSWORD)
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_TO_SIGN_IN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.PLACE_ORDER_BUTTON))
        success = driver.find_element(*TestLocators.PLACE_ORDER_BUTTON)
        assert success.text == "Оформить заказ"

    def test_sign_in_sign_up_page(self, driver):
        driver.find_element(*TestLocators.SIGN_IN_BUTTON).click()
        driver.find_element(*TestLocators.SIGN_UP_BUTTON).click()
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_ON_SIGN_UP_PAGE).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_SIGN_IN).send_keys(USER_EMAIL)
        driver.find_element(*TestLocators.PASSWORD_INPUT_SIGN_IN).send_keys(USER_PASSWORD)
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_TO_SIGN_IN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.PLACE_ORDER_BUTTON))
        success = driver.find_element(*TestLocators.PLACE_ORDER_BUTTON)
        assert success.text == "Оформить заказ"

    def test_sign_in_reset_password_page(self, driver):
        driver.find_element(*TestLocators.SIGN_IN_BUTTON).click()
        driver.find_element(*TestLocators.RESET_PASSWORD_BUTTON).click()
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_ON_RESET_PASSWORD_PAGE).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_SIGN_IN).send_keys(USER_EMAIL)
        driver.find_element(*TestLocators.PASSWORD_INPUT_SIGN_IN).send_keys(USER_PASSWORD)
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_TO_SIGN_IN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.PLACE_ORDER_BUTTON))
        success = driver.find_element(*TestLocators.PLACE_ORDER_BUTTON)
        assert success.text == "Оформить заказ"
