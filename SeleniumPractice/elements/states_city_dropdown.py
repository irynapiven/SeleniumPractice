import time
import random

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium_base.base import SeleniumBase


class StatesCityDropDown(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.states_name = 'div[id="state"]'
        self.city_name = 'div[id="city"]'

    def find_states_field(self):
        item = self.is_present('css', self.states_name)
        self.go_to_element(item)
        return item

    def find_city_field(self):
        item = self.is_present('css', self.city_name)
        self.go_to_element(item)
        return item

    def fill_states_and_city(self):
        input_state_element = self.driver.find_element(By.ID, "react-select-3-input")
        states_array = ["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"]
        state_index = random.randint(0, 3)
        input_state_element.send_keys(states_array[state_index])
        input_state_element.send_keys(Keys.ENTER)
        city_array = []
        if state_index == 0:
            city_array = ["Delhi", "Gurgaon", "Noida"]
        elif state_index == 1:
            city_array = ["Agra", "Lucknow", "Merrut"]
        elif state_index == 2:
            city_array = ["Karnal", "Panipat"]
        elif state_index == 3:
            city_array = ["Jaipur", "Jaiselmer"]

        end_range = len(city_array)
        city_index = random.randint(0, (end_range-1))
        time.sleep(5)
        input_city_element = self.driver.find_element(By.ID, "react-select-4-input")
        input_city_element.send_keys(city_array[city_index])
        input_city_element.send_keys(Keys.ENTER)



        time.sleep(5)
