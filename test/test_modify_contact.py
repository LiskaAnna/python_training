# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import allure

def test_modify_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Ivan", middlename="Ivan", lastname="Ivanov",
                                   nickname="ivanov", title="iv", company="IV", address="iviviv",
                                   home_phone="123", mobile="456", work_phone="789", fax="987",
                                   email="aaa@aa.com", email2="bbb@bb.com", email3="ccc@cc.com",
                                   address2="aaaa", phone2="ssss", notes="dddd"))
    with allure.step('Given a non-empty contact list'):
        old_contacts = db.get_contact_list()
    with allure.step('Given a random contact from the list'):
        contact = random.choice(old_contacts)
    with allure.step('When I modify the contact from the list'):
        contact1 = Contact(firstname="New_contact")
        contact1.id = contact.id
        app.contact.modify_contact_by_id(contact.id, contact1)
    with allure.step('Then the new contact list is equal to the old list with the modified contact'):
        new_contacts = db.get_contact_list()
        for element in old_contacts:
            if element.id == contact.id:
                element.firstname = contact1.firstname
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)