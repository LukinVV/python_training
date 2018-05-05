# -*- coding: utf-8 -*-
import random
import string
import pytest
from model.group import Group


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])

#testdata
# group = [Group(name="", header="", footer="")]+[Group(name=random_string('name', 10),
#                    header=random_string('header', 20), footer=random_string('footer', 20)) for i in range(5)]

group_new = [Group(name=name, header=header, footer=footer)
             for name in ["", random_string('name', 10)]
             for header in ["", random_string('header', 10)]
             for footer in ["", random_string('footer', 10)]
             ]

@pytest.mark.parametrize("group", group_new, ids=[repr(x) for x in group_new])
def test_group_add(app, group):
    old_group_list = app.group.get_list_group()
    # print("\n".join(map(str, old_group_list)))
    app.group.create_new(group)
    assert len(old_group_list) + 1 == app.group.count()
    new_group_list = app.group.get_list_group()
    # print(sorted(new_group_list, key=Group.id_or_max))
    old_group_list.append(group)
    # print(sorted(old_group_list, key=Group.id_or_max))
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
