__author__ = 'Eugene'

from model.group import group


def test_big_modify_group_name(app):
    app.group.modify_first_group(group(name="New Name"))

def test_big_modify_group_header(app):
    app.group.modify_first_group(group(header="New Header"))