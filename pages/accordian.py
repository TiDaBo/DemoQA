from components.components import WebElement
from pages.base_page import BasePage

class AccordianPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.center_text_what = WebElement(driver, '#section1Content > p')
        self.center_text_what_head = WebElement(driver, '#section1Heading')
        self.center_text_where_from_1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.center_text_where_from_2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.center_text_why_use = WebElement(driver, '#section3Content > p')
