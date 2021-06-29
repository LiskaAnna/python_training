from model.contact import Contact
from random import randrange


def test_update_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", middlename="Ivan", lastname="Ivanov",
                               nickname="ivanov", title="iv", company="IV", address="iviviv",
                               home_phone="123", mobile="456", work_phone="789", fax="987",
                               email="aaa@aa.com", email2="bbb@bb.com", email3="ccc@cc.com",
                               address2="aaaa", phone2="ssss", notes="dddd"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Petr", middlename="Petr", lastname="Semaforov",
                                             nickname="pet", title="ppp", company="pp", address="tgndgn",
                                             home_phone="111", mobile="222", work_phone="333", fax="444",
                                             email="aaa2@aa.com", email2="bbb2@bb.com", email3="ccc2@cc.com",
                                             address2="bbc", phone2="666", notes="nzgngn")
    contact.id = old_contacts[index].id
    app.contact.update_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

