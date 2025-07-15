# создайте тест кейс test_visible_accordion(browser) в нем реализуйте кейс:
# i. перейти на страницу https://demoqa.com/accordian
# 1. для этого в папке pages создайте файл accordion.py
# 2. в файле реализуйте класс страницы Accordion, по аналогии с классами DemoQa и ElementsPage
# 3. Отличается только название, урл и элементы
# 4. в тестовом файле (test_visible_hw.py)
# a. импортируйте новый класс
# b. создайте объект страницы
# c. вызовите метод входа

import time
from pages.accordian import AccordianPage

def test_visible_accordian(browser):
    ac_page = AccordianPage(browser)
    ac_page.visit()


# ii. проверьте, что элемент #section1Content > p виден
# 1. в новом классе страницы добавьте элемент с указанным локатором
# 2. в тестовом файле добавьте проверку на видимость элемента

    assert ac_page.center_text_what.visible()


# iii. кликните на #section1Heading
# 1. в новом классе страницы добавьте элемент с указанным локатором
# 2. в тестовом файле вызовите метод .click() для созданного элемента

    ac_page.center_text_what_head.click()


# iv. После клика добавьте time.sleep(2)

    time.sleep(2)


# v. проверьте, что элемент #section1Content > p НЕ виден
# 1. добавьте проверку на видимость элемента и добавьте отрицание (элемент уже есть)

    assert not ac_page.center_text_what.visible()


# создайте тест кейс test_visible_accordion_default(browser) в нем реализуйте кейс:
# i. перейдите на страницу https://demoqa.com/accordian
# 1. создайте объект страницы
# 2. вызовите метод входа

def test_visible_accordion_default(browser):
    ac_page = AccordianPage(browser)
    ac_page.visit()


# ii. проверьте, что следующие элементы по умолчанию скрыты
# 1. #section2Content > p:nth-child(1)
# 2. #section2Content > p:nth-child(2)
# 3. #section3Content > p
# 4. Для этого:
# a. Создайте каждый элемент в классе страницы
# b. в тесте вызовите проверку видимости для каждого
# c. в каждую проверку добавьте отрицание

    assert not ac_page.center_text_where_from_1.visible()
    assert not ac_page.center_text_where_from_2.visible()
    assert not ac_page.center_text_why_use.visible()