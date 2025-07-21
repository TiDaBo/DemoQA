# 3. в файле test_sort.py автоматизируйте тест кейс:
# a. Страница https://demoqa.com/webtables

from pages.webtables import WebTables

def test_sort(browser):
    webtables = WebTables(browser)

    webtables.visit()

# b. при клике на каждый заголовок столбца страницы, происходит сортировка таблицы по этому столбцу
# (Для проверки сортировки, в данном кейсе, достаточно считывать соответствующий класс элемента)

    webtables.col_first_name.click()
    assert 'sort-asc' in webtables.col_first_name.get_dom_attribute('class')
    webtables.col_last_name.click()
    assert 'sort-asc' in webtables.col_last_name.get_dom_attribute('class')
    webtables.col_email.click()
    assert 'sort-asc' in webtables.col_email.get_dom_attribute('class')
    webtables.col_age.click()
    assert 'sort-asc' in webtables.col_age.get_dom_attribute('class')
    webtables.col_salary.click()
    assert 'sort-asc' in webtables.col_salary.get_dom_attribute('class')
    webtables.col_dptmnt.click()
    assert 'sort-asc' in webtables.col_dptmnt.get_dom_attribute('class')

