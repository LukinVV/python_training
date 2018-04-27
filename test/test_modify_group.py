# -*- coding: utf-8 -*-

from model.group import Group


def test_mod_first_group_name(app):
    if app.group.count() == 0:
        app.group.create_new(Group(name="NEW"))
        old_group_list = app.group.get_list_group()
    old_group_list = app.group.get_list_group()
    app.group.mod_first_group(Group(name="NEW NAME"))
    new_group_list=app.group.get_list_group()
    assert len(old_group_list) == len(new_group_list)

def test_mod_first_group_header(app):
    if app.group.count() == 0:
        app.group.create_new(Group(header="NEW"))
        old_group_list = app.group.get_list_group()
    old_group_list = app.group.get_list_group()
    app.group.mod_first_group(Group(header="NEW HEADER"))
    new_group_list=app.group.get_list_group()
    assert len(old_group_list) == len(new_group_list)

def test_mod_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create_new(Group(footer="NEW"))
    app.group.mod_first_group(Group(footer="NEW FOOTER"))
