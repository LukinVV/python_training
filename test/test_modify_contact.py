# -*- coding: utf-8 -*-
from model.contact import Contact

def test_mod_first_cotact(app):
    app.session.login(user_name="admin", password="secret")
    app.contact.mod_first_contact(Contact(firstname="NEW NAME"))
    app.session.logout()