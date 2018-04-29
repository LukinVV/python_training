from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        # firefox=webdriver.Firefox(capabilities={"marionette": False})
        chrome = webdriver.Chrome(
            "C:\Windows\SysWOW64\chromedriver.exe")  # "C:\Windows\SysWOW64\chromedriver.exe" - может пригодится
        self.wd = chrome
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        # self.wd.implicitly_wait(5) - для учебного приложения не нужно

    def destroy(self):
        self.wd.quit()

    def is_vald(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
