import random
import time
from typing import List, Any

from selenium_base.base import SeleniumBase


class HobbiCheckBox(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.sport_check_box = 'label[for="hobbies-checkbox-1"]'
        self.reading_check_box = 'label[for="hobbies-checkbox-2"]'
        self.music_check_box = 'label[for="hobbies-checkbox-3"]'

    def find_sport_check_box(self):
        return self.is_visible('css', self.sport_check_box)

    def find_reading_check_box(self):
        return self.is_visible('css', self.reading_check_box)

    def find_music_check_box(self):
        return self.is_visible('css', self.music_check_box)

    def generate_random_array(self):
        random_array = [] * 3
        first_random_index = random.randint(0, 2)
        second_random_index = random.randint(0, 2)
        while first_random_index == second_random_index:
            first_random_index = random.randint(0, 2)

        random_array.append(first_random_index)
        random_array.append(second_random_index)
        return random_array

    def click_random_checkbox(self):
        random_array = self.generate_random_array()
        for index in random_array:
            if index == 0:
                self.find_sport_check_box().click()
            elif index == 1:
                self.find_reading_check_box().click()
            else:
                self.find_music_check_box().click()
