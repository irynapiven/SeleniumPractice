from selenium_base.base import SeleniumBase


class GenderRadio(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.male_option = 'label[for="gender-radio-1"]'
        self.female_option = 'label[for="gender-radio-2"]'
        self.other_option = 'label[for="gender-radio-3"]'

    def find_male_option(self):
        return self.is_visible('css', self.male_option)

    def find_female_option(self):
        return self.is_visible('css', self.female_option)

    def find_other_option(self):
        return self.is_visible('css', self.other_option)

    def click_random_gender(self, gender_index):
        if gender_index == 0:
            self.find_male_option().click()
        elif gender_index == 1:
            self.find_female_option().click()
        else:
            self.find_other_option().click()
        return gender_index
