from elementpage.configuration import Configuration
from common.do_selenium import *
import unittest
from common.do_faker import get_number
from common.do_config import scf_financier, scf_enterprise, scf_supplier, scf_platform, scf_factor, scf_subsidiaries

'''产品配置'''
class Projest(unittest.TestCase):
    def test_001_projest_input(self):
        '''新建项目'''
        project_name = 'ui自动化项目名称' + get_number(6)
        process_name = 'ui自动化流程名称' + get_number(6)
        obj = Configuration()
        obj.open('https://uat-cloud.dianliantech.com/user/login')
        obj.user_input(scf_platform['username'])
        obj.password_input(scf_platform['password'])
        obj.code_input('1234')
        obj.loginButton_clike()
        obj.into_clike()
        sleep(1)
        obj.iframe_add()
        obj.configuration_clike()
        obj.project_clike()
        obj.project_add_clike()
        obj.project_name_clike(project_name)
        obj.enterpriseId_clike()
        obj.businessType_clike()
        obj.scfFinanceProductId_clike()
        obj.isCoreGrant_clike()
        obj.value_clike()
        obj.page_clike()
        obj.create_clike()
        obj.process_clike(process_name)
        obj.number_clike()
        obj.customerType0_clike()
        obj.cconfirm_clike()
        obj.isPush_clike()
        obj.isHistory_clike()
        obj.pushMaterial_clike()
        obj.financeRat_input()
        obj.serviceRate_input()
        obj.submit_clike()
        obj.exit()

    def test_002_projest_delete(self):
        '''分配项目'''
        obj = Configuration()
        obj.open('https://uat-cloud.dianliantech.com/user/login')
        obj.user_input(scf_platform['username'])
        obj.password_input(scf_platform['password'])
        obj.code_input('1234')
        obj.loginButton_clike()
        obj.into_clike()
        sleep(1)
        obj.iframe_add()
        obj.configuration_clike()
        obj.project_clike()
        obj.distribution_clike()
        obj.customer_clike()
        obj.determine_clike()
        obj.exit()

