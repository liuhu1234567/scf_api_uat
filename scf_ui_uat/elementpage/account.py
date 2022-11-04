from elementpage.home import Home
from common.do_selenium import *
from selenium.webdriver.common.by import By
from common.do_faker import get_number

'''银行账户管理'''


class Account(Home):
    bankadd_element = (By.XPATH, "//button[contains(.,'新增')]")  # 新增
    bankAccountName_element = (By.ID, 'bankAccountName')  # 账户名称
    bankAccountNo_element = (By.ID, 'bankAccountNo')  # 银行账号
    bankAccountSite_element = (By.ID, 'bankAccountSite')  # 开户银行网点
    bankAccountDebutNo_element = (By.ID, 'bankAccountDebutNo')  # 开户行联行号
    bankAccountType_element = (By.ID, 'bankAccountType')  # 账户类型
    bankAccountType2_element = (By.ID, '//div[2]/div/div/div/div[2]/div')  # 账户类型下拉
    determine_element = (By.XPATH, "//button[contains(.,'确 定')]")  # 确认
    cancel_element = (By.XPATH, "//span[contains(.,'取消')]")  # 取消
    associated_element = (By.XPATH, "//span[contains(.,'关联项目')]")  # 关联项目
    associated1_element = (By.XPATH, "//label/span/input")  # 关联项目下拉框
    associated1_determine_element = (By.XPATH, "//span[contains(.,'确 定')]")  # 确定
    change_element = (By.XPATH, "//span[contains(.,'修改')]")  # 修改
    ssociated_element = (By.XPATH, "//span[contains(.,'删除')]")  # 删除
    view_element = (By.XPATH, "//span[contains(.,'查看')]")  # 查看
    input1_element = (By.XPATH, "//input[@value='1']")  # 银行账号搜索框
    input2_element = (By.XPATH, "//input[@value='2']")  # 开户银行网点搜索框

    def apply_clike(self):
        print('点击新增')
        self.clike(self.bankadd_element)
