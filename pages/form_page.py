from components.components import WebElement
from pages.base_page import BasePage

class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.gender_radio_1 = WebElement(driver, '#gender-radio-1')
        self.user_number = WebElement(driver, '#userNumber')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_close_modal = WebElement(driver, '#closeLargeModal')
        self.hobbies_checkbox_1 = WebElement(driver, '#hobbies-checkbox-1')
        self.current_address = WebElement(driver, '#currentAddress')
        self.states_form = WebElement(driver, '#state > div')
        self.states_list = WebElement(driver, '#state')
        self.btn_NCR = WebElement(driver, "//*[contains(text(), 'NCR')]", 'xpath')
        self.cities_form = WebElement(driver, '#city > div')
        self.cities_list = WebElement(driver, '#city')
        self.btn_Delhi = WebElement(driver, "//*[contains(text(), 'Delhi')]", 'xpath')
        self.form = WebElement(driver, 'form')