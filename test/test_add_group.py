import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username = "admin", password = "secret")
    app.create_group(Group(name = "PyGroup", header = "Head", footer = "Foot"))
    app.session.logout()

def test_add_emply_group(app):
    app.session.login(username = "admin", password = "secret")
    app.create_group(Group(name = "", header = "", footer = ""))
    app.session.logout()
