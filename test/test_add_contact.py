# -*- coding: utf-8 -*-
from selenium import webdriver
from model.contact import Contact
from fixture.application import Application


def setUp(self):
    self.app = Application
    self.wd = webdriver.Firefox()
    self.wd.implicitly_wait(30)


def test_add_new_contact(app):
    app.contact.create(Contact(firstname="Ivan", middlename="Ivan", lastname="Ivanov",
                               nickname="ivanov", title="iv", company="IV", address="iviviv",
                               home_phone="123", mobile="456", work_phone="789", fax="987",
                               email="aaa@aa.com", email2="bbb@bb.com", email3="ccc@cc.com",
                               address2="aaaa", phone2="ssss", notes="dddd"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="",
                               title="", company="", address="", home_phone="", mobile="",
                               work_phone="", fax="", email="", email2="", email3="", address2="",
                               phone2="", notes=""))
