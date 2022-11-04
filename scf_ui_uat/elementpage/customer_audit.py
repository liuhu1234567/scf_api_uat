from elementpage.home import Home
from common.do_selenium import *
from selenium.webdriver.common.by import By
from common.do_faker import get_number

'''客户审核'''


class CustomerAudit(Home):
    input1_element = (By.XPATH, "//input[@value='1']")  # 企业名称搜索框
    input2_element = (By.XPATH, "//input[@value='2']")  # 联系人搜索框
    input3_element = (By.XPATH, "//input[@value='3']")  # 联系人手机号码搜索框
    input4_element = (By.XPATH, "//span[contains(.,'全部')]")  # 客户类型搜索框
    input4_data_element = (By.XPATH, "//div[2]/div/div/div/div[2]/div")  # 客户类型下拉框数据
    view_element = (By.XPATH, "//span[contains(.,'查看')]")  # 查看
    audit_element = (By.XPATH, "//span[contains(.,'审核')]")  # 审核
    audit_return_element = (By.XPATH, "//span[contains(.,'返 回')]")
    audit_rejected_element = (By.XPATH, "//span[contains(.,'驳 回')]")
    audit_through_element = (By.XPATH, "//span[contains(.,'通 过')]")
    audit_rejectedto_element = (By.XPATH, "//span[contains(.,'拒 绝')]")

    def input1_input(self):
        print('企业名称搜索框')
        self.send_keys(self.input1_element, 1)
