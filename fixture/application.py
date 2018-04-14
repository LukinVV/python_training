from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import Group
from fixture.contact import Contact

class Application:

    def __init__(self):
        #firefox=webdriver.Firefox(capabilities={"marionette": False})
        chrome=webdriver.Chrome() #"C:\Windows\SysWOW64\chromedriver.exe" - может пригодится
        self.wd=chrome
        self.session=SessionHelper(self)
        self.group=Group(self)
        self.contact=Contact(self)
        self.wd.implicitly_wait(60)

    def open_start_page(self):
            wd = self.wd
            wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()