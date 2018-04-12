# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application

#создание фикстуры
@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_contact_add(app):
    app.login(user_name="admin", password="secret")
    app.contact(Contact(
        # ФИО+nickname
        firstname="Владислав",
        middlename="",
        lastname="Лукин",
        nickname="tester",
        # данные компании
        title="junior",
        company="sirena-travel",
        # адресс 1
        address="Moscow",
        # телефоны
        home="8495123456",
        mobile="79265314806",
        work="89265314806",
        fax="+79265314806",
        # почта
        email="lukinvv@inbox.ru",
        email2="lukinvv2@inbox.ru",
        email3="lukinvv3@inbox.ru",
        homepage="yandex.ru",
        # выбор дат
        birthday_date="13",
        birthday_month="November",
        byear="1991",
        anniversary_date="31",
        anniversary_month="November",
        ayear="2000",
        # адресс 2
        address2="Россия",
        phone2="STREET",
        # заметка
        notes="testin test"
    ))
    app.logout()