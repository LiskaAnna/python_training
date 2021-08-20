# -*- coding: utf-8 -*-
from model.group import Group
import random
import allure


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    with allure.step('Given a non-empty group list'):
        old_groups = db.get_group_list()
    with allure.step('Given a random group from the list'):
        group = random.choice(old_groups)
    with allure.step('When I modify the group from the list'):
        group1 = Group(name="New group")
        group1.id = group.id
        app.group.modify_group_by_id(group.id, group1)
    with allure.step('Then the new group list is equal to the old list with the modified group'):
        new_groups = db.get_group_list()
        for element in old_groups:
            if element.id == group.id:
                element.name = group1.name
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

