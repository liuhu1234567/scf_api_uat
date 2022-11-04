from elementpage.home import Home
from common.do_selenium import *
from selenium.webdriver.common.by import By
from common.do_faker import get_number

'''授信审核'''


class CreditAudit(Home):
    input1_element = (By.XPATH, "//input[@value='1']")  # 授信申请人名称搜索框
    input2_element = (By.XPATH, "//input[@value='2']")  # 授信方名称搜索框
    input3_element = (By.XPATH, "//input[@value='3']")  # 金融产品名称搜索框
    input4_element = (By.XPATH, "//span/input")  # 状态搜索框
    input4_data_element = (By.XPATH, "//div[2]/div/div/div/div[2]/div")  # 状态下拉框数据
    preview_element = (By.XPATH, "//li[contains(.,'详情')]")  # 详情
    credit_return_element = (By.XPATH, "//span[contains(.,'返 回')]")  # 返回
    credit_rejected_element = (By.XPATH, "//span[contains(.,'驳 回')]")  # 驳回
    credit_through_element = (By.XPATH, "//span[contains(.,'通 过')]")  # 通过
    credit_rejectedto_element = (By.XPATH, "//span[contains(.,'拒 绝')]")  # 拒绝

    def input1_input(self):
        print('企业名称搜索框')
        self.send_keys(self.input1_element, 1)
