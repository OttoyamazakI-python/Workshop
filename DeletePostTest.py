import os
from selenium import webdriver
import unittest
from services.service import Service
from services.config import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time
name=os.path.basename(__file__)

class DeletePostTest(unittest.TestCase):

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
        self.handler.click(CONFIG_XPATHS.PERFIL_LOCATOR)
        self.handler.click(CONFIG_XPATHS.BTN_FOTO_PERFIL)
        if not CONFIG_APP.GOOGLE:
            time.sleep(CONFIG_APP.SLEEP_TIME)
            self.handler.scrollby1(CONFIG_APP.SCROLL_AMOUNT)
        for path in CONFIG_XPATHS.PATH_ELIMINAR[CONFIG_APP.INCREMENTAL_INIT]:
            for elemento in CONFIG_XPATHS.PATH_ELIMINAR[CONFIG_APP.INITIAL_VALUE]:
                self.handler.click(elemento)
            self.handler.click(path)
        driver.get_screenshot_as_file(CONFIG_APP.EVIDENCE_PATH+name+CONFIG_APP.IMG_FORMAT)
        trash=driver.find_element_by_xpath(CONFIG_XPATHS.COMPROBACION_PAPELERA).text
        self.assertEqual(ASSERTS_CONS.DELETE_POST_ASSERT, trash, ASSERTS_CONS.ASSERT_PAPELERA)
        driver.quit()

if __name__ == "__main__":
    unittest.main()