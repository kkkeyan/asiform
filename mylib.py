from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import logging
import string

class mylib:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    @classmethod
    def browser_setup(self, browser):
        self.driver = webdriver.browser()
        self.driver.implicitly_wait(10)
        return self.driver

    def navigateUrl(self, base_url):
        if self.driver.get(base_url):
            return True
        else:
            return False

    def logConfig(self, logfile):
        logging.basicConfig(filename=logfile, level=logging.DEBUG, format=('%(asctime)s : %(message)s'))

    def element_is_visible(self, locator, locate_by='id', timeout=3):
        if locate_by=='css':locate_by = By.CSS_SELECTOR
        elif locate_by=='xpath':locate_by=By.XPATH
        elif locate_by=='class':locate_by=By.CLASS_NAME
        else: locate_by=By.ID
        try:
            WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located((locate_by,locator)))
        except TimeoutException as e:
            logging.debug("locator %s is not available", locator)
            return False
        return True

    def element_is_present(self, locator, locate_by='id', timeout=3):
        if locate_by=='css':locate_by = By.CSS_SELECTOR
        elif locate_by=='xpath':locate_by=By.XPATH
        elif locate_by=='class':locate_by=By.CLASS_NAME
        else: locate_by=By.ID
        try:
            WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located((locate_by,locator)))
        except NoSuchElementException as e:
            logging.debug.log("locator %s is not available", locator)
            return False
        return True

    def enter_text_byID(self, locator, value):
        self.driver.find_element_by_id(locator).clear()
        self.driver.find_element_by_id(locator).send_keys(value)

    def get_locator_type(self, locator):
        list = locator.string.split('=')
        if (list[0]=='css' or list[0]=='id' or list[0]=='xpath'): return list[0]
        assert False, 'Unable to get locator type'

    def get_locate_by(self, locate_by):
        if locate_by=='css':locate_by = By.CSS_SELECTOR
        elif locate_by=='xpath':locate_by=By.XPATH
        elif locate_by=='class':locate_by=By.CLASS_NAME
        else: locate_by=By.ID
        return locate_by

    def select_by_value(self, locator, text, locate_by='id'):
        self.element_is_visible(locator, locate_by)
        locate_by = self.get_locate_by(locate_by)
        locator = "option[value ='"+ text+"']"
        self.driver.find_element(locate_by, locator).click()
        return True

    def check_error_message_displayed(self, locator='mktoErrorMgs', locate_by='class'):
        if not self.element_is_visible(locator,locate_by):
            print "Error message is not found"
            return True
        print "Error message is found"
        return False

    def verify_error_message(self, error, locator, locate_by='class'):
        if self.check_error_message_displayed(locator,locate_by):
            locate_by = self.get_locate_by(locate_by)
            text = self.driver.find_element(locate_by,locator).text
            if text == error:
                return True
            else:
                print ("Expected error is %s, dispalyed error is %s", error, text)
                return False
        print "No error message is displayed"
        return False

    def click_button(self,locator,locate_by='css'):
        if self.element_is_visible(locator,locate_by):
            locate_by = self.get_locate_by(locate_by)
            self.driver.find_element(locate_by,locator).click()
            return True
        print "Button %s not found", locator
        return False

