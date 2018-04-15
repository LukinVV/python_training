# -*- coding: utf-8 -*-
from model.group import Group

def test_empty_group_add(app):
    app.session.login(user_name="admin", password="secret")
    app.group.create_new(Group(name="", header="", footer=""))
    app.session.logout()

def test_group_add(app):
    app.session.login(user_name="admin", password="secret")
    app.group.create_new(Group(name="NAME", header="HEADER", footer="FOOTER"))
    app.session.logout()
