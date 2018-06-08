# -*- coding: utf-8 -*-
from model.group import Group
import random
import pytest

def test_del_some_group(app, orm, check_ui):
    with pytest.allure.step('Given a group list'):
        if len(orm.get_group_list()) == 0:
            app.group.create_new(Group(name="NEW"))
        old_group_list = orm.get_group_list()
        group = random.choice(old_group_list)
    with pytest.allure.step('When I delete a group %s from the list' % group):
        app.group.del_group_by_id(group.id)
    with pytest.allure.step('Then the new group list is equal to the old list without the deleted group'):
        new_group_list = orm.get_group_list()
        old_group_list.remove(group)
        assert old_group_list == new_group_list
        if check_ui:
            print("Проверка пользовательского интерфейса")
            assert sorted(new_group_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
