# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_del_first_group(app):
    if app.group.count() == 0:
        app.group.create_new(Group(name="NEW"))
    old_group_list = app.group.get_list_group()
    app.group.del_first_group()
    assert len(old_group_list) - 1 == app.group.count()
    new_group_list = app.group.get_list_group()
    old_group_list[0:1] = []
    assert old_group_list == new_group_list

def test_del_some_group(app):
    if app.group.count() == 0:
        app.group.create_new(Group(name="NEW"))
    old_group_list = app.group.get_list_group()
    index = randrange(len(old_group_list))
    app.group.del_group_by_index(index)
    assert len(old_group_list) - 1 == app.group.count()
    new_group_list = app.group.get_list_group()
    old_group_list[index:index+1] = []
    assert old_group_list == new_group_list