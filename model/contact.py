from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None,
                 title=None, company=None, address=None, home=None, mobile=None, work=None, fax=None,
                 email=None, email2=None, email3=None, homepage=None,
                 birthday_date=None, birthday_month=None, anniversary_date=None, anniversary_month=None,
                 byear=None, ayear=None, address2=None, phone2=None, notes=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthday_date = birthday_date
        self.birthday_month = birthday_month
        self.anniversary_date = anniversary_date
        self.anniversary_month = anniversary_month
        self.byear = byear
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "[lastname= %s ; firstname= %s ; id= %s]" % (self.lastname, self.firstname, self.id)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    # def __eq__(self, other): -
    #     return self.lastname == other.lastname and self.firstname == other.firstname and
    # (self.id is None or other.id is None or self.id == other.id)
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) \
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)
