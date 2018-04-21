# -*- coding: utf-8 -*-
from model.contact import Contact

def test_mod_first_cotact(app):
    app.contact.mod_first_contact(Contact(firstname="NEW NAME"))