
from selenium.webdriver.common.by import By

def test_check_icon(browser):
    browser.get("https://demoqa.com/")

    icon = browser.find_element(By.CSS_SELECTOR, '#app > header > a')

    if icon is None:
        print('Элемент не найден')
    else:
        print('Элемент найден')


