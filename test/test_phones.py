from model.contact import Contact


def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="New",
                                       home_phone="8495123456",
                                       mobile_phone="79265314806",
                                       work_phone="89265314806",
                                       fax="+79265314806",
                                       secondary_phone="199144654456"))
    contact_from_home_page = app.contact.get_list_contact()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == \
           app.contact.merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="New",
                                       home_phone="8495123456",
                                       mobile_phone="79265314806",
                                       work_phone="89265314806",
                                       fax="+79265314806",
                                       secondary_phone="199144654456"))
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    if contact_from_view_page.home_phone is None:
        contact_from_view_page.home_phone = contact_from_edit_page.home_phone
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.secondary_phone == contact_from_edit_page.secondary_phone
