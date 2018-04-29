# -*- coding: utf-8 -*-
from model.contact import Contact


def test_mod_first_cotact(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="New"))
    old_contact_list = app.contact.get_list_contact()
    contact = Contact(firstname="NEW NAME")
    contact.id = old_contact_list[0].id
    if contact.firstname is None:
        contact.firstname = old_contact_list[0].firstname
    if contact.lastname is None:
        contact.lastname = old_contact_list[0].lastname
    app.contact.mod_first_contact(contact)
    # print(sorted(old_contact_list, key=Contact.id_or_max))
    new_contact_list = app.contact.get_list_contact()
    assert len(old_contact_list) == len(new_contact_list)
    old_contact_list[0] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    # print(sorted(old_contact_list, key=Contact.id_or_max))
    # print(sorted(new_contact_list, key=Contact.id_or_max))

# def test_mod_first_cotact_birthday_date(app):
#     if app.contact.count() == 0:
#         app.contact.create_new(Contact(firstname="New"))
#     old_contact_list = app.contact.get_list_contact()
#     app.contact.mod_first_contact(Contact(birthday_date="29"))
#     new_contact_list = app.contact.get_list_contact()
#     assert len(old_contact_list) == len(new_contact_list)
