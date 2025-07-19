import time
from pages.webtables import WebTables

def test_webtables(browser):
    webtables = WebTables(browser)

    webtables.visit()
    time.sleep(2)

    assert not webtables.table.get_text() == ''

    assert not webtables.no_data.exist()

    '''удаляем все записи'''
    while webtables.btns_del_row.exist():
        webtables.btns_del_row.click()

    time.sleep(2)

    assert webtables.no_data.exist()