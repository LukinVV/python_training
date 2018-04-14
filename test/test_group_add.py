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
    app.session.login(user_name="admin", password="secret")
    app.group.create_new(Group(name="", header="", footer=""))
    app.session.logout()

def test_group_add(app):
    app.session.login(user_name="admin", password="secret")
    app.group.create_new(Group(name="NAME", header="HEADER", footer="FOOTER"))
    app.session.logout()