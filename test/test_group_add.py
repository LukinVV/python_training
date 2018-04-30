# -*- coding: utf-8 -*-
from model.group import Group


def test_empty_group_add(app):
    old_group_list = app.group.get_list_group()
    # print("\n".join(map(str, old_group_list)))
    group = Group(name="", header="", footer="")
    app.group.create_new(group)
    assert len(old_group_list) + 1 == app.group.count()
    new_group_list = app.group.get_list_group()
    print(sorted(new_group_list, key=Group.id_or_max))
    old_group_list.append(group)
    #print(sorted(old_group_list, key=Group.id_or_max))
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


def test_group_add(app):
    old_group_list = app.group.get_list_group()
    # print("\n".join(map(str, old_group_list)))
    group = Group(name="NAME", header="HEADER", footer="FOOTER")
    app.group.create_new(group)
    assert len(old_group_list) + 1 == app.group.count()
    new_group_list = app.group.get_list_group()
    #print(sorted(new_group_list, key=Group.id_or_max))
    old_group_list.append(group)
    #print(sorted(old_group_list, key=Group.id_or_max))
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
