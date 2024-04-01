import allure

from page_objects.base_page import BasePage


class HomePage(BasePage):

    @allure.step('Скроллим к локатору {locator}')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Тапаем на вопрос в аккордеоне')
    def tap_question(self, locator, index):
        selector, locator = locator
        locator = locator.format(index)
        self.wait_element((selector, locator))
        self.click((selector, locator))
        return self.wait_element((selector, locator)).get_attribute("id")

    @allure.step('Ищем в открывшемся элементе аккордеона ответ на вопрос')
    def find_answer(self, locator, index):
        selector, locator = locator
        locator = locator.format(index)
        element = self.wait_element((selector, locator))
        return element.text
