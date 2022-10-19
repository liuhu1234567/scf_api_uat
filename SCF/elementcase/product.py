from elementpage.home import Home
from elementpage.product_element import Product
from common.do_selenium import *
import unittest
from common.do_faker import get_number

'''金融产品管理'''
class Product_add(unittest.TestCase):
    def test_001_product_add_input(self):
        name = 'ui自动化产品名称' + get_number(6)
        # Product_name = 'ui自动化金融机构名称' + get_number(6)
        obj = Product()
        obj.open('https://uat-cloud.dianliantech.com/user/login')
        obj.user_input('ML4W17585245519')
        obj.password_input('Ss123456')
        obj.code_input('1234')
        obj.loginButton_clike()
        obj.into_clike()
        sleep(1)
        obj.iframe_add()
        obj.product_clike()
        obj.product_list_clike()
        obj.product_add_clike()
        obj.name_input(name)
        obj.financeId_input()
        obj.amountMin_input('0.1')
        obj.amountMax_input('0.2')
        obj.rateMin_input('1')
        obj.rateMax_input('10')
        obj.loop_input()
        obj.single_input()
        obj.selection_input()
        obj.repaymentType_input()
        obj.available_input()
        obj.loan_input()
        obj.ue2ldsD_input()
        obj.exit()


