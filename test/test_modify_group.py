# -*- coding: utf-8 -*-
from model.group import Group

def test_mod_first_group_name(app):
    app.session.login(user_name="admin", password="secret")
    app.group.mod_first_group(Group(name="NEW NAME"))
    app.session.logout()

def test_mod_first_group_header(app):
    app.session.login(user_name="admin", password="secret")
    app.group.mod_first_group(Group(header="NEW HEADER"))
    app.session.logout()

def test_mod_first_group_footer(app):
    app.session.login(user_name="admin", password="secret")
    app.group.mod_first_group(Group(footer="NEW FOOTER"))
    app.session.logout()