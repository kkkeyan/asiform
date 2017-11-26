import selenium
from selenium.webdriver.common.by import By
from mylib import mylib
from myres import Locators
from myres import Data
import logging
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class myUtil(object):
    driver = None
    my_lib = None


    def __init__(self, driver):
        self.driver = driver
        self.my_lib = mylib(self.driver)

    def get_driver(self):
        self.mylib.browser_setup(Data.browser)

    def log(self, log_string):
        self.my_lib.logConfig(Data.logfile)
        logging.info(log_string)

    def closeChatWindow(self):
        if self.my_lib.element_is_visible(Locators.webChat_Frame_locator, 'xpath',10):
            self.driver.find_elements_by_xpath(Locators.webChat_Frame_locator)
            self.driver.switch_to_frame(Locators.webChat_Frame)
            if self.driver.find_element_by_xpath(Locators.webChat_Close_button_locator):
                self.driver.find_element_by_xpath(Locators.webChat_Close_button_locator).click()
                self.driver.switch_to_default_content()
                if self.my_lib.element_is_visible(Locators.webChat_Frame_locator, 'xpath'):
                    assert False,"Failed to close chat window"
        return True

    def navigateContactPage(self):
        page = Data.base_url + "contact-us"
        mylib.navigateUrl(self.my_lib,page)
        if self.closeChatWindow():
            if self.check_contactUs_text():
                return True
        assert False, "Navigation failed"

    def check_contactUs_text(self):
        if self.driver.find_element_by_xpath(Locators.contactUs_text_locator):
            return True

    def click_submit_button(self):
        self.my_lib.click_button(Locators.contactUs_sumbitButton_css, 'css')

    def check_submit_error_message(self, error,locator='mktoErrorMsg', locate_by='class'):
        if not self.my_lib.verify_error_message(error,locator,locate_by):
            return True
        print "Error message is not matched or found"
        return False


    def EnterContactForm(self ):
        self.closeChatWindow() #sometime it takes time for the chat frame to appear
        self.driver.switch_to_frame(self.driver.find_element_by_tag_name("iframe"))
        self.my_lib.element_is_visible(Locators.contactUs_firstName_id, 'id')
        self.my_lib.enter_text_byID(Locators.contactUs_firstName_id, Data.test_firstname)
        self.my_lib.element_is_visible(Locators.contactUs_lastName_id)
        self.my_lib.enter_text_byID(Locators.contactUs_lastName_id, Data.test_lastname)
        self.my_lib.select_by_value(Locators.contactUs_Country_id, 'CA', 'css')
        self.click_submit_button()
        self.my_lib.verify_error_message(Data.error_message)
        self.driver.switch_to_default_content()
        return True


