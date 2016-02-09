from model.contact import Contact

def test_add_contact(app):
    app.contact.create_contact(Contact(firstname = "Igor", middlename = "von", lastname = "V", nickname = "Thomas",
        address = "Blyuhera 7", mobile = "0936629380", email = "ivv@test.com"))

