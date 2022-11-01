from elementpage.home import Home
from elementpage.table_procurement import TableProcurement
from common.do_selenium import *
import unittest
from common.do_faker import get_number
from config.all_path import get_file_path

'''采购数据'''
class Procurement(unittest.TestCase):
    def test_001_procurement(self):
        '''导入采购数据'''
        png_path = get_file_path('caigou.xlsx')
        obj = TableProcurement()
        obj.open('https://uat-cloud.dianliantech.com/user/login')
        obj.user_input('ML4W17585245519')
        obj.password_input('Ss123456')
        obj.code_input('1234')
        obj.loginButton_clike()
        obj.into_clike()
        sleep(1)
        obj.iframe_add()
        obj.management_clike()
        obj.procurement_clike()
        obj.contains_clike()
        obj.upload_clike()
        obj.uploadWinFile(png_path)
        obj.table_determine_input()
