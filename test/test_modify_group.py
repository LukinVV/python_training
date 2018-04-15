# -*- coding: utf-8 -*-
from model.group import Group

def test_mod_first_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group.mod_first_group(Group(name="CHANGE NAME", header="CHANGE HEADER", footer="CHANGE FOOTER"))
    app.session.logout()