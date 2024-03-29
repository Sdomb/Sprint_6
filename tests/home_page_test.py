import allure
import pytest
from locators.home_page_locators import HomeLocators
from page_objects.home_page import HomePage


class TestHomePage:
    @allure.title('Тест на получение соответствующих ответов после тапа на вопрос аккордеона.')
    @allure.description('В тесте проверяем что когда нажимаешь на стрелочку, открывается соответствующий текст.')
    @pytest.mark.parametrize("index, text_of_answer",
                             [
                                 (0, HomePage.text[0]),
                                 (1, HomePage.text[1]),
                                 (2, HomePage.text[2]),
                                 (3, HomePage.text[3]),
                                 (4, HomePage.text[4]),
                                 (5, HomePage.text[5]),
                                 (6, HomePage.text[6]),
                                 (7, HomePage.text[7])
                             ])
    def test_check_answers(self, driver, index, text_of_answer):

        home_page = HomePage(driver)

        home_page.click_cookie_button()
        home_page.scroll_to_element(HomeLocators.home_subtitle)
        question = home_page.tap_question(HomeLocators.cell_question, index)
        result = home_page.find_answer(HomeLocators.cell_answer, index)

        assert text_of_answer[question] == result
