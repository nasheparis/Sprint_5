from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import TestLocators


class TestConstructorSections:
    def test_constructor_sections_buns(self, driver):
        driver.find_element(*TestLocators.FILLINGS_SECTION).click()
        driver.find_element(*TestLocators.BUNS_SECTION).click()
        heading = driver.find_element(*TestLocators.BUNS_SECTION_HEADING)
        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable(TestLocators.BUNS_SECTION_HEADING))
        assert "Булки" in heading.text

    def test_constructor_sections_sauces(self, driver):
        driver.find_element(*TestLocators.SAUCES_SECTION).click()
        item = driver.find_element(*TestLocators.SAUCE_ITEM)
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable(TestLocators.SAUCE_ITEM))
        assert "Соус" in item.text

    def test_constructor_sections_fillings(self, driver):
        driver.find_element(*TestLocators.FILLINGS_SECTION).click()
        heading = driver.find_element(*TestLocators.FILLINGS_SECTION_HEADING)
        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable(TestLocators.FILLINGS_SECTION_HEADING))
        assert "Начинки" in heading.text
