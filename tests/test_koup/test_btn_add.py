from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from pages.herokuapp import Herokuapp
from pages.add_remove import AddRemove


def test_btn_add(browser):
    herokuapp = Herokuapp(browser)
    add_remove = AddRemove(browser)

    herokuapp.visit()
    time.sleep(2)

    assert herokuapp.link_2.get_text() == 'Add/Remove Elements'
    herokuapp.link_2.click()
    # assert add_remove.equal_url()

    assert add_remove.add_el_btn.get_text() == 'Add Element'

    assert add_remove.add_el_btn.get_dom_attribute('onclick') == "addElement()"

    for i in range(4):
        add_remove.add_el_btn.click()

    assert add_remove.dlt_btns.check_count_elements(count=4)

    # проверка для всех элементов

    for element in add_remove.dlt_btns.find_elements():
        assert element.text == 'Delete'

    # проверка только для первого элемента (пример плохой проверки)
    # assert add_remove.dlt_btns.get_text() == 'Delete'

    while add_remove.dlt_btns.exist():
        add_remove.dlt_btns.click()

    assert not add_remove.dlt_btns.exist()
