# 1. Автоматизируйте тест кейс, страница https://demoqa.com/webtables

import time
from pages.webtables import WebTables

def test_webtables_hw1(browser):
    webtables = WebTables(browser)

    webtables.visit()

    # a. на странице имеется кнопка Add

    assert webtables.btn_add_rec.exist()

    # b. по клику на кнопку Add открывается диалоговое окно

    webtables.btn_add_rec.click()
    assert webtables.modal_registration.exist()

    # c. в диалоге нельзя сохранить пустую форму

    webtables.modal_reg_sbmt_btn.click()
    assert webtables.modal_registration.exist()
    time.sleep(2)

    # d. если заполнить все поля и нажать на кнопку Submit
    # i. диалог закрывается
    # ii. в таблицу добавляется новая запись с введенными данными

    webtables.mod_reg_first_name.send_keys('test')
    webtables.mod_reg_last_name.send_keys('testov')
    webtables.mod_reg_email.send_keys('test@test.te')
    webtables.mod_reg_age.send_keys('18')
    webtables.mod_reg_salary.send_keys('100500')
    webtables.mod_reg_dptmnt.send_keys('IT')
    time.sleep(2)
    webtables.modal_reg_sbmt_btn.click_force()
    time.sleep(2)
    assert not webtables.modal_registration.exist()
    assert 'test' in webtables.table_row.get_text() and 'testov' in webtables.table_row.get_text() and 'test@test.te' in webtables.table_row.get_text() and '18' in webtables.table_row.get_text() and '100500' in webtables.table_row.get_text() and 'IT' in webtables.table_row.get_text()

    # e. если кликнуть на карандаш на строке записи

    webtables.btn_edit_row_4.click()
    time.sleep(2)

    # i. открывается диалог с введенными данными

    assert webtables.modal_registration.exist()
    assert webtables.mod_reg_first_name.get_dom_attribute('value') == 'test'
    assert webtables.mod_reg_last_name.get_dom_attribute('value') == 'testov'
    assert webtables.mod_reg_email.get_dom_attribute('value') == 'test@test.te'
    assert webtables.mod_reg_age.get_dom_attribute('value') == '18'
    assert webtables.mod_reg_salary.get_dom_attribute('value') == '100500'
    assert webtables.mod_reg_dptmnt.get_dom_attribute('value') == 'IT'

    # f. если изменить имя и сохранить то в таблице обновятся данные

    webtables.mod_reg_first_name.clear()
    webtables.mod_reg_first_name.send_keys('new')
    time.sleep(1)
    webtables.modal_reg_sbmt_btn.click_force()
    assert 'new' in webtables.table_row.get_text()

    # g. если нажать на корзину в строке записи - запись удаляется

    webtables.btn_del_row_4.click()
    assert '' in webtables.table_row.get_text()


# 2. * Автоматизируйте тест кейс, страница https://demoqa.com/webtables

import time
from pages.webtables import WebTables

def test_webtables_hw2(browser):
    webtables = WebTables(browser)

    # a. предусловия
    # i. открыта страница
    # ii. кол-во строк в таблице установлено 5

    webtables.visit()
    time.sleep(2)
    webtables.page_size_ops.click()
    time.sleep(2)
    webtables.page_size_op_5.click()
    time.sleep(2)

    # b. тест кейс
    # i. кнопки Next и Previous заблокированы (по клику ничего не происходит и имеют атрибут disabled)

    assert webtables.next_btn.get_dom_attribute('disabled') is not None
    assert webtables.prev_btn.get_dom_attribute('disabled') is not None

    # ii. если добавить в таблицу еще 3 записи то:
    # 1. появляется 2-я страница (of 2)
    # 2. кнопка Next становится доступной

    for i in range(3):
        webtables.btn_add_rec.click()
        time.sleep(2)
        webtables.mod_reg_first_name.send_keys('test')
        webtables.mod_reg_last_name.send_keys('testov')
        webtables.mod_reg_email.send_keys('test@test.te')
        webtables.mod_reg_age.send_keys('18')
        webtables.mod_reg_salary.send_keys('100500')
        webtables.mod_reg_dptmnt.send_keys('IT')
        time.sleep(2)
        webtables.modal_reg_sbmt_btn.click_force()
        time.sleep(2)

    assert 'of 2' in webtables.pages_count.get_text()
    assert webtables.next_btn.get_dom_attribute('disabled') is False

    # iii. если кликнуть по кнопке Next то открывается 2-я страница

    webtables.next_btn.click()
    time.sleep(2)
    assert webtables.current_page.get_dom_attribute('value') == '2'

    # iv. если кликнуть по кнопке Previous то открывается 1-я страница

    webtables.prev_btn.click()
    time.sleep(2)
    assert webtables.current_page.get_dom_attribute('value') == '1'