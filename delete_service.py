import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class deleteService_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_deleteService(self):
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
        #Click Delete
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/table/tbody/tr[1]/td[9]/a').click()
        #Click OK
        alert_obj = driver.switch_to.alert
        alert_obj.accept()
        time.sleep(1)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
