from model.contact import Contact

def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(nickname="New"))
        old_contact_list = app.contact.get_list_contact()
    old_contact_list = app.contact.get_list_contact()
    app.contact.del_first_contact()
    new_contact_list = app.contact.get_list_contact()
    assert len(old_contact_list) - 1 == len(new_contact_list)