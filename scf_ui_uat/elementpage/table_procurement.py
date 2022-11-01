from elementpage.home import Home
from common.do_selenium import *
from selenium.webdriver.common.by import By
from common.do_faker import get_number
from config.all_path import get_file_path


class TableProcurement(Home):
    contains_element = (By.XPATH, "//span[contains(.,'批量导入')]")
    upload_element = (By.CSS_SELECTOR, '.Import--icon--B50GKYx')
    table_determine_element = (By.XPATH, '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/button')


    def contains_clike(self):
        print('点击批量上传')
        self.clike(self.contains_element)

    def upload_clike(self):
        print('点击上传文件')
        self.clike(self.upload_element)

    # def uploadWinFile_input(self,name):
    #     print('上传文件')
    #     self.uploadWinFile(name)

    def table_determine_input(self):
        print('点击确认')
        self.clike(self.table_determine_element)

# png_path = get_file_path('caigou.xlsx')
# table_name = 'ui自动化数据表名称' + get_number(6)
# obj = TableProcurement()
# obj.open('https://uat-cloud.dianliantech.com/user/login')
# obj.user_input('ML4W17585245519')
# obj.password_input('Ss123456')
# obj.code_input('1234')
# obj.loginButton_clike()
# obj.into_clike()
# sleep(1)
# obj.iframe_add()
# obj.management_clike()
# obj.procurement_clike()
# obj.contains_clike()
# obj.upload_clike()
# obj.uploadWinFile(png_path)
# obj.table_determine_input()
