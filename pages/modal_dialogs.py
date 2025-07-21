from components.components import WebElement
from pages.base_page import BasePage

class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_third_menu = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, 'header > a > img')
        self.small_modal_btn = WebElement(driver, '#showSmallModal')
        self.large_modal_btn = WebElement(driver, '#showLargeModal')
        self.small_modal = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.large_modal = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.cls_small_modal_btn = WebElement(driver, '#closeSmallModal')
        self.cls_large_modal_btn = WebElement(driver, '#closeLargeModal')