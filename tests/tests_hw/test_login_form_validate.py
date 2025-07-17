# 2. реализуйте тест кейс
# a. перейти на страницу https://demoqa.com/automation-practice-form
# b. проверить плейсхолдер у полей
# i. first_name
# ii. last_name
# iii. user_email - также проверьте атрибут “pattern”
# c. Сделайте попытку отправки пустой формы и проверьте наличие класса “was-validated” у элемента формы

from pages.form_page import FormPage
import time

def test_login_form_attributes(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert form_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert form_page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert form_page.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert form_page.user_email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'

    form_page.btn_submit.click_force()
    time.sleep(2)
    assert form_page.form.get_dom_attribute('class') == "was-validated"

