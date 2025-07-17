from components.components import WebElement
from pages.base_page import BasePage

class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.name = WebElement(driver, '#userName')
        self.current_address = WebElement(driver, '#currentAddress')
        self.submit_btn = WebElement(driver, '#submit')
        self.down_field_name = WebElement(driver, '#name.mb-1')
        self.down_field_current_address = WebElement(driver, '#currentAddress.mb-1')
