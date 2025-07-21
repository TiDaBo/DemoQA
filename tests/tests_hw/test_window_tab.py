# 4. * в файле test_window_tab.py автоматизируйте тест кейс:
# a. Страница https://demoqa.com/links

from pages.links_page import Links
import time

def test_window_tab(browser):
    links_page = Links(browser)

    links_page.visit()

# b. На странице имеется ссылка “Home”

    assert links_page.link_home.exist()

# c. текст ссылки == “Home”

    assert links_page.link_home.get_text() == 'Home'

# d. href ссылки == “https://demoqa.com”

    assert links_page.link_home.get_dom_attribute('href') == 'https://demoqa.com'

# e. При клике на ссылку открывается новая вкладка

    links_page.link_home.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2

