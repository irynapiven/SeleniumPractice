import time
from selenium_base.base import SeleniumBase


class MultipleSelect(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.first_name = 'input[id="subjectsInput"]' #'div[class="subjects-auto-complete__input"]'

    def find_subjects_field(self):
        item = self.is_present('css', self.first_name)
        self.go_to_element(item)
        return item