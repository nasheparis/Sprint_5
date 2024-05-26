from locators import TestLocators


class TestConstructorFromAccount:
    def test_go_to_constructor_via_header_button(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_SIGN_IN).send_keys('nataliasibgatullina9111@yandex.ru')
        driver.find_element(*TestLocators.PASSWORD_INPUT_SIGN_IN).send_keys('QAZwsx123')
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_TO_SIGN_IN).click()
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        success = driver.find_element(*TestLocators.PLACE_ORDER_BUTTON)
        assert success.text == "Оформить заказ"

    def test_go_to_constructor_via_logo(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.EMAIL_INPUT_SIGN_IN).send_keys('nataliasibgatullina9111@yandex.ru')
        driver.find_element(*TestLocators.PASSWORD_INPUT_SIGN_IN).send_keys('QAZwsx123')
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_TO_SIGN_IN).click()
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.LOGO_BUTTON).click()
        success = driver.find_element(*TestLocators.PLACE_ORDER_BUTTON)
        assert success.text == "Оформить заказ"
