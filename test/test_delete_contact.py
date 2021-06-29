from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", middlename="Ivan", lastname="Ivanov",
                               nickname="ivanov", title="iv", company="IV", address="iviviv",
                               home_phone="123", mobile="456", work_phone="789", fax="987",
                               email="aaa@aa.com", email2="bbb@bb.com", email3="ccc@cc.com",
                               address2="aaaa", phone2="ssss", notes="dddd"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts
