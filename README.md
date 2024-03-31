# Sprint_6 Покрытие вебморды тестами в стиле POM (Page Object Model)

## Содержание
- [start](#)
- [conftest](#conftest)
- [locators](#locators)
- [page_objects](#page_objects)
- [tests](#tests)
- [allure_results](#allure_results)


## start

#### Для запуска проекта нужно использовать следующее:

импортировать библиотеки:
pytest, allure, webdriver


для запуска всех автотестов с формированием актуальных отчетов:
```
pytest header_page_test.py order_page_test.py home_page_test.py --alluredir=allure_results
```

открыть в браузере сформированные отчеты:

```
allure serve allure_results 
```


## conftest
Содержит стартовую фикстуру и создает клас локаторов



## locators
Содержит файлы с локаторами для всех страниц и общеиспользуемые локаторы в base


## page_objects
Тут находятся выделенные классы содержащие в себе методы и данные  для тестов


## tests
Здесь лежат тесты

## allure_results
Тут лежат отчеты. 
