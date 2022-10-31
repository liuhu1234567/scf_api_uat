from elementpage.loginPage import *
import unittest

'''登陆'''
class Landing(unittest.TestCase):
    def test_001_landing_platform(self):
        '''平台方登陆'''
        obj = loginPage()
        obj.open('https://uat-cloud.dianliantech.com/user/login')
        obj.user_input('ML4W17585245519')
        obj.password_input('Ss123456')
        obj.code_input('1234')
        obj.loginButton_clike()
        obj.into_clike()
        obj.exit()

    def test_002_Landing_financier(self):
        '''资金方账号'''
        obj = loginPage()
        obj.open('https://uat-cloud.dianliantech.com/user/login')
        obj.user_input('BFW17585245519')
        obj.password_input('Aa1234567')
        obj.code_input('1234')
        obj.loginButton_clike()
        obj.exit()

    def test_003_Landing_enterprise(self):
        '''核心企业账号'''
        obj = loginPage()
        obj.open('https://uat-cloud.dianliantech.com/user/login')
        obj.user_input('FDN17585245519')
        obj.password_input('Aa1234567')
        obj.code_input('1234')
        obj.loginButton_clike()
        obj.exit()

    def test_004_Landing_supplier(self):
        '''供应商账号'''
        obj = loginPage()
        obj.open('https://uat-cloud.dianliantech.com/user/login')
        obj.user_input('AEW6317585245519')
        obj.password_input('Aa1234567')
        obj.code_input('1234')
        obj.loginButton_clike()
        obj.exit()

    def test_005_Landing_subsidiaries(self):
        '''核心子公司账号'''
        obj = loginPage()
        obj.open('https://uat-cloud.dianliantech.com/user/login')
        obj.user_input('UPC217585245519')
        obj.password_input('Aa1234567')
        obj.code_input('1234')
        obj.loginButton_clike()
        obj.exit()

    def test_006_Landing_factor(self):
        '''保理商账号'''
        obj = loginPage()
        obj.open('https://uat-cloud.dianliantech.com/user/login')
        obj.user_input('BZW17585245519')
        obj.password_input('Aa1234567')
        obj.code_input('1234')
        obj.loginButton_clike()
        obj.exit()





