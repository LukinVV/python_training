class Group:

    def __init__(self, app):
        self.app=app

    def create_new(self, group):
        wd = self.app.wd
        self.app.navigator.open_page_group()
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
        self.app.navigator.return_to_page_group()