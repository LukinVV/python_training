# -*- coding: utf-8 -*-
from model.contact import Contact


def test_contact_add(app):
    old_contact_list = app.contact.get_list_contact()
    # print("\n".join(map(str, old_contact_list)))
    contact = Contact(
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
    )
    app.contact.create_new(contact)
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact_list = app.contact.get_list_contact()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
