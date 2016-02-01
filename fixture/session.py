__author__ = 'thomas'

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        driver = self.driver
        self.app.open_home_page(driver)
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text("Logout").click()
