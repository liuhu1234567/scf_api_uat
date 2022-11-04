from elementpage.loginPage import *
import unittest
from common.do_config import scf_financier, scf_enterprise, scf_supplier, scf_platform, scf_factor, scf_subsidiaries

'''登陆'''
class Landing(unittest.TestCase):
    def test_001_landing_platform(self):
        '''平台方登陆'''
        obj = loginPage()
        obj.open('https://uat-cloud.dianliantech.com/user/login')
        obj.user_input(scf_platform['username'])
        obj.password_input(scf_platform['password'])
        obj.code_input('1234')
        obj.loginButton_clike()
        obj.into_clike()
        obj.exit()

    def test_002_Landing_financier(self):
        '''资金方账号'''
        obj = loginPage()
        obj.open('https://uat-cloud.dianliantech.com/user/login')
        obj.user_input(scf_financier['username'])
        obj.password_input(scf_financier['password'])
        obj.code_input('1234')
        obj.loginButton_clike()
        obj.exit()

    def test_003_Landing_enterprise(self):
        '''核心企业账号'''
        obj = loginPage()
        obj.open('https://uat-cloud.dianliantech.com/user/login')
        obj.user_input(scf_enterprise['username'])
        obj.password_input(scf_enterprise['password'])
        obj.code_input('1234')
        obj.loginButton_clike()
        obj.exit()

    def test_004_Landing_supplier(self):
        '''供应商账号'''
        obj = loginPage()
        obj.open('https://uat-cloud.dianliantech.com/user/login')
        obj.user_input(scf_supplier['username'])
        obj.password_input(scf_supplier['password'])
        obj.code_input('1234')
        obj.loginButton_clike()
        obj.exit()

    def test_005_Landing_subsidiaries(self):
        '''核心子公司账号'''
        obj = loginPage()
        obj.open('https://uat-cloud.dianliantech.com/user/login')
        obj.user_input(scf_subsidiaries['username'])
        obj.password_input(scf_subsidiaries['password'])
        obj.code_input('1234')
        obj.loginButton_clike()
        obj.exit()

    def test_006_Landing_factor(self):
        '''保理商账号'''
        obj = loginPage()
        obj.open('https://uat-cloud.dianliantech.com/user/login')
        obj.user_input(scf_factor['username'])
        obj.password_input(scf_factor['password'])
        obj.code_input('1234')
        obj.loginButton_clike()
        obj.exit()





