from elementpage.data_table import DataTable
from common.do_selenium import *
import unittest
from common.do_faker import get_number
from common.do_config import scf_financier, scf_enterprise, scf_supplier, scf_platform, scf_factor, scf_subsidiaries

'''数据表配置'''


class Table(unittest.TestCase):
    def test_001_table_input(self):
        '''新建数据表配置'''
        table_name = 'ui自动化数据表名称' + get_number(6)
        obj = DataTable()
        obj.open('https://uat-cloud.dianliantech.com/user/login')
        obj.user_input(scf_platform['username'])
        obj.password_input(scf_platform['password'])
        obj.code_input('1234')
        obj.loginButton_clike()
        obj.into_clike()
        sleep(1)
        obj.iframe_add()
        obj.configuration_clike()
        obj.table_clike()
        obj.table_add_clike()
        obj.table_name_input(table_name)
        obj.value_type_clike()
        obj.customer_type_clike()
        obj.templateId_clike()
        obj.itemId_clike()
        obj.according_clike()
        obj.confirm_table_clike()
