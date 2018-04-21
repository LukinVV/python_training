# -*- coding: utf-8 -*-
from model.contact import Contact

def test_mod_first_cotact(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="New"))
    app.contact.mod_first_contact(Contact(firstname="NEW NAME"))