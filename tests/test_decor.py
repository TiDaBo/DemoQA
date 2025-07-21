import pytest
from pages.demoqa import DemoQA
from pages.radio_button import RadioButton

@pytest.mark.skip
def test_decor(browser):
    demoqa = DemoQA(browser)

    demoqa.visit()
    assert demoqa.cards_titles.check_count_elements(count=6)

    for element in demoqa.cards_titles.find_elements():
        assert element.text != ''

# @pytest.mark.skipif(True, reason='просто пропуск')
def test_decor_2(browser):
    radio_button = RadioButton(browser)

    radio_button.visit()
    radio_button.yes.click_force()
    assert radio_button.result_field.get_text() == 'You have selected Yes'

    radio_button.impressive.click_force()
    assert radio_button.result_field.get_text() == 'You have selected Impressive'

    assert 'disabled' radio_button.no.get_dom_attribute('class')