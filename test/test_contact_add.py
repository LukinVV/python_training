from model.contact import Contact

def test_contact_add(app, data_contacts):
    old_contact_list = app.contact.get_list_contact()
    contact = data_contacts
    # print(sorted(old_contact_list, key=Contact.id_or_max))
    # print("\n".join(map(str, old_contact_list)))

    app.contact.create_new(contact)
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact_list = app.contact.get_list_contact()
    # print(sorted(new_contact_list, key=Contact.id_or_max))
    old_contact_list.append(contact)
    # print(sorted(old_contact_list, key=Contact.id_or_max))
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
