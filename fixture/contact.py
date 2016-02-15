class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_new_contact_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("add new").click()

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        driver = self.app.driver
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)

    def create_contact(self, group):
        driver = self.app.driver
        self.open_new_contact_page()
        self.fill_contact_form(group)
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def select_first_contact(self):
        driver = self.app.driver
        driver.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        driver = self.app.driver
        self.select_first_contact()
        driver.find_element_by_xpath(".//*[@id='content']/form[2]/div[2]/input").click()
        driver.switch_to_alert().accept()

    def modify_first_contact(self, new_contact_data):
        driver = self.app.driver
        # go home
        driver.find_element_by_xpath(".//*[@id='nav']/ul/li[1]/a")
        self.select_first_contact()
        # edit
        driver.find_element_by_xpath("//*[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill
        self.fill_contact_form(new_contact_data)
        # submit
        driver.find_element_by_name("update").click()

    def count(self):
        driver = self.app.driver
        return len(driver.find_elements_by_name("selected[]"))