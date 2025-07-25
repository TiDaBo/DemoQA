from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from components.components import WebElement

class DemoQA(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        self.footer = WebElement(driver, 'footer > span')
        self.cards_titles = WebElement(driver, '#app .category-cards h5')

