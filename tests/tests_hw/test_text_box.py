# 1. реализуйте тест кейс
# a. перейти на страницу https://demoqa.com/text-box
# b. записать в поля Full Name, Current Address произвольный текст
# c. нажать на кнопку submit
# d. проверить, что снизу появились 2 элемента с нашим текстом
# i. * сравнение и ввод текста, реализовать через переменную

from pages.text_box import TextBox
import time

def test_down_field_check(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.name.send_keys('He-Who-Must-Not-Be-Named')
    text_box.current_address.send_keys('Unknown place')
    text_box.submit_btn.click_force()
    time.sleep(2)
    assert text_box.name.get_text() in text_box.down_field_name.get_text()
    assert text_box.current_address.get_text() in text_box.down_field_current_address.get_text()