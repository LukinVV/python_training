# -*- coding: utf-8 -*-

from selenium import webdriver
import time, unittest

chrome=webdriver.Chrome()
#firefox=webdriver.Firefox(capabilities={"marionette": False}) так и не смог заупстить в Firefox, бразер открывается
#  но ни чего не происходит

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

    def open_start_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd):
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

    def return_to_page_groups(self, wd):
        wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        # логаут
        wd.find_element_by_link_text("Logout").click()

    def create_new_group(self, wd):
        # создание новой группы
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("asda")  # название имени группы
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("asdasd")  # название header
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("asdasd")  # название footer
        # завершили создание новой группы
        wd.find_element_by_name("submit").click()

    def open_page_groups(self, wd):
        # открытие страницы groups
        wd.find_element_by_link_text("groups").click()

    def tearDown(self):
        self.wd.quit()

    def test_test_group_add(self):
        wd = self.wd
        self.open_start_page(wd)
        self.login(wd)
        self.open_page_groups(wd)
        self.create_new_group(wd)
        self.return_to_page_groups(wd)
        self.logout(wd)

if __name__ == '__main__':
    unittest.main()
