import unittest
from selenium import webdriver
from myres import Locators
from myres import Data
import mylib
import logging
from myutil import myUtil
from mydriver import mydriver


class myTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        #myTest.driver = mydriver()
        #myTest.driver.navigateUrl()
        if Data.browser=='Firefox':
            self.driver = webdriver.Firefox()
        if Data.browser == 'Chrome':
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(Data.base_url)
        self.my_util = myUtil(self.driver)


    def tearDown(self):
        self.driver.close()

    def testContactPageValidation(self):
        self.my_util.log("Starting testContactPageValidation")
        self.assertFalse(not self.my_util.navigateContactPage()),"Test Passed"
        self.my_util.EnterContactForm()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest((myTest('testContactPageValidation')))
    unittest.TextTestRunner().run(suite)

