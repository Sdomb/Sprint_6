from selenium.webdriver.common.by import By


class BasePageLocators:

    """Логотип самоката в хедере странички """
    header_logo = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')

    """Кнопка "Да все привыкли" в модалке кук на главной"""
    cocokies_btn = (By.ID, 'rcc-confirm-button')

    """Кнопка 'Статус заказа' в хедере"""
    header_status_order_btn = (By.CLASS_NAME, 'Header_Link__1TAG7')

    """Поле ввода для номера заказа в хедере """
    header_input_num_order = (By.CLASS_NAME, 'Input_Input__1iN_Z.Header_Input__xIoUq')

    """Кнопка 'GO' для вполнения поиска по номеру заказа из инпута в хедере"""
    header_search_btn_status = (By.CLASS_NAME, 'Button_Button__ra12g.Header_Button__28dPO')


