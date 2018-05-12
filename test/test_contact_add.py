# -*- coding: utf-8 -*-
from model.contact import Contact
from data.contact_add import contact
import pytest


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
