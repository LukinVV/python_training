# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time, unittest
from contact import Contact


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_contact_add(unittest.TestCase):
    def setUp(self):
        #chrome=webdriver.Chrome()
        #self.wd=chrome
        #self.wd = webdriver.Firefox(capabilities={"marionette": False, "proxy": {"proxyType": "DIRECT"}}, firefox_profile=fp)
        firefox=webdriver.Firefox(capabilities={"marionette": False}) # запустил Firefox на рабочем компе
        self.wd=firefox
        self.wd.implicitly_wait(60)

    def test_test_contact_add(self):
        wd = self.wd

        self.open_start_page(wd)
        self.login(wd, user_name="admin", password="secret")
        self.add_new_contact(wd)

        self.contact(wd, Contact(
            # ФИО+nickname
            firstname="Владислав",
            middlename="",
            lastname="Лукин",
            nickname="tester",
            # данные компании
            title="junior",
            company="sirena-travel",
            # адресс 1
            address="Moscow",
            # телефоны
            home="8495123456",
            mobile="79265314806",
            work="89265314806",
            fax="+79265314806",
            # почта
            email="lukinvv@inbox.ru",
            email2="lukinvv2@inbox.ru",
            email3="lukinvv3@inbox.ru",
            homepage="yandex.ru",
            # выбор дат
            birthday_date="13",
            birthday_month="November",
            byear="1991",
            anniversary_date="31",
            anniversary_month="November",
            ayear="2000",
            # адресс 2
            address2="Россия",
            phone2="STREET",
            # заметка
            notes="testin test"
        ))

        self.logout(wd)

    def contact(self, wd, contact):
        # ФИО+nickname
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # данные компании
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        # адресс 1
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        # телефоны
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        # почта
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # выбор дат
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]").is_selected():
            Select(wd.find_element_by_xpath("//div[@id='content']/form/select[1]")).select_by_visible_text(
                contact.birthday_date)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]").is_selected():
            Select(wd.find_element_by_xpath("//div[@id='content']/form/select[2]")).select_by_visible_text(
                contact.birthday_month)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]").is_selected():
            Select(wd.find_element_by_xpath("//div[@id='content']/form/select[3]")).select_by_visible_text(
                contact.anniversary_date)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]").is_selected():
            Select(wd.find_element_by_xpath("//div[@id='content']/form/select[4]")).select_by_visible_text(
                contact.anniversary_month)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        wd.find_element_by_name("theform").click()
        # адресс 2
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()  # странно что "HOME" нашелся по имени "phone2"
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        # заметка
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # подтвердить ввод
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # прейти на страницу с контактами
        wd.find_element_by_link_text("home").click()

    def add_new_contact(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, user_name, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        #wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_start_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
