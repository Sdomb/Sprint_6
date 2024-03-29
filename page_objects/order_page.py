import random

import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage
from locators.order_page_locators import PageOrderLocators


class OrderPage(BasePage):
    @allure.step('Кликаем на кнопку Заказать в хедере ')
    def click_order_header_btn(self):
        self.click(PageOrderLocators.header_order_btn)

    @allure.step('Кликаем на кнопку Заказть внизу страницы')
    def click_order_lower_btn(self):
        self.click(PageOrderLocators.lower_order_btn)

    @allure.step('Вводим Имя')
    def input_name(self, name):
        self.input_text(PageOrderLocators.input_name, name)

    @allure.step('Вводим Фамилию')
    def input_surname(self, surname):
        self.input_text(PageOrderLocators.input_surname, surname)

    @allure.step('Добавляем адрес')
    def input_address(self, address):
        self.input_text(PageOrderLocators.input_adress, address)

    @allure.step('Вписываем метро')
    def choice_metro(self, metro):
        self.click(PageOrderLocators.drop_list_metro)
        self.input_text(PageOrderLocators.drop_list_metro, metro)
        self.click(PageOrderLocators.metro_station_item)

    @allure.step('Вводим номер телефона')
    def input_phone_number(self, number):
        self.input_text(PageOrderLocators.input_phone_number, number)

    @allure.step('Генерируем случайную дату и вводим ее')
    def input_start_date_rent(self):
        date = str(random.randint(10, 28)) + '.' + str(random.randint(10, 12)) + '.2024'
        self.input_text(PageOrderLocators.input_day_rent_start, date)
        self.click(PageOrderLocators.rent_title)

    @allure.step('Выбираем срок аренды')
    def order_filled_date(self):
        self.click(PageOrderLocators.date_rent_list)
        self.click(PageOrderLocators.three_days_rent_el)

    @allure.step('Вписываем пользовательские данные для оформления заказа')
    def filling_personal_date_action(self, name, surname, address, metro, number):
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.choice_metro(metro)
        self.input_phone_number(number)
        self.click(PageOrderLocators.next_btn)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(PageOrderLocators.rent_title))
        self.input_start_date_rent()
        self.order_filled_date()
        self.click(PageOrderLocators.grey_checkbox)
        self.input_text(PageOrderLocators.input_courier_comment, 'Fus-Ro-Dah!!!!')
        self.click(PageOrderLocators.order_btn)
        self.click(PageOrderLocators.yes_btn_in_modal)

    @allure.step('Ждем появления окна подтверждения заказа')
    def check_congratulation_modal(self):
        text = self.wait_element(PageOrderLocators.order_completed_modal)
        return self.get_text_element(text)

    personal_date = [
                    ['Борислав', 'Грожеедов', 'Пролетарский переулок 3', 'Нагорная', '88005553535'],
                     ['Ульфрик', 'Буревестник', 'Громовая гора, пик 4 ', 'Нагорная', '88002000600']
                     ]