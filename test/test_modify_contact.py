# -*- coding: utf-8 -*-
from model.contact import Contact

def test_mod_first_cotact(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="New"))
        old_contact_list = app.contact.get_list_contact()
    old_contact_list = app.contact.get_list_contact()
    app.contact.mod_first_contact(Contact(firstname="NEW NAME"))

def test_mod_first_cotact_birthday_date(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="New"))
        old_contact_list = app.contact.get_list_contact()
    old_contact_list = app.contact.get_list_contact()
    app.contact.mod_first_contact(Contact(birthday_date="29"))
    new_contact_list = app.contact.get_list_contact()
    assert len(old_contact_list) == len(new_contact_list)