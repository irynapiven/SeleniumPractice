import time

from generator.generator import create_person
from selenium_base.base import SeleniumBase


class Elements(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.first_name = '#firstName'
        self.last_name = '#lastName'
        self.email = '#userEmail'
        self.mobile = '#userNumber'
        self.current_address = '#currentAddress'
        self.submit_button = '#submit'

    def text_first_name(self):
        return self.is_visible('css', self.first_name)

    def text_last_name(self):
        return self.is_visible('css', self.last_name)

    def text_email(self):
        return self.is_visible('css', self.email)

    def text_mobile(self):
        return self.is_visible('css', self.mobile)

    def text_current_address(self):
        return self.is_visible('css', self.current_address)

    def find_submit_button(self):
        item = self.is_present('css', self.submit_button)
        self.go_to_element(item)
        time.sleep(5)

    def fill_all_fields(self):
        person_info = next(create_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        mobile = person_info.phone_number
        current_address = person_info.current_address

        self.text_first_name().send_keys(first_name)
        self.text_last_name().send_keys(last_name)
        self.text_email().send_keys(email)
        self.text_mobile().send_keys(mobile)
        self.text_current_address().send_keys(current_address)
        return first_name, last_name, email, mobile, current_address

