from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage
# import time

def test_navigation(browser):
    demo_qa_page = DemoQA(browser)
    el_page = ElementsPage(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()

    demo_qa_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()

    assert el_page.equal_url()