from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators


class TestPersonalAccount:
    def test_go_to_personal_account(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_SIGN_IN).send_keys('nataliasibgatullina9111@yandex.ru')
        driver.find_element(*TestLocators.PASSWORD_INPUT_SIGN_IN).send_keys('QAZwsx123')
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_TO_SIGN_IN).click()
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(TestLocators.SIGN_OUT_BUTTON))
        profile_text = driver.find_element(*TestLocators.TEXT_IN_PERSONAL_ACCOUNT)
        assert profile_text.text == "В этом разделе вы можете изменить свои персональные данные"
