from model.contact import Contact
import pytest

def test_contact_add(app, json_contacts, orm, check_ui):
    contact = json_contacts
    with pytest.allure.step('Given a contact list'):
        old_contact_list = orm.get_contact_list()
    with pytest.allure.step('When I add a contact %s to the list' % contact):
        app.contact.create_new(contact)
    with pytest.allure.step('Then the new contact list is equal to the old list with the added contact'):
        new_contact_list = orm.get_contact_list()
        old_contact_list.append(contact)
        assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
        if check_ui:
            print("Проверка пользовательского интерфейса")
            assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                             key=Contact.id_or_max)
