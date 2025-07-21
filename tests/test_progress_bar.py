import time
from pages.progress_bar import ProgressBar
from selenium.webdriver.common.keys import Keys


def test_progress_bar(browser):
    progress_bar = ProgressBar(browser)

    progress_bar.visit()
    time.sleep(2)
    progress_bar.start_stop_btn.click()

    while True:
        if progress_bar.bar.get_dom_attribute('aria-valuenow') == '51':
            progress_bar.start_stop_btn.click()
            break

    time.sleep(5)
    assert progress_bar.bar.get_dom_attribute('aria-valuenow') == '51'
