import time

from pages.alerts import Alerts

def test_alert(browser):
    alerts_page = Alerts(browser)

    alerts_page.visit()
    assert not alerts_page.alert()

    alerts_page.alert_btn.click()
    time.sleep(2)
    assert alerts_page.alert()


def test_alert_text(browser):
    alerts_page = Alerts(browser)

    alerts_page.visit()
    alerts_page.alert_btn.click()
    time.sleep(2)
    assert alerts_page.alert().text == 'You clicked a button'

    alerts_page.alert().accept()
    assert not alerts_page.alert()


def test_confirm(browser):
    alerts_page = Alerts(browser)

    alerts_page.visit()
    alerts_page.confirm_btn.click()
    time.sleep(2)
    alerts_page.alert().dismiss()
    assert alerts_page.confirm_result.get_text() == "You selected Cancel"


def test_prompt(browser):
    alerts_page = Alerts(browser)
    name = 'Daria'

    alerts_page.visit()
    alerts_page.prompt_btn.click()
    time.sleep(2)
    alerts_page.alert().send_keys(name)
    alerts_page.alert().accept()
    assert alerts_page.prompt_result.get_text() == f"You entered { name }"
