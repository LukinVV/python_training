# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_mod_group_name(app):
    if app.group.count() == 0:
        app.group.create_new(Group(name="NEW"))
    old_group_list = app.group.get_group_list()
    index = randrange(len(old_group_list))
    group = Group(header="NEW NAME")
    group.id = old_group_list[index].id
    # нужна проверка если имя группы None
    if group.name is None:
        group.name = old_group_list[index].name
    app.group.mod_group_by_index(index, group)
    #print(sorted(old_group_list, key=Group.id_or_max))
    assert len(old_group_list) == app.group.count()
    new_group_list = app.group.get_group_list()
    old_group_list[index] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    # print(sorted(new_group_list, key=Group.id_or_max))
    # print(sorted(old_group_list, key=Group.id_or_max))

