import os
from time import sleep
from selenium import webdriver
import unittest
from services.service import Service
from services.config import *

name=os.path.basename(__file__)

class PersonTest(unittest.TestCase):

    def setUp(self):
        if CONFIG_APP.GOOGLE:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option(CONFIG_APP.EXCLUDE_OPT, CONFIG_APP.PREFS_0)
            self.driver = webdriver.Chrome(CONFIG_APP.WEB_DRIVER_CHROME, options=chrome_options)
        else: 
            self.driver = webdriver.Firefox(executable_path=CONFIG_APP.WEB_DRIVER_FIREFOX)
        self.driver.get(CONFIG_APP.WEB_PAGE)

    def testPythonScript(self):
        driver=self.driver
        driver.maximize_window()
        driver.implicitly_wait(CONFIG_APP.TIME_IMPLICIT)
        self.handler = Service(driver)
        if not CONFIG_APP.GOOGLE:
            self.handler.scroll_down()
        self.handler.click(CONFIG_XPATHS.A_PERSONS)
        sleep(CONFIG_APP.SLEEP_TIME)
        driver.get_screenshot_as_file(CONFIG_APP.EVIDENCE_PATH+str(name)+CONFIG_APP.IMG_FORMAT)
        assert ASSERTS_CONS.PERSON_ASSERT in driver.title
        driver.quit()

if __name__ == "__main__":
    unittest.main()