import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class editCustomer_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_editCustomer(self):
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
        time.sleep(1)
        #Click login
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div/form/p[3]/input').click()
        time.sleep(1)
        #Click Customer View Details
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a').click()
        time.sleep(1)
        #Click Edit
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/table/tbody/tr[1]/td[12]/a').click()
        #Edit customer information
        elem = driver.find_element_by_id("id_role").clear()
        elem = driver.find_element_by_id("id_role")
        elem.send_keys("Executive Assistant")
        elem = driver.find_element_by_id("id_bldgroom").clear()
        elem = driver.find_element_by_id("id_bldgroom")
        elem.send_keys("PKI 299")
        elem = driver.find_element_by_id("id_phone_number").clear()
        elem = driver.find_element_by_id("id_phone_number")
        elem.send_keys("402-499-4321")
        time.sleep(2)
        #Click save
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/form/button').click()
        time.sleep(1)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
