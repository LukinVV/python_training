class Navigator:

    def __init__(self, app):
        self.app=app

    def open_start_page(self):
            wd = self.app.wd
            wd.get("http://localhost/addressbook/")

    def open_page_group(self):
        wd = self.app.wd
        # открытие страницы groups
        wd.find_element_by_link_text("groups").click()

    def return_to_page_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def add_new_contact(self, wd):
        wd.find_element_by_link_text("add new").click()