from pages.form_page import FormPage
import time

def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerovich')
    form_page.user_email.send_keys('test@ttt.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('9992223344')
    form_page.hobbies_checkbox_1.click_force()
    form_page.current_address.send_keys('Мой адрес не дом и не улица')
    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(2)

    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()


# a. создайте новый тест кейс
# b. реализуйте заполнение поля State and City

def test_state_city_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    form_page.states_form.click_force()
    time.sleep(2)
    form_page.states_list.click_force()
    time.sleep(2)
    form_page.cities_form.click_force()
    time.sleep(2)
    form_page.cities_list.click_force()
    time.sleep(2)

# def test_state_city_1(browser):
#     form_page = FormPage(browser)
#
#     form_page.visit()
#     time.sleep(2)
#     form_page.states_form.scroll_to_element()
#     time.sleep(2)
#     form_page.states_form.click()
#     form_page.btn_NCR.click()
#     form_page.cities_form.click()
#     form_page.btn_Delhi.click()
#     time.sleep(2)
#
# def test_state_city_2(browser):
#     form_page = FormPage(browser)
#
#     form_page.visit()
#     time.sleep(2)
#     form_page.states_form.scroll_to_element()
#     form_page.states_form.click()
#     time.sleep(2)
#     form_page.states_list.send_keys('NCR')
#     form_page.states_list.send_keys(Keys.ENTER)
#     time.sleep(2)
#
# def test_state_city_3(browser):
#     form_page = FormPage(browser)
#
#     form_page.visit()
#     time.sleep(2)
#     form_page.states_form.scroll_to_element()
#     form_page.states_form.click()
#     time.sleep(2)
#     form_page.states_list.send_keys(Keys.PAGE_DOWN)
#     form_page.states_list.send_keys(Keys.ENTER)
#     time.sleep(2)