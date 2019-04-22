import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class addCustomer_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_addCustomer(self):
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
        #Click Customer View Details
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a').click()
        time.sleep(1)
        #Click Add Customer
        elem = driver.find_element_by_link_text("Add Customer").click()
        #Enter customer information
        elem = driver.find_element_by_id("id_cust_name")
        elem.send_keys("Bill Davis")
        elem = driver.find_element_by_id("id_organization")
        elem.send_keys("UNO")
        elem = driver.find_element_by_id("id_role")
        elem.send_keys("Administrative Assistant")
        elem = driver.find_element_by_id("id_bldgroom")
        elem.send_keys("PKI 106")
        elem = driver.find_element_by_id("id_account_number")
        elem.send_keys("5005")
        elem = driver.find_element_by_id("id_address")
        elem.send_keys("123 W Elm St")
        elem = driver.find_element_by_id("id_city")
        elem.send_keys("Omaha")
        elem = driver.find_element_by_id("id_state")
        elem.send_keys("Nebraska")
        elem = driver.find_element_by_id("id_zipcode")
        elem.send_keys("68112")
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("bdavis@unomaha.edu")
        elem = driver.find_element_by_id("id_phone_number")
        elem.send_keys("402-499-1234")
        #Click save
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/form/button').click()
        time.sleep(1)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
