from model.group import Group
from model.contact import Contact
import random

def test_remove_contact_from_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Ivan", middlename="Ivan", lastname="Ivanov",
                                   nickname="ivanov", title="iv", company="IV", address="iviviv",
                                   home_phone="123", mobile="456", work_phone="789", fax="987",
                                   email="aaa@aa.com", email2="bbb@bb.com", email3="ccc@cc.com",
                                   address2="aaaa", phone2="ssss", notes="dddd"))
    groups = db.get_group_list()
    group = random.choice(groups)
    if len(db.get_contact_list_by_group(group.id)) == 0:
        contacts = db.get_contact_list()
        contact = random.choice(contacts)
        app.contact.add_contact_to_group(contact.id, group.id)
    contacts = db.get_contact_list_by_group(group.id)
    contact = random.choice(contacts)
    app.contact.remove_contact_from_group(group.id, contact.id)
    assert not db.check_contact_in_group(contact.id, group.id)