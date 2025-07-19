import pytest
from pages.accordian import AccordianPage
from pages.browser_tab import BrowserTab
from pages.demoqa import DemoQA
from pages.alerts import Alerts
import time

@pytest.mark.parametrize("pages", [AccordianPage, Alerts, DemoQA, BrowserTab])
def test_check_meta_all_pages(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)
    assert page.viewport.exist()
    assert page.viewport.get_dom_attribute('name') == 'viewport'
    assert page.viewport.get_dom_attribute('content') == 'width=device-width,initial-scale=1'