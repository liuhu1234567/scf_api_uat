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

    def password_input(self, username):
        self.send_keys(self.username_element, username)
        return username


obj = loginPage()
obj.open('https://uat-cloud.dianliantech.com/user/login')
obj.user_input('AEW6317585245519')