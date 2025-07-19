from pages.text_box import TextBox
import time

def test_text_box_submit(browser):
    text_box = TextBox(browser)

    text_box.visit()
    time.sleep(2)

    assert text_box.submit_btn.check_css('color', 'rgba(255, 255, 255, 1)')
    assert text_box.submit_btn.check_css('backgroundColor', 'rgba(0, 123, 255, 1)')
    assert text_box.submit_btn.check_css('borderColor', 'rgb(0, 123, 255)')