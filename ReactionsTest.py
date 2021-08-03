import os
from selenium import webdriver
import unittest
from services.service import Service
from services.config import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pickle
import time
name=os.path.basename(__file__)

class ReactionsTest(unittest.TestCase):

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
        if not CONFIG_APP.GOOGLE:
            self.handler.scrollby1(CONFIG_APP.SCROLL_SMALL_AMOUNT)
        i=CONFIG_APP.INITIAL_VALUE
        for reaction, asert in zip(CONFIG_XPATHS.REACTIONS, ASSERTS_CONS.asserts_reactions):
                self.handler.hover(CONFIG_XPATHS.BTN_ELEMENT_LIKE)
                time.sleep(1)
                self.handler.click(reaction)
                test_name=driver.find_element_by_xpath(CONFIG_XPATHS.BTN_ELEMENT_LIKE).text
                self.assertEqual(asert, test_name, ASSERTS_CONS.FAIL_REACTION)
                driver.get_screenshot_as_file(CONFIG_APP.EVIDENCE_PATH+str(name)+CONFIG_APP.IMG_FORMAT)
        driver.quit()

if __name__ == "__main__":
    unittest.main()