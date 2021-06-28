from model.contact import Contact


def test_update_first_contact(app):
    app.contact.update_first_contact(Contact(firstname="Petr", middlename="Petr", lastname="Semaforov",
                                             nickname="pet", title="ppp", company="pp", address="tgndgn",
                                             home_phone="111", mobile="222", work_phone="333", fax="444",
                                             email="aaa2@aa.com", email2="bbb2@bb.com", email3="ccc2@cc.com",
                                             address2="bbc", phone2="666", notes="nzgngn"))
