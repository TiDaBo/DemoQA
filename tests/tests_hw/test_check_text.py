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
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def test_check_text_elements(browser):
    demo_qa_page = DemoQA(browser)
    el_page = ElementsPage(browser)

    demo_qa_page.visit()

    # Закрытие баннера, если он появился
    try:
        close_banner = browser.find_element(By.ID, "close-fixedban")
        close_banner.click()
    except NoSuchElementException:
        pass  # баннера нет — идем дальше

    demo_qa_page.btn_elements.click()
    assert el_page.center_area.get_text() == 'Please select an item from left to start practice.'


def test_page_elements(browser):
    el_page = ElementsPage(browser)
    el_page.visit()

    assert el_page.icon.exist()
    assert el_page.btn_sidebar_first.exist()
    assert el_page.btn_sidebar_first_textbox.exist()

