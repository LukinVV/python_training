from model.contact import Contact
from model.group import Group
import random

def test_add_contact_to_group(app, orm):
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
    orm.get_contacts_not_in_groups(group).append(contact)
    sorted(orm.get_contacts_not_in_groups(group), key=Contact.id_or_max) == sorted(orm.get_contacts_in_groups(group),
                                                                                   key=Contact.id_or_max)



def test_remove_contact_from_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create_new(Group(name="NEW"))
    group = random.choice(orm.get_group_list())
    if len(orm.get_contact_list()) == 0:
        app.contact.create_new(Contact(firstname="New"))
    if len(orm.get_contacts_in_groups(group)) == 0:
        contact = random.choice(orm.get_contact_list())
        app.contact.add_to_group(contact.id, group.id)
    else:
        contact = random.choice(orm.get_contacts_in_groups(group))
    if contact not in orm.get_contacts_in_groups(group):
        app.contact.add_to_group(contact.id, group.id)
    app.contact.remove_from_group(contact.id, group.id)
    assert contact in orm.get_contacts_not_in_groups(group)
    assert contact not in orm.get_contacts_in_groups(group)
    orm.get_contacts_not_in_groups(group).remove(contact)
    sorted(orm.get_contacts_not_in_groups(group), key=Contact.id_or_max) == sorted(orm.get_contacts_in_groups(group),
                                                                                   key=Contact.id_or_max)