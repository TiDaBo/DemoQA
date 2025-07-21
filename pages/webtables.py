from components.components import WebElement
from pages.base_page import BasePage

class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.table = WebElement(driver, '.rt-table')
        self.no_data = WebElement(driver, 'div.rt-noData')
        self.btns_del_row = WebElement(driver, '[id^="delete-record"]')
        self.btn_add_rec = WebElement(driver, '#addNewRecordButton')
        self.modal_registration = WebElement(driver, '#registration-form-modal')
        self.modal_reg_sbmt_btn = WebElement(driver, '#submit')
        self.modal_reg_rows = WebElement(driver, '.mt-2')
        self.mod_reg_first_name = WebElement(driver, '#firstName')
        self.mod_reg_last_name = WebElement(driver, '#lastName')
        self.mod_reg_email = WebElement(driver, '#userEmail')
        self.mod_reg_age = WebElement(driver, '#age')
        self.mod_reg_salary = WebElement(driver, '#salary')
        self.mod_reg_dptmnt = WebElement(driver, '#department')
        self.table_row = WebElement(driver, '.rt-tbody div:nth-child(4) > div')
        self.page_size_ops = WebElement(driver, '#app span.select-wrap.-pageSizeOptions > select')
        self.page_size_op_5 = WebElement(driver, '#app span.select-wrap.-pageSizeOptions > select > option:nth-child(1)')
        self.prev_btn = WebElement(driver, '.-previous')
        self.next_btn = WebElement(driver, '.-next')
        self.pages_count = WebElement(driver, '.-pageInfo')
        self.current_page = WebElement(driver, '.-pageJump > input')
        self.btn_edit_row_4 = WebElement(driver, '#edit-record-4#edit-record-4')
        self.btn_del_row_4 = WebElement(driver, '#delete-record-4#delete-record-4')

        self.col_first_name = WebElement(driver, "#app .rt-thead > [role='row'] > div:nth-of-type(1)")
        self.col_last_name = WebElement(driver, "#app .rt-thead > [role='row'] > div:nth-of-type(2)")
        self.col_email = WebElement(driver, "#app .rt-thead > [role='row'] > div:nth-of-type(3)")
        self.col_age = WebElement(driver, "#app .rt-thead > [role='row'] > div:nth-of-type(4)")
        self.col_salary = WebElement(driver, "#app .rt-thead > [role='row'] > div:nth-of-type(5)")
        self.col_dptmnt = WebElement(driver, "#app .rt-thead > [role='row'] > div:nth-of-type(6)")
