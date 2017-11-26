import os
from selenium import webdriver
from myres import Data

class mydriver():

    def __init__(self):
        self.base_url = Data.base_url
        self.browser = Data.browser

    def navigateUrl(self):
        if Data.browser=='Firefox':
            self.driver = webdriver.Firefox()
        if Data.browser == 'Chrome':
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url)
        return self.driver
