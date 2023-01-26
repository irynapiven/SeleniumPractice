import time
from selenium_base.base import SeleniumBase


class DateTime(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.first_name = 'input[id="dateOfBirthInput"]'

    def find_date_if_birth(self):
        item = self.is_present('css', self.first_name)
        self.go_to_element(item)
        return item
