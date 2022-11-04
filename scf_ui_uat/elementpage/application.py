from elementpage.home import Home
from common.do_selenium import *
from selenium.webdriver.common.by import By
from common.do_faker import get_number

'''产品申请'''


class Configuration(Home):
    a1ply_element = (By.XPATH,
                     '//*[@id="ice-container"]/div/section/div/main/div/div/div/div/div/div/div/div/div/div/table/tbody/tr[4]/td[11]/div/div[1]/button/span')
    apply_ok_element = (By.XPATH,
                        '//*[@id="ice-container"]/div/section/div/main/div/div/div/div/div[1]/form/div[9]/div/div/div[2]/button')

    def apply_clike(self):
        print('列表申请融资')
        self.clike(self.a1ply_element)

    def apply_ok_clike(self):
        print('金融产品页面申请融资')
        self.clike(self.apply_ok_element)

# obj=Configuration()
# obj.open('https://uat-cloud.dianliantech.com/user/login')
# obj.user_input('AEW6317585245519')
# obj.password_input('Aa1234567')
# obj.code_input('1234')
# obj.loginButton_clike()
# obj.into_one_clike()
# sleep(1)
# obj.iframe_add()
# obj.product_supplier_clike()
# obj.production_clike()
# obj.apply_clike()
# obj.apply_ok_clike()
