from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage
from components.components import WebElement


def test_go_to_page_elements(browser):

    demo_qa_page = DemoQA(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    demo_qa_page.btn_elements.click()
    assert elements_page.equal_url()
