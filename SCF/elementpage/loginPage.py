from common.do_selenium import *
from selenium.webdriver.common.by import By

class loginPage(BasePage):
    username_element = (By.ID, "basic_username")
    password_element = (By.ID, "basic_password")
    code_element = (By.ID, "basic_code")
    loginButton_element = (By.CSS_SELECTOR, '#basic > div.ant-row.ant-form-item._FormBottom_h5mzm_273 > div > div > div > button > span')

    def user_input(self, username):
        self.send_keys(self.username_element, username)
        return username

    def password_input(self, password):
        self.send_keys(self.password_element, password)
        return password

    def code_input(self, code):
        self.send_keys(self.code_element, code)
        return code

    def loginButton_clike(self):
        self.clike(self.loginButton_element)



obj = loginPage()
obj.open('https://uat-cloud.dianliantech.com/user/login')
obj.user_input('AEW6317585245519')
obj.password_input('Aa1234567')
obj.code_input('1234')
obj.loginButton_clike()