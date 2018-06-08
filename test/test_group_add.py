from model.group import Group
import pytest

def test_group_add(app, orm, json_groups, check_ui):
    group = json_groups
    with pytest.allure.step('Given a group list'):
        old_group_list = orm.get_group_list()
    with pytest.allure.step('When I add a group %s to the list' % group):
        app.group.create_new(group)
    with pytest.allure.step('Then the new group list is equal to the old list with the added group'):
        new_group_list = orm.get_group_list()
        old_group_list.append(group)
        assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
        if check_ui:
            print("Проверка пользовательского интерфейса")
            assert sorted(new_group_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
