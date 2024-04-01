from selenium.webdriver.common.by import By


class HomeLocators:

    """Заголовок на главной страничке """
    home_title = (By.CLASS_NAME, 'Home_Header__iJKdX')

    """Подзаголовок 'Вопросы о важном' """
    home_subtitle = (By.XPATH, '//div[@class="Home_SubHeader__zwi_E" and contains(text(), "Вопросы о важном")]')

    """Локатор вопросов без индекса"""
    cell_question = (By.ID, 'accordion__heading-{}')

    """Локтор ответов без индекса"""
    cell_answer = (By.ID, 'accordion__panel-{}')
