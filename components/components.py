from selenium.webdriver.common.by import By

class WebElement:

    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def click(self):
        self.find_element().click()

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    # 1. в классе компонентов создайте метод для получения текста с элементов get_text(self).
    #  текст из элемента считывайте так str(self.find_element().text)

    def get_text(self):
        return str(self.find_element().text)
