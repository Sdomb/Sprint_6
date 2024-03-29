import allure

from locators.header_page_locators import HeaderPageLocators
from page_objects.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step('Клик по логотипу Яндекса в хедере')
    def click_on_yandex_logo(self):
        self.click(HeaderPageLocators.logo_yandex_header)

    @allure.step('Клик по логотипу Самоката в хедере')
    def click_on_scooter_logo(self):
        self.click(HeaderPageLocators.logo_scooter_header)
