# -*- coding: utf-8 -*-
from model.group import Group

def test_del_first_group(app):
    if app.group.count() == 0:
        app.group.create_new(Group(name="NEW"))
    app.group.del_first_group()