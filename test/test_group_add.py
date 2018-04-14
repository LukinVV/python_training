# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application

#создание фикстуры
@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_empty_group_add(app):
    app.login(user_name="admin", password="secret")
    app.create_new_group(Group(name="", header="", footer=""))
    app.logout()

def test_group_add(app):
    app.login(user_name="admin", password="secret")
    app.create_new_group(Group(name="NAME", header="HEADER", footer="FOOTER"))
    app.logout()
