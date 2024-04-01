import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем объект {locator}')
    def wait_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Кликаем на ')
    def click(self, locator):
        WebDriverWait(self.driver, 2).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Печатаем текст в поле ввода')
    def input_text(self, locator, text):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получаем текст из локатора')
    def get_text_element(self, locator):
        return locator.text

    @allure.step('Ждем кнопку кук и кликаем на неё')
    def click_cookie_button(self):
        self.wait_element(BasePageLocators.cocokies_btn)
        self.click(BasePageLocators.cocokies_btn)
