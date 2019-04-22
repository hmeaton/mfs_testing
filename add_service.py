import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class addService_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_addService(self):
        # Define Login Info
        user = "instructor"
        pwd = "instructor1a"
        #Open Google Chrome
        driver = self.driver
        #Maximize Chrome window
        driver.maximize_window()
        #Open home page
        driver.get("http://hmeaton.pythonanywhere.com/")
        #Click login
        elem = driver.find_element_by_link_text("Login").click()
        # Enter username
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        # Enter password
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        #Click login
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/form/p[3]/input').click()
        time.sleep(1)
        #Click Service View Details
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a').click()
        time.sleep(1)
        #Click Add Service
        elem = driver.find_element_by_link_text("Add Service").click()
        #Enter service information
        select = Select(driver.find_element_by_id('id_cust_name'))
        select.select_by_visible_text('Bill Davis')
        elem = driver.find_element_by_id("id_service_category")
        elem.send_keys("Food Prep/Delivery")
        elem = driver.find_element_by_id("id_description")
        elem.send_keys("Turkey sandwich and beverage for 30 guests")
        elem = driver.find_element_by_id("id_location")
        elem.send_keys("PKI 215")
        elem = driver.find_element_by_id("id_setup_time")
        elem.send_keys("2019-04-22 12:00:00")
        elem = driver.find_element_by_id("id_cleanup_time")
        elem.send_keys("2019-04-22 15:00:00")
        elem = driver.find_element_by_id("id_service_charge")
        elem.send_keys("150")
        #Scroll to bottom of page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #Click save
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/form/button').click()


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
