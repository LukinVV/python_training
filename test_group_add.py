# -*- coding: utf-8 -*-
# from selenium.webdriver.firefox.webdriver import WebDriver так и не смог заупстить в Firefox, бразер открывается
#  но ни чего не происходит
# from selenium.webdriver.chrome.webdriver import WebDriver

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

chrome=webdriver.Chrome()

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_group_add(unittest.TestCase):
    def setUp(self):
        self.wd = chrome
        self.wd.implicitly_wait(60)
    
    def test_test_group_add(self):
        success = True
        wd = self.wd
        wd.get("http://localhost/addressbook/") # переход к тестовой странице
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("asda") # название имени группы
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("asdasd") # название header
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("asdasd") # название footer
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_link_text("Logout").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
