from elementpage.home import Home
from common.do_selenium import *
from selenium.webdriver.common.by import By
from common.do_faker import get_number

'''授信审核'''


class LinesAudit(Home):
    input1_element = (By.XPATH, "//div[@id='ice-container']/div/section/div/main/div/div/ul/li/input")  # 企业名称搜索框
    input2_element = (By.XPATH, "//div[@id='ice-container']/div/section/div/main/div/div/ul/li[2]/input")  # 授信方名称搜索框
    input3_element = (By.XPATH, "//div[@id='ice-container']/div/section/div/main/div/div/ul/li[3]/input")  # 项目名称搜索框
    input4_element = (By.ID, "rc_select_29")  # 状态
    input4_data_element = (By.XPATH, "//div[2]/div/div/div/div/div")  # 状态下拉框
    preview_element = (By.XPATH, "//li[contains(.,'详情')]")  # 详情
    delete_element = (By.XPATH, "//li[contains(.,'审批')]")  # 删除
    return_element = (By.XPATH, "//span[contains(.,'返 回')]")  # 返回
    rejected_element = (By.XPATH, "//span[contains(.,'驳 回')]")  # 驳回
    through_element = (By.XPATH, "//span[contains(.,'通 过')]")  # 通过
    auditOpinion_element = (By.XPATH, "auditOpinion")  # 驳回意见

    def input1_input(self):
        print('企业名称搜索框')
        self.send_keys(self.input1_element, 1)
