from components.components import WebElement
from pages.base_page import BasePage

class Herokuapp(BasePage):

    def __init__(self, driver):
        self.base_url = 'http://the-internet.herokuapp.com/'
        super().__init__(driver, self.base_url)

        self.link_2 = WebElement(driver, '#content > ul > li:nth-child(2) > a')