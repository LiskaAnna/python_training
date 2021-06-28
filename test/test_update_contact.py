from model.contact import Contact


def test_update_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", middlename="Ivan", lastname="Ivanov",
                               nickname="ivanov", title="iv", company="IV", address="iviviv",
                               home_phone="123", mobile="456", work_phone="789", fax="987",
                               email="aaa@aa.com", email2="bbb@bb.com", email3="ccc@cc.com",
                               address2="aaaa", phone2="ssss", notes="dddd"))
    app.contact.update_first_contact(Contact(firstname="Petr", middlename="Petr", lastname="Semaforov",
                                             nickname="pet", title="ppp", company="pp", address="tgndgn",
                                             home_phone="111", mobile="222", work_phone="333", fax="444",
                                             email="aaa2@aa.com", email2="bbb2@bb.com", email3="ccc2@cc.com",
                                             address2="bbc", phone2="666", notes="nzgngn"))
