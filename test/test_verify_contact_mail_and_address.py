from model.contact import Contact


def test_verify_random_contact_on_home_page(app, orm):
    if len(orm.get_group_list()) == 0:
        app.contact.create_new(Contact(
            # ФИО+nickname
            firstname="Владислав",
            middlename="",
            lastname="sadasda",
            nickname="tester",
            # данные компании
            title="junior",
            company="sirena-travel",
            # адресс 1
            address="Moscow",
            # телефоны
            home_phone="8495123456",
            mobile_phone="79265314806",
            work_phone="89265314806",
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
            secondary_phone="199144654456",
            # заметка
            notes="testin test"
        ))
    contacts_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_db = sorted(orm.get_contact_list(), key=Contact.id_or_max)
    assert len(contacts_ui) == len(contacts_db)
    for i in range(len(contacts_ui)):
        assert contacts_ui[i].firstname == contacts_db[i].firstname
        assert contacts_ui[i].lastname == contacts_db[i].lastname
        assert contacts_ui[i].address == contacts_db[i].address
        assert contacts_ui[i].all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(contacts_db[i])
        assert contacts_ui[i].all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contacts_db[i])


