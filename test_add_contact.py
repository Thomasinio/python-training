from selenium import webdriver
import unittest
from group import Contact

class Add_contact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(60)
    
    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def login(self, driver, username, password):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        
    def open_new_contact_page(self, driver):
        driver.find_element_by_link_text("add new").click()
        
    def create_contact(self, driver, group):    
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(group.firstname)
        driver.find_element_by_name("middlename").click()
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(group.middlename)
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(group.lastname)
        driver.find_element_by_name("nickname").click()
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(group.nickname)
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(group.address)
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(group.mobile)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(group.email)
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def test_add_contact(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, username = "admin", password = "secret")
        self.open_new_contact_page(driver)
        self.create_contact(driver, Contact(firstname = "Igor", middlename = "von", lastname = "V", nickname = "Thomas",
            address = "Blyuhera 7", mobile = "0936629380", email = "ivv@test.com"))
        self.logout(driver)        
    
    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
