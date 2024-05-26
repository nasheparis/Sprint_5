from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators


class TestSignUp:
    def test_sign_up_invalid_password(self, driver):
        driver.find_element(*TestLocators.SIGN_IN_BUTTON).click()
        driver.find_element(*TestLocators.SIGN_UP_BUTTON).click()
        driver.find_element(*TestLocators.NAME_INPUT_SIGN_UP).send_keys('Natalia')
        driver.find_element(*TestLocators.EMAIL_INPUT_SIGN_UP).send_keys('nataliasibgatullina9111@yandex.ru')
        driver.find_element(*TestLocators.PASSWORD_INPUT_SIGN_UP).send_keys('QAZ')
        driver.find_element(*TestLocators.SIGN_UP_BUTTON_TO_REGISTER).click()
        error_message = driver.find_element(*TestLocators.INVALID_PASSWORD)
        assert error_message.text == "Некорректный пароль"

    def test_sign_up(self, driver):
        driver.find_element(*TestLocators.SIGN_IN_BUTTON).click()
        driver.find_element(*TestLocators.SIGN_UP_BUTTON).click()
        driver.find_element(*TestLocators.NAME_INPUT_SIGN_UP).send_keys('Natalia')
        driver.find_element(*TestLocators.EMAIL_INPUT_SIGN_UP).send_keys('nataliasibgatullina9013@yandex.ru')
        driver.find_element(*TestLocators.PASSWORD_INPUT_SIGN_UP).send_keys('QAZwsx123')
        driver.find_element(*TestLocators.SIGN_UP_BUTTON_TO_REGISTER).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(TestLocators.SIGN_IN_BUTTON_TO_SIGN_IN))
        driver.find_element(*TestLocators.EMAIL_INPUT_SIGN_IN).send_keys('nataliasibgatullina9013@yandex.ru')
        driver.find_element(*TestLocators.PASSWORD_INPUT_SIGN_IN).send_keys('QAZwsx123')
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_TO_SIGN_IN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.PLACE_ORDER_BUTTON))
        success = driver.find_element(*TestLocators.PLACE_ORDER_BUTTON)
        assert success.text == "Оформить заказ"