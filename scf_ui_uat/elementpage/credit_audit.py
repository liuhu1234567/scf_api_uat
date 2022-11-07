from elementpage.home import Home
from common.do_selenium import *
from selenium.webdriver.common.by import By
from common.do_faker import get_number

'''授信审批'''


class CreditAudit(Home):
    input1_element = (By.XPATH, "//div[@id='ice-container']/div/section/div/main/div/div/ul/li/input")  # 授信申请人名称搜索框
    input2_element = (By.XPATH, "//div[@id='ice-container']/div/section/div/main/div/div/ul/li[2]/input")  # 授信方名称搜索框
    input3_element = (By.XPATH, "//div[@id='ice-container']/div/section/div/main/div/div/ul/li[3]/input")  # 金融产品名称搜索框
    input4_element = (By.ID, "rc_select_10")  # 状态
    input4_data_element = (By.XPATH, "//div[2]/div/div/div/div[2]/div")  # 状态下拉框
    preview_element = (By.XPATH, "//li[contains(.,'详情')]")  # 详情
    audit_element = (By.XPATH, "//li[contains(.,'审核')]")  # 审核
    audit_return_element = (By.XPATH, "//button[contains(.,'返 回')]")  # 返回
    audit_through_element = (By.XPATH, "//button[contains(.,'通 过')]")  # 通过
    audit_rejected_element = (By.XPATH, "//button[contains(.,'驳 回')]")  # 驳回
    audit_refused_element = (By.XPATH, "//button[contains(.,'拒 绝')]")  # 拒绝

    def input1_input(self):
        print('企业名称搜索框')
        self.send_keys(self.input1_element, 1)
