from common.do_selenium import *
from selenium.webdriver.common.by import By

class loginPage(BasePage):
    username_element = (By.ID, "basic_username")
    password_element = (By.ID, "basic_password")
    code_element = (By.ID, "basic_code")
    loginButton_element = (By.CSS_SELECTOR, '#basic > div.ant-row.ant-form-item._FormBottom_h5mzm_273 > div > div > div > button > span')
    into_element = (By.XPATH , '//*[@id="ice-container"]/div/section/div[2]/main/div/div/div[2]/div/div/div/div[1]/ul/li[2]/div[2]/div[2]/span/img')
    into_one_element = (By.XPATH,
                    '//*[@id="ice-container"]/div/section/div[2]/main/div/div/div[2]/div/div/div/div[1]/ul/li/div[2]/div[2]/span')
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

    def into_clike(self):
        self.clike(self.into_element)

    def into_one_clike(self):
        self.clike(self.into_one_element)

usernamess_element = (By.XPATH, '//*[@id="ice-container"]/div/section/div[1]/div/ul/li[4]/span/img[2]')

#调试
obj = loginPage()
obj.open('https://uat-cloud.dianliantech.com/user/login')
obj.user_input('ML4W17585245519')
obj.password_input('Ss123456')
obj.code_input('1234')
obj.loginButton_clike()
obj.wait_element_visibility(usernamess_element)
# obj.into_clike()
# obj.exit()