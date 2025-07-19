from components.components import WebElement
from pages.base_page import BasePage

class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.table = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]', 'xpath')
        self.no_data = WebElement(driver, 'div.rt-noData')
        self.btns_del_row = WebElement(driver, '[id^="delete-record"]')