from pages.slider_page import Slider
from selenium.webdriver.common.keys import Keys


def test_slider(browser):
    slider_page = Slider(browser)

    slider_page.visit()
    assert slider_page.slider.exist()
    assert slider_page.slider_text_field.exist()
    assert slider_page.slider_text_field.get_dom_attribute('value') == '25'

    while not slider_page.slider_text_field.get_dom_attribute('value') == '50':
        slider_page.slider.send_keys(Keys.ARROW_RIGHT)

    assert slider_page.slider_text_field.get_dom_attribute('value') == '50'


