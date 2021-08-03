import os
import pickle
import time
import random
from selenium import webdriver
import unittest
from services.service import Service
from services.config import *

name=os.path.basename(__file__)

class FindUserTest(unittest.TestCase):

    def setUp(self):
        if CONFIG_APP.GOOGLE:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option(CONFIG_APP.EXCLUDE_OPT, CONFIG_APP.PREFS_0)
            chrome_options.add_experimental_option(CONFIG_APP.EXCLUDE_OPT_GOOGLE, CONFIG_APP.PREFS_1)            
            self.driver = webdriver.Chrome(CONFIG_APP.WEB_DRIVER_CHROME, options=chrome_options)
        else: 
            browser_profile = webdriver.FirefoxProfile()
            browser_profile.set_preference(CONFIG_APP.EXCLUDE_OPT_FIREFOX, False)
            self.driver = webdriver.Firefox(executable_path=CONFIG_APP.WEB_DRIVER_FIREFOX, firefox_profile=browser_profile)
        self.driver.get(CONFIG_APP.WEB_PAGE)

    def testPythonScript(self):
        driver=self.driver
        with open(CONFIG_APP.LOG_COOKIES, 'rb') as f:
              cookies = pickle.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie) 
        driver.refresh()
        driver.maximize_window()
        driver.implicitly_wait(CONFIG_APP.TIME_IMPLICIT)
        self.handler = Service(driver)
        self.handler.click(CONFIG_XPATHS.INPUT_SEARCH)
        time.sleep(CONFIG_APP.SLEEP_TIME)
        self.handler.writeToInputs(CONFIG_XPATHS.INPUT_SEARCH, ASSERTS_CONS.USER_FOR_TEST)
        self.handler.sendEnter(CONFIG_XPATHS.INPUT_SEARCH)
        time.sleep(CONFIG_APP.SLEEP_TIME)
        driver.get_screenshot_as_file(CONFIG_APP.EVIDENCE_PATH+str(name)+CONFIG_APP.IMG_FORMAT)
        assert ASSERTS_CONS.FIND_USER_ASSERT in driver.title
        driver.quit()

if __name__ == "__main__":
    unittest.main()