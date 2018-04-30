# -*- coding: utf-8 -*-
from model.group import Group


def test_mod_first_group_name(app):
    if app.group.count() == 0:
        app.group.create_new(Group(name="NEW"))
    old_group_list = app.group.get_list_group()
    group = Group(header="NEW NAME")
    group.id = old_group_list[0].id
    # нужна проверка если имя группы None
    if group.name is None:
        group.name = old_group_list[0].name
    app.group.mod_first_group(group)
    #print(sorted(old_group_list, key=Group.id_or_max))
    assert len(old_group_list) == app.group.count()
    new_group_list = app.group.get_list_group()
    old_group_list[0] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    # print(sorted(new_group_list, key=Group.id_or_max))
    # print(sorted(old_group_list, key=Group.id_or_max))