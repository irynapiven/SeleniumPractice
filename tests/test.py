import random
import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from elements.Hobbies_check_box import HobbiCheckBox
from elements.dateTime import DateTime
from elements.elements import Elements
from elements.genderRadio import GenderRadio
from elements.multiple_select import MultipleSelect
from elements.states_city_dropdown import StatesCityDropDown
from elements.upload_download_files import UploadDownloadPage


@pytest.mark.usefixtures('setup')
class TestElements:

    def test1(self):
        page = Elements(self.driver)
        page.find_submit_button()
        time.sleep(5)

    def test(self):
        gender_array = ["Male", "Femail", "Other"]
        page = Elements(self.driver)
        first_name, last_name, email, mobile, current_address = page.fill_all_fields()

        radio_elements = GenderRadio(self.driver)
        gender_index = (random.randint(0, 2))
        radio_elements.click_random_gender(gender_index)
        gender = gender_array[gender_index]

        check_box_elements = HobbiCheckBox(self.driver)
        check_box_elements.click_random_checkbox()

        upload_download_page = UploadDownloadPage(self.driver)
        upload_download_page.upload_files()

        date_item = DateTime(self.driver)
        day_of_birth_item = date_item.find_date_if_birth()
        day_of_birth_item.click()
        for x in range(15):
            day_of_birth_item.send_keys(Keys.SHIFT, Keys.ARROW_LEFT)
        day_of_birth_item.send_keys("26/01/2023")
        day_of_birth_item.send_keys(Keys.ENTER)

        subjects_item = MultipleSelect(self.driver)
        subjects_item_object = subjects_item.find_subjects_field()
        subjects_item_object.click()
        subjects_item_object.send_keys("s")
        subjects_item_object.send_keys(Keys.ARROW_DOWN)
        subjects_item_object.send_keys(Keys.ARROW_DOWN)
        subjects_item_object.send_keys(Keys.ENTER)
        subjects_item_object.click()
        subjects_item_object.send_keys(Keys.SPACE)
        subjects_item_object.send_keys(Keys.ARROW_DOWN)
        subjects_item_object.send_keys(Keys.ENTER)

        state_city_item = StatesCityDropDown(self.driver)
        test = state_city_item.fill_states_and_city()

        time.sleep(10)
        page.find_submit_button().click()
        time.sleep(10)