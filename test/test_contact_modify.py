# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_mod_some_cotact(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="New"))
    old_contact_list = app.contact.get_list_contact()
    index = randrange(len(old_contact_list))
    contact = Contact(firstname="NEW NAME")
    contact.id = old_contact_list[index].id
    if contact.firstname is None:
        contact.firstname = old_contact_list[index].firstname
    if contact.lastname is None:
        contact.lastname = old_contact_list[index].lastname
    app.contact.mod_contact_by_index(index, contact)
    # print(sorted(old_contact_list, key=Contact.id_or_max))
    assert len(old_contact_list) == app.contact.count()
    new_contact_list = app.contact.get_list_contact()
    old_contact_list[index] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    # print(sorted(old_contact_list, key=Contact.id_or_max))
    # print(sorted(new_contact_list, key=Contact.id_or_max))


def test_first_cotact(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="New"))
    old_contact_list = app.contact.get_list_contact()
    index = randrange(len(old_contact_list))
    contact = Contact(firstname="NEW NAME")
    contact.id = old_contact_list[0].id
    if contact.firstname is None:
        contact.firstname = old_contact_list[0].firstname
    if contact.lastname is None:
        contact.lastname = old_contact_list[0].lastname
    app.contact.mod_first_contact(contact)
    # print(sorted(old_contact_list, key=Contact.id_or_max))
    assert len(old_contact_list) == app.contact.count()
    new_contact_list = app.contact.get_list_contact()
    old_contact_list[0] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    # print(sorted(old_contact_list, key=Contact.id_or_max))
    # print(sorted(new_contact_list, key=Contact.id_or_max))