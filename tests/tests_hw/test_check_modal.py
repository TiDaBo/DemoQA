# 1. в файле test_check_modal.py автоматизируйте тест кейс
# a. страница https://demoqa.com/modal-dialogs

import time
from pages.modal_dialogs import ModalDialogs

def test_check_modal(browser):
    modal_dialogs = ModalDialogs(browser)

    modal_dialogs.visit()

# i. на странице присутствуют 2 кнопки “Small modal” и “Large modal”

    assert modal_dialogs.small_modal_btn.exist()
    assert modal_dialogs.large_modal_btn.exist()

# ii. при клике на каждую открывается модальное окно
# iii. у каждого окна есть кнопка “close” по клику окно закрывается

    modal_dialogs.small_modal_btn.click()
    time.sleep(2)
    assert modal_dialogs.small_modal.exist()
    modal_dialogs.cls_small_modal_btn.click()
    time.sleep(2)
    assert not modal_dialogs.small_modal.exist()

    modal_dialogs.large_modal_btn.click()
    time.sleep(2)
    assert modal_dialogs.large_modal.exist()
    modal_dialogs.cls_large_modal_btn.click()
    time.sleep(2)
    assert not modal_dialogs.large_modal.exist()

# iv. *** Доработайте тестовый файл так, чтоб тест пропускался если страница недоступна.

''' @pytest.mark.skipif(False, reason='Page not available') '''

# Подумайте, как можно проверять страницу на доступность.

''' По статусу ответа, например (!=200), но я не знаю, как составить запрос '''