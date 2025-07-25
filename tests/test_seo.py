import pytest
from pages.accordian import AccordianPage
from pages.browser_tab import BrowserTab
from pages.demoqa import DemoQA
from pages.alerts import Alerts
import time


def test_check_title_demo(browser):
    demo_qa_page = DemoQA(browser)

    demo_qa_page.visit()
    assert browser.title == 'DEMOQA'

@pytest.mark.parametrize("pages", [AccordianPage, Alerts, DemoQA, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'
