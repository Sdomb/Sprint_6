from selenium.webdriver.common.by import By


class HeaderPageLocators:

    """Логотип яндекса в хедере на главной страничке """
    logo_yandex_header = By.XPATH, './/a[contains(@class, "Header_LogoYandex")]'

    """Логотип скутера в хедере на главной страничке """
    logo_scooter_header = By.XPATH, './/a[contains(@class, "Header_LogoScooter")]'
