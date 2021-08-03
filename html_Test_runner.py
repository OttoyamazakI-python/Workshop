import unittest
import sys
import LoginTest_Blank, LoginTest_MailWrong, LoginTest_NumberWrong, LoginTest_PassWrong, LoginTest_Sucess
import CategoryTest, PageTest, PersonTest, PlacesTest, WatchTest
import Perfil_Photo
import ReactionsTest, DeletePostTest
import EmptyPostTest, FindUserTest, HobbieTest, PostTest
from services.config import *
import os
 
# Import the HTMLTestRunner Module
import HtmlTestRunner
 
# Get the Present Working Directory since that is the place where the report
# would be stored
 
current_directory = os.getcwd()
 
class HTML_TestRunner_TestSuite(unittest.TestCase):
    def test_facebook(self):
 
        # Create a TestSuite comprising the two test cases
        consolidated_test = unittest.TestSuite()
 
        # Add the test cases to the Test Suite
        consolidated_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(WatchTest.WatchTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(PlacesTest.PlacesTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(PersonTest.PersonTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(PageTest.PageTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(CategoryTest.CategoryTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(LoginTest_Blank.LoginTest_Blank),
            unittest.defaultTestLoader.loadTestsFromTestCase(LoginTest_Sucess.LoginTest_Sucess),
            unittest.defaultTestLoader.loadTestsFromTestCase(Perfil_Photo.Perfil_Photo),
            unittest.defaultTestLoader.loadTestsFromTestCase(LoginTest_PassWrong.LoginTest_PassWrong),
            unittest.defaultTestLoader.loadTestsFromTestCase(LoginTest_MailWrong.LoginTest_MailWrong),
            unittest.defaultTestLoader.loadTestsFromTestCase(LoginTest_NumberWrong.LoginTest_NumberWrong),
            unittest.defaultTestLoader.loadTestsFromTestCase(ReactionsTest.ReactionsTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(DeletePostTest.DeletePostTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(EmptyPostTest.EmptyPostTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(FindUserTest.FindUserTest),
            # unittest.defaultTestLoader.loadTestsFromTestCase(HobbieTest.HobbieTest),
            unittest.defaultTestLoader.loadTestsFromTestCase(PostTest.PostTest)            
        ])

        output_file = open(current_directory + CONFIG_APP.HTML_REPORT, "w")
 
        html_runner = HtmlTestRunner.HTMLTestRunner(
            stream=output_file,
            report_title=CONFIG_APP.HTML_REPORT_TITLE,
            descriptions=CONFIG_APP.HTML_REPORT_DESCRIPTION,
        )
 
        html_runner.run(consolidated_test)
 
if __name__ == '__main__':
    unittest.main()
        
