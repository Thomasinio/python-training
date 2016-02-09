from model.group import Group

def test_add_group(app):
    app.group.create(Group(name = "PyGroup", header = "Head", footer = "Foot"))

def test_add_empty_group(app):
    app.group.create(Group(name = "", header = "", footer = ""))
