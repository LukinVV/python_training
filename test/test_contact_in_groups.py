from model.contact import Contact
from model.group import Group
import random
import time


def test_add_contact_to_group(app, orm, check_ui):
    if len(orm.get_group_list()) == 0:
        app.group.create_new(Group(name="NEW"))
    group = random.choice(orm.get_group_list())
    if len(orm.get_contacts_not_in_groups(group)) == 0:
        app.contact.create_new(Contact(firstname="New"))
    contact = random.choice(orm.get_contacts_not_in_groups(group))
    if contact in orm.get_contacts_in_groups(group):
        app.contact.delete_contact_from_group(contact.id, group.id)
    app.contact.add_to_group(contact.id, group.id)
    assert contact in orm.get_contacts_in_groups(group)
    assert contact not in orm.get_contacts_not_in_groups(group)
    if check_ui:
        print("Проверка пользовательского интерфейса")
        assert sorted(orm.get_contacts_in_groups(group), key=Group.id_or_max) == sorted(
            app.contact.get_contact_list_in_group(group.id), key=Group.id_or_max)


def test_remove_contact_from_group(app, orm, check_ui):
    if len(orm.get_group_list()) == 0:
        app.group.create_new(Group(name="NEW"))
    group = random.choice(orm.get_group_list())
    if len(orm.get_contact_list()) == 0:
        app.contact.create_new(Contact(firstname="New"))
    if len(orm.get_contacts_in_groups(group)) == 0:
        contact = random.choice(orm.get_contact_list())
        # time.sleep(1)  # иногда "падает" ссылаясь на что не может найти элемент
        app.contact.add_to_group(contact.id, group.id)
    else:
        contact = random.choice(orm.get_contacts_in_groups(group))
    if contact not in orm.get_contacts_in_groups(group):
        app.contact.add_to_group(contact.id, group.id)
        # time.sleep(1)  # иногда "падает" ссылаясь на что не может найти элемент
    app.contact.remove_from_group(contact.id, group.id)
    assert contact in orm.get_contacts_not_in_groups(group)
    assert contact not in orm.get_contacts_in_groups(group)
    if check_ui:
        print("Проверка пользовательского интерфейса")
        # time.sleep(1)  # иногда "падает" ссылаясь на
        assert sorted(orm.get_contacts_in_groups(group), key=Group.id_or_max) == sorted(
            app.contact.get_contact_list_in_group(group.id), key=Group.id_or_max)
