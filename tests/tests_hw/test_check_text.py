# 2. в файле test_check_text.py реализуйте тест-кейс:
# a. перейти на страницу 'https://demoqa.com/'
# b. проверить что текст в подвале == ‘© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.’

from pages.demoqa import DemoQA

def test_check_text(browser):

    demo_qa_page = DemoQA(browser)
    demo_qa_page.visit()
    assert demo_qa_page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

# 3. в файле test_check_text.py реализуйте тест-кейс:
# a. перейти на страницу 'https://demoqa.com/'
# b. через кнопку перейти на страницу 'https://demoqa.com/elements'
# c. проверить что текст по центру == 'Please select an item from left to start practice.'

from pages.elements_page import ElementsPage

def test_check_text_elements(browser):

    demo_qa_page = DemoQA(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    assert elements_page.center_area.get_text() == 'Please select an item from left to start practice.'

