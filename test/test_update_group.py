from model.group import Group

def test_update_first_group(app):
    app.group.update_first_group(Group(name="aaa", header="aaaa", footer="aaaaa"))
