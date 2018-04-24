'''from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('http://localhost:8000/home/')
browser.get('http://localhost:8000/home/')
'''
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
           command_executor='http://selenium-chrome:4444/wd/hub',
           desired_capabilities=DesiredCapabilities.CHROME)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get('http://web:8000/home/')
        # song_link = driver.find_element_by_class_name('container')
        # self.assertEqual(song_link, True)
        self.assertIn("Home", driver.title)
        # elem = driver.find_element_by_name("q")
        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

time.sleep(20)

if __name__ == "__main__":
    unittest.main()


 # Let the user actually see something!
