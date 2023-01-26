import base64
import os
import random
import time

from generator.generator import generate_file
from selenium_base.base import SeleniumBase


class UploadDownloadPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.upload_file = 'input[id="uploadPicture"]'

    def upload_files(self):
        file_name, path = generate_file()
        self.is_present('css', self.upload_file).send_keys(path)
        os.remove(path)
