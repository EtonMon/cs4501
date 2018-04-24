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

    def test_signup_and_login_and_logout(self):
        driver = self.driver

        driver.get('http://web:8000/home/')

        register_button = driver.find_element_by_xpath('/html/body/div[1]/div/p[2]/a')

        register_button.click()

        username_input = driver.find_element_by_id('id_username')
        pw_input = driver.find_element_by_id('id_password')
        first_name_input = driver.find_element_by_id('id_first_name')
        last_name_input = driver.find_element_by_id('id_last_name')
        submit_btn = driver.find_element_by_id('submit-id-submit')

        username_input.send_keys("username")
        pw_input.send_keys("password")
        first_name_input.send_keys("john")
        last_name_input.send_keys("smith")
        submit_btn.click()

        driver.get('http://web:8000/login/')

        username_input = driver.find_element_by_id('id_username')
        pw_input = driver.find_element_by_id('id_password')
        submit_btn = driver.find_element_by_id('submit-id-submit')

        username_input.send_keys("username")
        pw_input.send_keys("password")

        submit_btn.click()

        driver.get('http://web:8000/home/')

        home_page_title = driver.find_element_by_xpath('/html/body/div[1]/div/h1')

        self.assertEqual("Welcome username!", home_page_title.get_attribute('innerHTML'))

        logout_button = driver.find_element_by_xpath('/html/body/nav/div/ul[2]/li/a/b')

        logout_button.click()

        driver.get('http://web:8000/home/')

        home_page_title_post_logout = driver.find_element_by_xpath('/html/body/div[1]/div/h1')

        self.assertEqual("Share your interests", home_page_title_post_logout.get_attribute('innerHTML'))
        
    def test_listing_creation_and_searcn(self):
        driver = self.driver
        driver.get('http://web:8000/signup/')

        username_input = driver.find_element_by_id('id_username')
        pw_input = driver.find_element_by_id('id_password')
        first_name_input = driver.find_element_by_id('id_first_name')
        last_name_input = driver.find_element_by_id('id_last_name')
        submit_btn = driver.find_element_by_id('submit-id-submit')

        username_input.send_keys("username2")
        pw_input.send_keys("password2")
        first_name_input.send_keys("john")
        last_name_input.send_keys("smith")
        submit_btn.click()

        driver.get('http://web:8000/login/')

        username_input = driver.find_element_by_id('id_username')
        pw_input = driver.find_element_by_id('id_password')
        submit_btn = driver.find_element_by_id('submit-id-submit')

        username_input.send_keys("username2")
        pw_input.send_keys("password2")

        submit_btn.click()

        driver.get('http://web:8000/songs/create/')

        title_input = driver.find_element_by_id('id_title')
        artist_input = driver.find_element_by_id('id_artists')
        submit_btn = driver.find_element_by_id('submit-id-submit')

        title_input.send_keys("mysong")
        artist_input.send_keys("anartist")
        submit_btn.click()

        driver.get('http://web:8000/home/')

        search_input = driver.find_element_by_id('search')
        submit_btn = driver.find_element_by_xpath('/html/body/nav/div/form/button')

        search_input.send_keys("mysong")
        submit_btn.click()

        song_search = driver.find_element_by_xpath('/html/body/div[1]/div/a')

        self.assertEqual(" mysong, anartist,  Song ", song_search.get_attribute('innerHTML'))

    def tearDown(self):
        self.driver.close()

time.sleep(20)

if __name__ == "__main__":
    unittest.main()


 # Let the user actually see something!
