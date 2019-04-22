import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class editService_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_editService(self):
        # Define Login Info
        user = "instructor"
        pwd = "instructor1a"
        #Open Google Chrome
        driver = self.driver
        #Maximize Chrome window
        driver.maximize_window()
        #Open home page
        driver.get("http://hmeaton.pythonanywhere.com/")
        time.sleep(1)
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
        #Click Edit
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/table/tbody/tr/td[8]/a').click()
        #Edit service information
        elem = driver.find_element_by_id("id_description").clear()
        elem = driver.find_element_by_id("id_description")
        elem.send_keys("Turkey sandwich and beverage for 35 guests")
        elem = driver.find_element_by_id("id_service_charge").clear()
        elem = driver.find_element_by_id("id_service_charge")
        elem.send_keys("175")
        time.sleep(1)
        #Scroll to bottom of page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #Click save
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/form/button').click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
