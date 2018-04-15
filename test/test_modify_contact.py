# -*- coding: utf-8 -*-
from model.contact import Contact

def test_mod_first_cotact(app):
    app.session.login(user_name="admin", password="secret")
    app.contact.mod_first_contact(Contact(
        # ФИО+nickname
        firstname="CHANGE Владислав",
        middlename="",
        lastname="CHANGE Лукин",
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
    app.session.logout()