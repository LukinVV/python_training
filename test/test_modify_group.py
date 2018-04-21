# -*- coding: utf-8 -*-

from model.group import Group

def test_mod_first_group_name(app):
    app.group.mod_first_group(Group(name="NEW NAME"))

def test_mod_first_group_header(app):
    app.group.mod_first_group(Group(header="NEW HEADER"))

def test_mod_first_group_footer(app):
    app.group.mod_first_group(Group(footer="NEW FOOTER"))