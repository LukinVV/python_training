# -*- coding: utf-8 -*-
from model.group import Group

def test_empty_group_add(app):
    app.group.create_new(Group(name="", header="", footer=""))

def test_group_add(app):
    app.group.create_new(Group(name="NAME", header="HEADER", footer="FOOTER"))
