from model.group import Group

def test_group_add(app, db, json_groups):
    group = json_groups
    old_group_list = db.get_group_list()
    app.group.create_new(group)
    new_group_list = db.get_group_list()
    old_group_list.append(group)
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
