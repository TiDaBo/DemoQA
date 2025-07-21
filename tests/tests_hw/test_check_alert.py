# 2. в файле test_check_alert.py автоматизируйте тест кейс:
# a. Страница https://demoqa.com/alerts

import time
from pages.alerts import Alerts

def test_check_alert(browser):
    alerts_page = Alerts(browser)

    alerts_page.visit()

# i. на странице присутствует кнопка “#timerAlertButton”

    assert alerts_page.timer_alert_btn.exist()

# ii. через 5 сек после клика на кнопку всплывает алерт

    alerts_page.timer_alert_btn.click()
    time.sleep(5)
    assert alerts_page.alert()
    alerts_page.alert().accept()
    alerts_page.timer_alert_btn.click()
    time.sleep(4)
    assert not alerts_page.alert()


