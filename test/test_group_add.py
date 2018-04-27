# -*- coding: utf-8 -*-
from model.group import Group

def test_empty_group_add(app):
    old_group_list = app.group.get_list_group()
    app.group.create_new(Group(name="", header="", footer=""))
    new_group_list=app.group.get_list_group()
    assert len(old_group_list)+1 == len(new_group_list)

def test_group_add(app):
    old_group_list = app.group.get_list_group()
    app.group.create_new(Group(name="NAME", header="HEADER", footer="FOOTER"))
    new_group_list=app.group.get_list_group()
    assert len(old_group_list)+1 == len(new_group_list)