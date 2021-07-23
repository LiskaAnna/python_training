import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated = '0000-00-00 00:00:0'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_contact_by_id(self, id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, home, mobile, work, fax, email, email2, email3 from addressbook where id = " + id + " and deprecated = '0000-00-00 00:00:0'")
            for row in cursor:
                (id, firstname, lastname, home_phone, mobile, work_phone, phone2, email, email2, email3) = row
        finally:
            cursor.close()
        return Contact(id=str(id), firstname=firstname, lastname=lastname, home_phone=home_phone, mobile=mobile, work_phone=work_phone, phone2=phone2, email=email, email2=email2, email3=email3)

    def check_contact_in_group(self, contactid, groupid):
        cursor = self.connection.cursor()
        try:
            cursor.execute("select count(*) as count from address_in_groups where id = " + contactid + " and group_id = " + groupid + " and deprecated = '0000-00-00 00:00:0'")
            for row in cursor:
                (count) = row
        finally:
            cursor.close()
        return count[0] == 1

    def destroy(self):
            self.connection.close()
