from model.contact import Contact

def test_contact_add(app, json_contacts, db, check_ui):
    contact = json_contacts
    old_contact_list = db.get_contact_list()
    app.contact.create_new(contact)
    new_contact_list = db.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        print("Проверка пользовательского интерфейса")
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)
