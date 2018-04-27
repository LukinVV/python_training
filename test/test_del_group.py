# -*- coding: utf-8 -*-
from model.group import Group

def test_del_first_group(app):
    if app.group.count() == 0:
        app.group.create_new(Group(name="NEW"))
        old_group_list = app.group.get_list_group()
    old_group_list = app.group.get_list_group()
    app.group.del_first_group()
    new_group_list=app.group.get_list_group()
    assert len(old_group_list)-1 == len(new_group_list)