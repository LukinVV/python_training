from model.contact import Contact
import random
import pytest


def test_del_some_contact(app, orm, check_ui):
    with pytest.allure.step('Given a group list'):
        if len(orm.get_contact_list()) == 0:
            app.contact.create_new(Contact(nickname="New"))
        old_contact_list = orm.get_contact_list()
        contact = random.choice(old_contact_list)
    with pytest.allure.step('When I delete a contact %s from the list' % contact):
        app.contact.del_contact_by_id(contact.id)
    with pytest.allure.step('Then the new contact list is equal to the old list without the deleted contact'):
        new_contact_list = orm.get_contact_list()
        old_contact_list.remove(contact)
        assert old_contact_list == new_contact_list
        if check_ui:
            print("Проверка пользовательского интерфейса")
            assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                             key=Contact.id_or_max)