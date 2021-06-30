# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=firstname, lastname=lastname)
    for firstname in ["", random_string("firstname", 10)]
    for lastname in ["", random_string("lastname", 20)]
    #for middlename in ["", random_string("middlename", 20)]
    #for nickname in ["", random_string("nickname", 20)]
    #for title in ["", random_string("title", 20)]
    #for company in ["", random_string("company", 20)]
    #for address in ["", random_string("address", 20)]
    #for home_phone in ["", random_string("home_phone", 20)]
    #for mobile in ["", random_string("mobile", 20)]
    #for work_phone in ["", random_string("work_phone", 20)]
    #for fax in ["", random_string("fax", 20)]
    #for email in ["", random_string("email", 20)]
    #for email2 in ["", random_string("email2", 20)]
    #for email3 in ["", random_string("email3", 20)]
    #for address2 in ["", random_string("address2", 20)]
    #for phone2 in ["", random_string("phone2", 20)]
    #for notes in ["", random_string("notes", 20)]
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    print("old contacts")
    print(sorted(old_contacts, key=Contact.id_or_max))
    print("new contacts")
    print(sorted(new_contacts, key=Contact.id_or_max))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


