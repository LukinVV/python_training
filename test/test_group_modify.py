# -*- coding: utf-8 -*-
from model.group import Group
import random
import pytest

def test_mod_group_name(app, orm, check_ui):
    with pytest.allure.step('Given a non-empty group list'):
        if len(orm.get_group_list()) == 0:
            app.group.create_new(Group(name="NEW"))
        old_group_list = orm.get_group_list()
        new_group = Group(header="NEW NAME")
        mod_group = random.choice(old_group_list)
        new_group.id = mod_group.id
    with pytest.allure.step('I modify the group %s in the list' % mod_group):
        if new_group.name is None:
            new_group.name = mod_group.name
        app.group.mod_group_by_id(new_group)
    with pytest.allure.step('the new group list is equal to the old list with the modified group'):
        new_group_list = orm.get_group_list()
        old_group_list.remove(mod_group)
        old_group_list.append(new_group)
        assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
        if check_ui:
            print("Проверка пользовательского интерфейса")
            assert sorted(new_group_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

