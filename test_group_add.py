# -*- coding: utf-8 -*-

from selenium import webdriver
import time, unittest
from group import Group

#firefox=webdriver.Firefox(capabilities={"marionette": False}) так и не смог заупстить в Firefox, браузер открывается
#  но ни чего не происходит

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_group_add(unittest.TestCase):
    def setUp(self):
        chrome=webdriver.Chrome() #"C:\Windows\SysWOW64\chromedriver.exe" - может пригодится
        self.wd=chrome
        self.wd.implicitly_wait(60)

    def open_start_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, user_name, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        #wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click() - видмо лишнее
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def return_to_page_groups(self, wd):
        wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def create_new_group(self, wd, group):
        # создаем группу
        wd.find_element_by_name("new").click()
        # вводим данные
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)  # название имени группы
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)  # название header
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)  # название footer
        # завершили создание новой группы
        wd.find_element_by_name("submit").click()

    def open_page_groups(self, wd):
        # открытие страницы groups
        wd.find_element_by_link_text("groups").click()

    def test_empty_group_add(self):
        wd = self.wd
        self.open_start_page(wd)
        self.login(wd, user_name="admin", password="secret")
        self.open_page_groups(wd)
        self.create_new_group(wd, Group(name="", header="", footer=""))
        self.return_to_page_groups(wd)
        self.logout(wd)

    def test_group_add(self):
        wd = self.wd
        self.open_start_page(wd)
        self.login(wd, user_name="admin", password="secret")
        self.open_page_groups(wd)
        self.create_new_group(wd, Group(name="NAME", header="HEADER", footer="FOOTER"))
        self.return_to_page_groups(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
