import os
from time import sleep
import pickle
from selenium import webdriver
import unittest
from services.service import Service
from services.config import *

name=os.path.basename(__file__)

class LoginTest_Sucess(unittest.TestCase):

    def setUp(self):
        if CONFIG_APP.GOOGLE:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("prefs", CONFIG_APP.PREFS_0)   
            chrome_options.add_experimental_option("prefs", CONFIG_APP.PREFS_1)   
            self.driver = webdriver.Chrome(CONFIG_APP.WEB_DRIVER_CHROME, options=chrome_options)
        else: 
            browser_profile = webdriver.FirefoxProfile()
            browser_profile.set_preference("dom.webnotifications.enabled", False)
            self.driver = webdriver.Firefox(executable_path=CONFIG_APP.WEB_DRIVER_FIREFOX, firefox_profile=browser_profile)
        self.driver.get(CONFIG_APP.WEB_PAGE)
        
    def testPythonScript(self):
        driver=self.driver
        driver.implicitly_wait(CONFIG_APP.TIME_IMPLICIT)
        driver.maximize_window()
        self.handler = Service(driver)
        self.handler.writeToInputs(CONFIG_XPATHS.EMAIL_FIELD, ASSERTS_CONS.VALID_USER)
        self.handler.writeToInputs(CONFIG_XPATHS.PASS_FIELD, ASSERTS_CONS.VALID_PASS)
        self.handler.click(CONFIG_XPATHS.LOGIN_BUTTON)
        sleep(CONFIG_APP.SLEEP_TIME)
        driver.get_screenshot_as_file(CONFIG_APP.EVIDENCE_PATH+str(name)+CONFIG_APP.IMG_FORMAT)
        # with open(CONFIG_APP.LOG_COOKIES, "wb") as f:
        #     pickle.dump(driver.get_cookies(), f)
        # f.close()
        assert ASSERTS_CONS.FACEBOOK_PAGE in driver.title
        driver.quit()

if __name__ == "__main__":
    unittest.main()