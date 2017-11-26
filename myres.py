from selenium.webdriver.common.by import By

class Locators(object):
    webChat_Frame_locator =  "//div[@class='intercom-messenger-frame']"
    webChat_Frame = 'intercom-messenger-frame'
    webChat_Locator_id = 'web-chat-button'
    webChat_Close_button_locator = "//div[@class='intercom-header-buttons-close-contents']"
    contactUs_text_locator = "//div[@class='banner-title' and normalize-space()='Contact Us']"
    contactUs_text_locator1 = "//div[@class='banner-title']/text()[normalize-space()='Contact Us']"
    contactUs_firstName_id = 'FirstName'
    contactUs_lastName_id = 'LastName'
    contactUs_comapnyName_id = 'Company'
    contactUs_emailId_id = 'Email'
    contactUs_phoneNo_id = 'Phone'
    contactUs_Country_id = 'Country'
    contactUs_description_id = 'Call_Description__c'
    contactUs_sumbitButton_css = 'button.mktoButton'
    contactUs_form_locator = 'wide-page-no-container'
    contactUs_form_frame = 'form-iframe'

class Data(object):
    base_url = "http://www.asigra.com/"
    browser = 'Firefox'
    logfile = 'logfile.log'
    test_firstname = 'karthik'
    test_lastname = 'k'
    test_companyName = 'ktech'
    test_emailId = 'karthik@ktech.com'
    test_country = 'Canada'
    error_message = 'This field is required.'


