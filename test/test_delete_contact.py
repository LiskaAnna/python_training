from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", middlename="Ivan", lastname="Ivanov",
                               nickname="ivanov", title="iv", company="IV", address="iviviv",
                               home_phone="123", mobile="456", work_phone="789", fax="987",
                               email="aaa@aa.com", email2="bbb@bb.com", email3="ccc@cc.com",
                               address2="aaaa", phone2="ssss", notes="dddd"))
    app.contact.delete_first_contact()
