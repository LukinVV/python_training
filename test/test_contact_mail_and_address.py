from random import randrange
from model.contact import Contact


def test_verify_random_contact_on_home_page(app):
    if app.contact.count() == 0:
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
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_from_home_page_by_index(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.first_name == contact_from_edit_page.firstname
    assert contact_from_home_page.last_name == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == \
           app.contact.merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == \
           app.contact.merge_phones_like_on_home_page(contact_from_edit_page)
