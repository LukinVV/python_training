from datetime import datetime
from pony.orm import *
from pymysql.converters import encoders, decoders, convert_mysql_timestamp
from model.contact import Contact
from model.group import Group


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        first_name = Optional(str, column='firstname')
        last_name = Optional(str, column='lastname')
        address = Optional(str, column='address')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        home_phone = Optional(str, column='home')
        mobile_phone = Optional(str, column='mobile')
        work_phone = Optional(str, column='work')
        fax = Optional(str, column='fax')
        secondary_phone = Optional(str, column='phone2')
        deprecated = Optional(datetime, column='deprecated')

    def __init__(self, host, name, user, password):
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=conv)
        self.db.generate_mapping()

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)

        return list(map(convert, groups))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.first_name, lastname=contact.last_name,
                           address=contact.address, email=contact.email, email2=contact.email2, email3=contact.email3,
                           home_phone=contact.home_phone, work_phone=contact.work_phone,
                           mobile_phone=contact.mobile_phone, fax=contact.fax, secondary_phone=contact.secondary_phone)

        return list(map(convert, contacts))
