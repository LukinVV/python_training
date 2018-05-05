# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest

months = ( "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
           "November", "December")


def get_random_name():
    return "%s%s" % (get_random_string_uppercase(1), get_random_string_lowercase(3, 6))


def get_random_email():
    return "%s@%s.%s" % (get_random_string_lowercase(3, 6), get_random_string_lowercase(3, 6), get_random_string_lowercase(2, 4))


def get_random_address():
    return "%s%s" % (get_random_string_uppercase(1), get_random_string_lowercase(3, 6))


def get_random_text(max_len):
    symbols = string.ascii_letters + string.digits + " " * 10
    return "".join([random.choice(symbols) for i in range(random.randrange(max_len))])

def get_random_string_lowercase(min_len, max_len):
    return "".join([random.choice(string.ascii_lowercase) for i in range(random.randrange(min_len, max_len))])


def get_random_string_uppercase(len):
    return "".join([random.choice(string.ascii_uppercase) for i in range(len)])


def get_random_string_digits(min_len, max_len):
    return "".join([random.choice(string.digits) for i in range(random.randrange(min_len, max_len))])


def get_random_day():
    return "".join(map(str, [random.randint(1,31)]))


def get_random_year():
    return "".join(map(str, [random.randint(1980, 2000)]))

def get_random_months():
    return "".join([random.choice(months)])


contact = [Contact(
    # ФИО+nickname
    firstname=get_random_name(),
    middlename=get_random_name(),
    lastname=get_random_name(),
    nickname=get_random_name(),
    # данные компании
    title=get_random_name(),
    company=get_random_name(),
    # адресс 1
    address=get_random_address(),
    # телефоны
    home_phone=get_random_string_digits(10, 11),
    mobile_phone=get_random_string_digits(10, 11),
    work_phone=get_random_string_digits(10, 11),
    fax=get_random_string_digits(10, 11),
    # почта
    email=get_random_email(),
    email2=get_random_email(),
    email3=get_random_email(),
    homepage=get_random_email(),
    # выбор дат
    birthday_date=get_random_day(),
    birthday_month=get_random_months(),
    byear=get_random_year(),
    anniversary_date=get_random_day(),
    anniversary_month=get_random_months(),
    ayear=get_random_year(),
    # адресс 2
    address2=get_random_address(),
    secondary_phone=get_random_string_digits(10, 11),
    # заметка
    notes=get_random_text(10)), Contact(firstname="", lastname="", address="", home_phone="", work_phone="",
                                      mobile_phone="", secondary_phone="",
                                      email="", email2="", email3="")]


@pytest.mark.parametrize("contact", contact, ids=[repr(x) for x in contact])
def test_contact_add(app, contact):
    old_contact_list = app.contact.get_list_contact()
    # print(sorted(old_contact_list, key=Contact.id_or_max))
    # print("\n".join(map(str, old_contact_list)))

    app.contact.create_new(contact)
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact_list = app.contact.get_list_contact()
    # print(sorted(new_contact_list, key=Contact.id_or_max))
    old_contact_list.append(contact)
    # print(sorted(old_contact_list, key=Contact.id_or_max))
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
