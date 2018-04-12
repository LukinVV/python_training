from selenium import webdriver
from selenium.webdriver.support.ui import Select

class Application:

    def __init__(self):
        #firefox=webdriver.Firefox(capabilities={"marionette": False})
        chrome=webdriver.Chrome() #"C:\Windows\SysWOW64\chromedriver.exe" - может пригодится
        self.wd=chrome
        self.wd.implicitly_wait(60)

    def open_start_page(self):
            wd = self.wd
            wd.get("http://localhost/addressbook/")

    def login(self, user_name, password):
        wd = self.wd
        self.open_start_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def return_to_page_groups(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def create_new_group(self, group):
        wd = self.wd
        self.open_page_groups()
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
        self.return_to_page_groups()

    def open_page_groups(self):
        wd = self.wd
        # открытие страницы groups
        wd.find_element_by_link_text("groups").click()

    def destroy(self):
        self.wd.quit()

    def contact(self, contact):
        wd = self.wd
        self.add_new_contact(wd)
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