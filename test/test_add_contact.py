import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.create_contact(Contact(firstname = "Igor", middlename = "von", lastname = "V", nickname = "Thomas",
        address = "Blyuhera 7", mobile = "0936629380", email = "ivv@test.com"))
    app.session.logout()
