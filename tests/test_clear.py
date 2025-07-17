from pages.text_box import TextBox
import time

def test_clear(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.name.send_keys('Random text')
    time.sleep(2)
    text_box.username.clear()
    time.sleep(2)
    assert text_box.name.get_text() == ''