from selenium.webdriver.support.ui import Select

class Contact:

    def __init__(self, app):
        self.app=app

    def create_new(self, contact):
        wd = self.app.wd
        self.add_new_contact(wd)
        self.fill_contact_form(contact)
        # подтвердить ввод
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.go_to_page_home()

    def go_to_page_home(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and
                len( wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)  # название имени группы


    def fill_contact_form(self, contact):
        wd = self.app.wd
        # ФИО+nickname
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        # данные компании
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        # адресс 1
        self.change_field_value("address", contact.address)
        # телефоны
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        # почта
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        # даты пока пропустить
        #self.pick_year_data(contact)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("ayear", contact.ayear)
        # адресс 2
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2) # странно что "HOME" нашелся по имени "phone2"
        # заметка
        self.change_field_value("notes", contact.notes)


    #ругается на  TypeError: argument of type 'NoneType' is not iterable
    def pick_year_data(self, contact):
        wd = self.app.wd
        Select(wd.find_element_by_xpath("//div[@id='content']/form/select[1]")).select_by_visible_text(
            contact.birthday_date)
        Select(wd.find_element_by_xpath("//div[@id='content']/form/select[2]")).select_by_visible_text(
                contact.birthday_month)
        Select(wd.find_element_by_xpath("//div[@id='content']/form/select[3]")).select_by_visible_text(
                contact.anniversary_date)
        Select(wd.find_element_by_xpath("//div[@id='content']/form/select[4]")).select_by_visible_text(
                contact.anniversary_month)

    def add_new_contact(self, wd):
        wd.find_element_by_link_text("add new").click()

    def del_first_contact(self):
        wd = self.app.wd
        self.go_to_page_home()
        #выбрать 1 контакт
        wd.find_element_by_name("selected[]").click()
        #нажать на "удалить"
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.go_to_page_home()

    def mod_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.go_to_page_home()
        #выбрать 1 контакт
        wd.find_element_by_name("selected[]").click()
        # выбрать кнопку для редоктирования
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # прейти на страницу с контактами
        self.go_to_page_home()

    def count(self):
        wd = self.app.wd
        self.go_to_page_home()
        return len(wd.find_elements_by_name("selected[]"))