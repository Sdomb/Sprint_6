from selenium.webdriver.common.by import By


class PageOrderLocators:

    """Тайтл на страничке оформления заказа самоката """
    order_title = (By.CLASS_NAME, 'Order_Header__BZXOb')

    """Кнопка 'Заказать' в хедере """
    header_order_btn = (By.XPATH, './/div[contains(@class,"Header_Nav")]//button[text()="Заказать"]')

    """Кнопка Заказать внизу главной страницы """
    lower_order_btn = (By.XPATH, './/div[contains(@class,"Home_FinishButton")]//button[text()="Заказать"]')

    """Поле ввода имени на странице оформления заказа"""
    input_name = (By.XPATH, './/input[@placeholder="* Имя"]')

    """Поле ввода фамилии на странице оформления заказа"""
    input_surname = (By.XPATH, './/input[@placeholder="* Фамилия"]')

    """Поле ввода адреса, куда привезти заказ"""
    input_adress = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')

    """Выпадающий список станций метро на странице оформелния заказа"""
    drop_list_metro = (By.CLASS_NAME, "select-search__input")

    """Станиция метро "Нагорная" """
    metro_station_item = (By.XPATH, '//div[text()="Нагорная"]')

    """Поле ввода номера телефона на который позвонить курьер"""
    input_phone_number = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')

    """Кнопка 'Далее' на странице оформления заказа  """
    next_btn = (By.CLASS_NAME, 'Button_Button__ra12g.Button_Middle__1CSJM')

    """Заголовок 'Про аренду' на страничке оформления заказа"""
    rent_title = (By.XPATH, '//div[text()="Про аренду"]')

    """Поле ввода даты, когда привезти самокат"""
    input_day_rent_start = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]')

    """Календарь для ввода даты, в которую нужно привезти самокат"""
    date_picker_rent_start = (By.CLASS_NAME, 'react-datepicker-popper')

    """Кнопка выпадающего спиcка для срока аренды """
    date_rent_list = (By.XPATH, '//div[text() = "* Срок аренды"]')

    """Вариант ""трое суток"" аренды из выпадающего списка """
    three_days_rent_el = (By.XPATH, './/div[@class = "Dropdown-option" and text()="трое суток"]')

    """Чекбокс выбора серого цвета арендуемых самокатов """
    grey_checkbox = (By.ID, "grey")

    """Поле ввода комментария для курьера """
    input_courier_comment = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')

    """Кнопка "Заказать" на страничке оформления заказа"""
    order_btn = (By.XPATH, '//button[@class = "Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]')

    """Всплывающее окно подтверждения оформления заказа"""
    modal_order_window = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')

    """Кнопка "ДА" подтверждения оформления заказа в модальном окне"""
    yes_btn_in_modal = (By.XPATH, './/button[text()="Да"]')

    """Сообщение о заказе в модальном окне """
    order_completed_modal = (By.XPATH, './/*[contains(@class,"Order_ModalHeader")]')


    """Блок оформления заказа с полями для ввода личных данных"""
    block_order_info = (By.XPATH, '//div[contains(@class, "Order_Content")]')

