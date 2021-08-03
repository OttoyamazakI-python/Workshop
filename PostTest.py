import os
import pickle
import time
import random
from selenium import webdriver
import unittest
from services.service import Service
from services.config import *

name=os.path.basename(__file__)

class PostTest(unittest.TestCase):

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
        driver.implicitly_wait(CONFIG_APP.TIME_IMPLICIT)
        driver.maximize_window()
        self.handler = Service(driver)
        with open(CONFIG_APP.LOG_COOKIES, 'rb') as f:
            cookies = pickle.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie) 
        driver.refresh()
        self.handler = Service(driver)
        self.handler.click(CONFIG_XPATHS.OPEN_POST)
        time.sleep(CONFIG_APP.SLEEP_TIME)
        variation = ' ' + str(random.random())
        self.handler.writeToInputs(CONFIG_XPATHS.POST_FIELD, ASSERTS_CONS.HELLO_POST_BASE + variation)
        self.handler.click(CONFIG_XPATHS.POST_BUTTON)
        driver.get_screenshot_as_file(CONFIG_APP.EVIDENCE_PATH+str(name)+CONFIG_APP.IMG_FORMAT)
        time.sleep(CONFIG_APP.SLEEP_TIME)
        assert driver.find_elements_by_xpath(CONFIG_XPATHS.POST_TXT + ASSERTS_CONS.HELLO_POST_BASE + variation + "')]")
        driver.quit()

if __name__ == "__main__":
    unittest.main()